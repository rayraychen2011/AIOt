from umqtt.simple import MQTTClient
import sys
import time
import mcu
from machine import ADC


def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"subscribe topic:{topic}, msg:{msg}")
    m = msg


wi = mcu.wifi()
wi.setup(ap_active=False, sta_active=True)
if wi.connect("Singular_AI", "Singular#1234"):
    print(f"IP={wi.ip}")

mq_server = "mqtt.singularinnovation-ai.com"
mqttClientId = "Ray"
mqtt_username = "singular"
mqtt_password = "Singular#1234"
mqClient0 = MQTTClient(
    mqttClientId, mq_server, user=mqtt_username, password=mqtt_password, keepalive=30
)

try:
    mqClient0.connect()
except:
    sys.exit()
finally:
    print("connected to %s" % mq_server)

mqClient0.set_callback(on_message)
mqClient0.subscribe("Ray")

gpio = mcu.gpio()
LED = mcu.LED(gpio.D5, gpio.D6, gpio.D7, pwm=False)
LED.LED_open(0, 0, 0)
light_sensor = ADC(0)
m = ""

while True:
    mqClient0.check_msg()
    mqClient0.ping()
    light_sensor_value = light_sensor.read()
    if m == "ON":
        LED.LED_open(1, 1, 1)
    elif m == "OFF":
        LED.LED_open(0, 0, 0)
    elif m == "AUTO":
        if light_sensor_value > 700:
            LED.LED_open(1, 1, 1)
        else:
            LED.LED_open(0, 0, 0)
    time.sleep(0.1)
