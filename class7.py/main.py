from umqtt.simple import MQTTClient
import sys
import time
import mcu


def on_message(topic, msg):
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"訂閱主題:{topic},收到訊息:{msg}")


wi = mcu.WiFi()
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
    print("連接MQTT伺服器成功")

mqClient0.set_callback(on_message)
mqClient0.subscribe("ha")


while True:
    mqClient0.check_msg()
    mqClient0.ping()
    time.sleep(0, 1)
