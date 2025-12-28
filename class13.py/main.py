from machine import Pin, I2C
import dht
import time
import mcu
import ssd1306


gpio = mcu.gpio()
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")
mqtt = mcu.MQTT(
    "Ray", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234", keepalive=30
)
mqtt.connect()
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

d = dht.DHT11(Pin(gpio.D0, Pin.IN))

while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    oled.fill(0)  # 清除顯示
    oled.text(f"Humidity: {hum:02d}", 0, 0)  # 顯示文字
    oled.text(f"TEMPERATURE: {temp:02d} C", 0, 8)
    oled.show()  # 更新顯示
    msg = f"HUMIDITY:{hum:02d},TEMPERATURE:{temp:02d}C"
    mqtt.publish(topic="RAY", msg=msg)
    time.sleep(10)
