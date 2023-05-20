
void normalpowermode(void)
{
    //PWR_CTRL: disable auxiliary sensor, gryo acc temp on
    //200Hz en datos acc, filter: performance optimized, acc_range +/-8g (1g = 9.80665 m/s2, alcance max: 78.4532 m/s2, 16 bit= 65536 => 1bit = 78.4532/32768 m/s2)
    //200Hz en datos gyro, noise filter: performance optimized, filter: performance opt., gyr_range +/-2000dps, 16.4LSB/dps (1 bit= 2000/32768 dps, 34.90659/32768 rad/s)
    uint8_t reg_pwr_ctrl=0x7D, val_pwr_ctrl=0x0E;
    uint8_t reg_acc_conf=0x40, val_acc_conf=0xA9;
    uint8_t reg_gyr_conf=0x42, val_gyr_conf=0xA9; 
    uint8_t reg_pwr_conf=0x7C, val_pwr_conf=0x02;
    
    bmi_write(I2C_NUM_0, &reg_pwr_ctrl, &val_pwr_ctrl,1);
    bmi_write(I2C_NUM_0, &reg_acc_conf, &val_acc_conf,1);
    bmi_write(I2C_NUM_0, &reg_gyr_conf, &val_gyr_conf,1);
    bmi_write(I2C_NUM_0, &reg_pwr_conf, &val_pwr_conf,1);

    vTaskDelay(1000 /portTICK_RATE_MS);   

    ESP_LOGD("POWER", "Normal power mode: activated. \n\n");
}