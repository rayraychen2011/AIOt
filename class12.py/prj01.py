import time
import mcu
from machine import ADC

wi = mcu.wifi()
wi.setup(ap_active=False, sta_active=True)
if wi.connect("Singular_AI", "Singular#1234"):
    print(f"IP={wi.ip}")

mqtt = mcu.MQTT(
    "Ray", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234", keepalive=30
)
light_sensor = ADC(0)

mqtt.connect()
while True:
    msg = f"Light sensor value:{ADC(0).read()}"
    print(msg)
    mqtt.publish(topic="RAY", msg=msg)
    time.sleep(5)
