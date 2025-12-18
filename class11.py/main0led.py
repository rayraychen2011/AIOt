######################匯入模組######################
import mcu
from machine import Pin, I2C
import ssd1306

######################宣告與設定######################
gpio = mcu.gpio()
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
######################主程式######################
oled.fill(0)  # 清除顯示
oled.text("Hello", 0, 0)  # 顯示文字
oled.text("world", 0, 27)
oled.show()  # 更新顯示
