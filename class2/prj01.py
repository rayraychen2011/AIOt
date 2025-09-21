##################################匯入模組##################################
from machine import Pin
from time import sleep
import mcu

##################################宣告與設定##################################
gpio = mcu.gpio()
Red = Pin(gpio.D5, Pin.OUT)
Green = Pin(gpio.D6, Pin.OUT)
Blue = Pin(gpio.D7, Pin.OUT)

Red.value(0)
Green.value(0)
Blue.value(0)

###################################主程式##################################
while True:
    Red.value(1)
    sleep(2)
    Red.value(0)
    Green.value(1)
    sleep(2)
    Green.value(0)
