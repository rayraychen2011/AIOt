from machine import Pin, I2C, ADC
import dht
import time
import mcu
import ssd1306
import json

msg_jason = {}
adc = ADC(0)
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
    light_value = adc.read()
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    oled.fill(0)  # 清除顯示
    oled.text(f"Humidity: {hum:02d}", 0, 0)  # 顯示文字
    oled.text(f"TEMPERATURE: {temp:02d} C", 0, 8)
    oled.text(f"LIGHT: {light_value}", 0, 16)
    oled.show()  # 更新顯示
    msg_jason["HUMIDITY"] = hum
    msg_jason["TEMPERATURE"] = temp
    msg_jason["LIGHT"] = light_value
    msg = json.dumps(msg_jason)
    mqtt.publish(topic="RAY", msg=msg)
    time.sleep(10)
