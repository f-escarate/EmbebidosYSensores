#include "esp_log.h"
#include "BMI270.c"
#include "freertos/FreeRTOS.h"
#include "gpio_interrupt.c"

#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/uart.h"

#define BUF_SIZE 127

TaskHandle_t myTaskHandle = NULL;
const uart_port_t uart_num = UART_NUM_0;

// Selecting power mode-> Suspend:0, Low:1, Normal:2, Performance:3
uint8_t pwr_mode = 2;
// Setting Sample rate and sensibility config
uint8_t acc_odr = 7;    // From 1 to 12 (5 to 12 in normal/perf mode) (1 to 10 in low)
uint8_t gyr_odr = 6;    // From 6 to 13 (6 to 8 in low mode)
uint8_t acc_sens = 2;   // From 0 to 3
uint8_t gyr_sens = 0;   // From 0 to 4
uint8_t *change;

void refresh_config(){
    // Intento de Anymotion
    //set_anymo2(0xAA);
    //set_anymo1(0x05, 0, 0, 1);
    
    set_acc_sensibility(acc_sens);      // reg 0x41
    set_gyr_sensibility(gyr_sens, 0);   // reg 0x43
    set_pwrmode_and_ODRs(pwr_mode, acc_odr, gyr_odr);
    internal_status();
    *change = 0;
}

void read_serial_task(void *arg){   
    uart_config_t uart_config = {
        .baud_rate = 115200,
        .data_bits = UART_DATA_8_BITS,
        .parity = UART_PARITY_DISABLE,
        .stop_bits = UART_STOP_BITS_1,
        .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
        .rx_flow_ctrl_thresh = 122,
        .source_clk = UART_SCLK_DEFAULT,
    };
    // Install UART driver (we don't need an event queue here)
    // In this example we don't even use a buffer for sending data.
    ESP_ERROR_CHECK(uart_driver_install(uart_num, BUF_SIZE * 2, 0, 0, NULL, 0));
    // Configure UART parameters
    ESP_ERROR_CHECK(uart_param_config(uart_num, &uart_config));

    uint8_t data[128];
    while(1){
        int length = 0;
        ESP_ERROR_CHECK(uart_get_buffered_data_len(uart_num, (size_t*)&length));
        length = uart_read_bytes(uart_num, data, length, 100);
        
        if(length > 0){
            //printf("TUKI %d %d %d %d %d %d\n", data[0], data[1], data[2], data[3], data[4], data[5] );
            *change = 1;
            switch(data[0]){
                case 0:
                case 1:
                    pwr_mode = data[1];
                    acc_odr = data[2];    // From 1 to 12 (5 to 12 in normal/perf mode) (1 to 10 in low)
                    acc_sens = data[3];   // From 0 to 3
                    gyr_odr = data[4];    // From 6 to 13 (6 to 8 in low mode)
                    gyr_sens = data[5];   // From 0 to 4
                case 2:
            }
            refresh_config();
        }
        vTaskDelay(1000/ portTICK_RATE_MS);
    }
}

void send_data(const char *data, size_t length) {
    uart_write_bytes(uart_num, data, length);
}

#include <stdio.h>
#include <unistd.h>

void app_main(void) {
    //ESP_ERROR_CHECK(bmi_init());
    //softreset();
    //chipid();
    //initialization();
    //check_initialization();

    change = (uint8_t*) malloc(sizeof(uint8_t));
    *change = 0;

    xTaskCreate(read_serial_task, "read_serial_task", 4096, NULL, 10, &myTaskHandle);
    
    printf("Comienza lectura\n\n");
    refresh_config();
    uint8_t len = 1 + sizeof(float)*7 + 1;
    char* msg = malloc(len);
    msg[0] = '~';
    msg[len-1] = '\n';
    
    while(1){
        if(!(*change)){
            lectura(acc_sens, gyr_sens, msg);
            uart_write_bytes(uart_num, (const char*)msg, len);
        }

    }
    printf("Fin de la lectura");
    
}