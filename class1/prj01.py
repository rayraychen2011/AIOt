###########################匯入模組################################
from machine import Pin, PWM
from time import sleep

##############################宣告與設定##################################
frequency = 50  # 頻率
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)
#################################主程式###############################
while True:
    led.duty(0)
    sleep(2)
    led.duty(512)
    sleep(2)
    led.duty(1023)
    sleep(2)
