import mcu
from machine import Pin, I2C
import ssd1306
import time


gpio = mcu.gpio()
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"subscribe topic:{topic}, msg:{msg}")
    m = msg


def display_message(init_y, msg):
    """在OLED上顯示多行訊息.自動換行
    每個字像素寬度:8, 高度:8 oled寬度:128, 高度:64
    參數:
        init_y: 起始y座標
        msg: 要顯示的訊息
    迴圈變數m從init_y開始到msg長度,每次增加16個字元
    取得當前型的字串為line=msg[m:m+16]
    y座標為y_position=(m//16)*8
    透過oled.text(line,0,y_position)顯示文字"""
    max_chars_per_line = 16
    for m in range(0, len(msg), max_chars_per_line):
        line = msg[m : m + max_chars_per_line]
        y_position = (m // max_chars_per_line) * 8
        oled.text(line, 0, y_position + init_y)


wi = mcu.wifi()
wi.setup(ap_active=False, sta_active=True)
if wi.connect("Singular_AI", "Singular#1234"):
    print(f"IP={wi.ip}")

mq_server = "mqtt.singularinnovation-ai.com"
mqttClientId = "Ray"
mqtt_username = "singular"
mqtt_password = "Singular#1234"
mqtt = mcu.MQTT(mqttClientId, mq_server, mqtt_username, mqtt_password, keepalive=30)
mqtt.connect()
mqtt.subscribe(topic="Ray", callback=on_message)
m = "no message"

while True:
    mqtt.check_msg()
    oled.fill(0)  # 清除顯示
    oled.text(f"{wi.ip}", 0, 0)  # 顯示文字
    oled.text("topic:Ray", 0, 8)
    display_message(16, f"msg:{m}")
    oled.show()  # 更新顯示
    time.sleep(0.1)
