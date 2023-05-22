#include "esp_log.h"
#include "BMI270.c"
#include "freertos/FreeRTOS.h"
#include "gpio_interrupt.c"


void app_main(void) {
    ESP_ERROR_CHECK(bmi_init());
    softreset();
    chipid();
    initialization();
    check_initialization();

    // Intento de Anymotion
    //set_anymo2(0xAA);
    //set_anymo1(0x05, 0, 0, 1);

    // Selecting power mode-> Suspend:0, Low:1, Normal:2, Performance:3
    uint8_t pwr_mode = 3;
    // Setting Sample rate and sensibility config
    uint8_t acc_odr = 7;    // From 1 to 12 (5 to 12 in normal/perf mode) (1 to 10 in low)
    uint8_t gyr_odr = 6;    // From 6 to 13 (6 to 8 in low mode)
    uint8_t acc_sens = 2;   // From 0 to 3
    uint8_t gyr_sens = 0;   // From 0 to 4
    
    set_acc_sensibility(acc_sens);      // reg 0x41
    set_gyr_sensibility(gyr_sens, 0);   // reg 0x43
    set_pwrmode_and_ODRs(pwr_mode, acc_odr, gyr_odr);

    internal_status();    
    printf("Comienza lectura\n\n");
    lectura(acc_sens, gyr_sens);
    
}