#include "esp_log.h"
#include "BMI270.c"


void app_main(void)
{
    ESP_ERROR_CHECK(bmi_init());
    softreset();
    chipid();
    initialization();
    check_initialization();

    // Setting Sample rate and sensibility config
    uint8_t ACC_CONF = acc_odr(8);              // reg 0x40
    uint8_t ACC_RANGE = acc_sensibility(2);     // reg 0x41
    uint8_t GYR_CONF = gyr_odr(9);              // reg 0x42
    uint8_t GYR_RANGE = gyr_sensibility(0,0);   // reg 0x43
    // Selecting power mode-> Suspend:0, Low:1, Normal:2, Performance:3
    uint8_t pwr_mode = 2;
    uint8_t* aux = powermodes(pwr_mode);
    uint8_t PWR_CTRL = aux[0];                  // reg 0x7D
    uint8_t ACC_CONF2 = aux[1];                 // reg 0x40
    uint8_t GYR_CONF2 = aux[2];                 // reg 0x42
    uint8_t PWR_CONF = aux[3];                  // reg 0x7C
    ACC_CONF = ACC_CONF | ACC_CONF2;
    GYR_CONF = GYR_CONF | GYR_CONF2;
    free(aux);
    // Defining the registers where we are going to write
    uint8_t reg_acc_conf = 0x40;
    uint8_t reg_acc_rng  = 0x41;
    uint8_t reg_gyr_conf = 0x42;
    uint8_t reg_gyr_rng  = 0x43;
    uint8_t reg_pwr_conf = 0x7C;
    uint8_t reg_pwr_ctrl = 0x7D;
    // Writing
    bmi_write(I2C_NUM_0, &reg_acc_conf, &ACC_CONF,1);
    bmi_write(I2C_NUM_0, &reg_acc_rng, &ACC_RANGE,1);
    bmi_write(I2C_NUM_0, &reg_gyr_conf, &GYR_CONF,1);
    bmi_write(I2C_NUM_0, &reg_gyr_rng, &GYR_RANGE,1);
    bmi_write(I2C_NUM_0, &reg_pwr_conf, &PWR_CONF,1);
    bmi_write(I2C_NUM_0, &reg_pwr_ctrl, &PWR_CTRL,1);

    internal_status();    
    printf("Comienza lectura\n\n");
    lectura();
    
}