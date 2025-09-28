######################### 匯入模組 #########################
# 使用機板相關的硬體介面：Pin, ADC, PWM
from machine import Pin, ADC, PWM

# sleep 用於讓迴圈有間隔
from time import sleep

# 匯入同專案中的 mcu 模組（封裝了 GPIO 腳位命名）
import mcu

######################### 函式與類別定義 #########################
# (此檔案為簡單範例，沒有額外函式或類別定義)

######################### 宣告與設定 #########################
# PWM 頻率（Hz），用來控制 LED 閃爍/調光的頻率
frequency = 1000
# 初始佔空比（0 = 關閉，最大值視板子 ADC/PWM 規格而定）
duty_cycle = 0

# 取得板子上的 GPIO 腳位定義（由 mcu.gpio() 提供）
gpio = mcu.gpio()

# 光敏電阻（或其他類比光感測器）接到 ADC(0)
# read() 會回傳一個整數值，代表類比量測結果
light_sensor = ADC(0)

# 將 RGB 三色 LED 的腳位設定為 PWM，以便透過佔空比控制亮度
# 假設 mcu.gpio() 提供 D5/D6/D7 的對應腳位物件或編號
RED = PWM(Pin(gpio.D5), freq=frequency, duty=duty_cycle)
GREEN = PWM(Pin(gpio.D6), freq=frequency, duty=duty_cycle)
BLUE = PWM(Pin(gpio.D7), freq=frequency, duty=duty_cycle)

######################### 主程式 #########################
# 連續讀取光感測器值，印出來並用來設定 RGB LED 的亮度
while True:
    # 讀取光感測器的類比值（範圍依板子 ADC 規格而定，常見為 0~1023 或 0~4095）
    duty_cycle = light_sensor.read()
    # 印出感測值，方便偵錯或觀察
    print(duty_cycle)
    # 每次讀取之間暫停 0.5 秒，避免印出過快或讀取頻率過高
    sleep(0.5)

    # 將讀到的感測值直接當作 PWM 佔空比，控制 LED 亮度
    # 注意：若 ADC 的量測範圍與 PWM 的 duty 範圍不同，
    # 可能需要進行比例縮放（例如將 ADC 0~4095 映射到 0~1023）
    RED.duty(duty_cycle)
    GREEN.duty(duty_cycle)
    BLUE.duty(duty_cycle)
