#include <stdio.h>
#include <unistd.h>
#include "esp_log.h"
#include "BMI270.c"
#include "bme68x_lib.h"
#include "freertos/FreeRTOS.h"

#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/uart.h"

#define BUF_SIZE 127

#define SENSOR_NONE 0
#define SENSOR_BMI270 1
#define SENSOR_BME688 2

TaskHandle_t myTaskHandle = NULL;
const uart_port_t uart_num = UART_NUM_0;
uart_config_t uart_config = {
        .baud_rate = 115200,
        .data_bits = UART_DATA_8_BITS,
        .parity = UART_PARITY_DISABLE,
        .stop_bits = UART_STOP_BITS_1,
        .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
        .rx_flow_ctrl_thresh = 122,
        .source_clk = UART_SCLK_DEFAULT,
    };

// --------------- BMI270 CONFIG -----------------------------------

uint8_t *change;
uint8_t ACC_SENS;
uint8_t GYR_SENS;

// --------------- BME688 CONFIG -----------------------------------
//uint8_t ope_mode = BME68X_PARALLEL_MODE;
uint8_t ope_mode = BME68X_FORCED_MODE;
uint32_t bme_delay;
uint16_t shared_heatr_dur = 0;


void BMI270_config(uint8_t pwr_mode, uint8_t acc_odr, uint8_t acc_sens, uint8_t gyr_odr, uint8_t gyr_sens){
    // Selecting power mode-> Suspend:0, Low:1, Normal:2, Performance:3
    // and setting Sample rate and sensibility config
    // acc_odr  From 1 to 12 (5 to 12 in normal/perf mode) (1 to 10 in low)
    // gyr_odr  From 6 to 13 (6 to 8 in low mode)
    // acc_sens From 0 to 3
    // gyr_sens From 0 to 4
    ACC_SENS = acc_sens;
    GYR_SENS = gyr_sens;
    
    set_acc_sensibility(acc_sens);      // reg 0x41
    set_gyr_sensibility(gyr_sens, 0);   // reg 0x43
    set_pwrmode_and_ODRs(pwr_mode, acc_odr, gyr_odr);
    internal_status();
    *change = 0;
}

void to_forced(bme68x_lib_t* const me){
    ope_mode = BME68X_FORCED_MODE;
    bme68x_lib_set_filter(me, BME68X_FILTER_OFF);   
    bme68x_lib_set_tph(me, BME68X_OS_2X, BME68X_OS_1X, BME68X_OS_16X);
    bme68x_lib_set_heater_prof_for(me, 300, 100);
    bme68x_lib_set_op_mode(me, ope_mode);
}

void to_parallel(bme68x_lib_t* const me){
    ope_mode = BME68X_PARALLEL_MODE;
    /* Heater temperature in degree Celsius */
    uint16_t temp_prof[10] = { 320, 100, 100, 100, 200, 200, 200, 320, 320, 320 };
    /* Multiplier to the shared heater duration */
    uint16_t mul_prof[10] = { 5, 2, 10, 30, 5, 5, 5, 5, 5, 5 };

    bme68x_lib_set_tph(me, BME68X_OS_2X, BME68X_OS_16X, BME68X_OS_1X);

    shared_heatr_dur = (uint16_t)(140 - bme68x_lib_get_meas_dur(me, ope_mode) / 1000);

    bme68x_lib_set_heater_prof_par(me, temp_prof, mul_prof, shared_heatr_dur, 10);
    bme68x_lib_set_op_mode(me, ope_mode);
}

void BME688_config(uint8_t mode, bme68x_lib_t* const me){
    if (mode == 0){
        to_parallel(me);
    } else if (mode == 1){
        to_forced(me);
    }
}

static i2c_t i2c;
bme68x_lib_t* const setup_BME688(){
    /* I2C parameters to configure the BME68x device */
    i2c.i2c_conf.mode = I2C_MODE_MASTER;
    i2c.i2c_conf.sda_io_num = GPIO_NUM_21;
    i2c.i2c_conf.scl_io_num = GPIO_NUM_22;
    i2c.i2c_conf.sda_pullup_en = GPIO_PULLUP_ENABLE;
    i2c.i2c_conf.scl_pullup_en = GPIO_PULLUP_ENABLE;
    i2c.i2c_conf.master.clk_speed = 400000;
    i2c.i2c_addr = BME68X_I2C_ADDR_LOW;
    i2c.i2c_num = I2C_NUM_0;
    
    bme68x_lib_t* const me = malloc(sizeof(bme68x_lib_t));
    printf("%d\n", bme68x_lib_init(me, &i2c, BME68X_I2C_INTF));

    return me;
}

void read_serial_task(void *arg){  
    bme68x_lib_t* const me = arg;

    uint8_t data[128];
    while(1){
        int length = 0;
        ESP_ERROR_CHECK(uart_get_buffered_data_len(uart_num, (size_t*)&length));
        length = uart_read_bytes(uart_num, data, length, 100);
        if(length > 0){
            //printf("TUKI %d %d %d %d %d %d\n", data[0], data[1], data[2], data[3], data[4], data[5] );
            *change = 1;
            switch(data[0]){
                case SENSOR_NONE:
                    continue;
                case SENSOR_BMI270:
                    BMI270_config(data[1], data[2], data[3], data[4], data[5]);
                case SENSOR_BME688:
                    BME688_config(data[1], me);
                    
            }
        }
        vTaskDelay(1000/ portTICK_RATE_MS);
    }
}

void send_data(const char *data, size_t length) {
    uart_write_bytes(uart_num, data, length);
}


void app_main(void) {
    // Install UART driver (we don't need an event queue here)
    // In this example we don't even use a buffer for sending data.
    ESP_ERROR_CHECK(uart_driver_install(uart_num, BUF_SIZE * 2, 0, 0, NULL, 0));
    // Configure UART parameters
    ESP_ERROR_CHECK(uart_param_config(uart_num, &uart_config));

    change = (uint8_t*) malloc(sizeof(uint8_t));
    *change = 0;

    uint8_t data[128];
    while(1){
        int length = 0;
        ESP_ERROR_CHECK(uart_get_buffered_data_len(uart_num, (size_t*)&length));
        length = uart_read_bytes(uart_num, data, length, 100);
        if(length > 0){
            switch(data[0]){
                case SENSOR_NONE:
                    continue;
                case SENSOR_BMI270:
                    ESP_ERROR_CHECK(bmi_init());
                    softreset();
                    chipid();
                    initialization();
                    check_initialization();
                    BMI270_config(data[1], data[2], data[3], data[4], data[5]);

                    xTaskCreate(read_serial_task, "read_serial_task", 4096, NULL, 10, &myTaskHandle);

                    printf("Comienza lectura\n\n");
                    uint8_t len = 1 + sizeof(float)*7 + 1;
                    char* msg = malloc(len);
                    msg[0] = '~';
                    msg[len-1] = '\n';
                    
                    while(1){
                        if(!(*change)){
                            lectura(ACC_SENS, GYR_SENS, msg);
                            uart_write_bytes(uart_num, (const char*)msg, len);
                        }

                    }
                    printf("Fin de la lectura");
                    break;

                
                case SENSOR_BME688:
                    bme68x_lib_t* const me = setup_BME688();
                    BME688_config(data[1], me);

                    xTaskCreate(read_serial_task, "read_serial_task", 4096, me, 10, &myTaskHandle);

                    if(bme68x_lib_intf_error(me) == 0){
                        while(1){
                            if(ope_mode == BME68X_FORCED_MODE){
                                bme68x_lib_set_op_mode(me, ope_mode);
                                bme_delay = bme68x_lib_get_meas_dur(me, ope_mode);
                            }else{
                                bme_delay = bme68x_lib_get_meas_dur(me, ope_mode) + (shared_heatr_dur * 1000);
                            }
                            printf("%lu %d \n", bme_delay, ope_mode);
                            (me->bme6).delay_us(bme_delay, (me->bme6).intf_ptr);
                            bme68x_lib_fetch_data(me);
                            bme68x_data_t* data = bme68x_lib_get_all_data(me);
                            printf("temp %f, press %f, hum %f\n", data->temperature, data->pressure, data->humidity);
                        }
                    }
                    break;    
            }
        }
        sleep(1);
    }
    
}