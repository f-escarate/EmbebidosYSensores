idf_component_register(SRCS "bme68x_lib.c" "main.c" "BMI270.c" "bme68x/bme68x.c"
                    INCLUDE_DIRS "." "include" "bme68x"
                    REQUIRES esp_timer driver)