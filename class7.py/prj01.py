import paho.mqtt.client as mqtt


def on_connect(client, userdata, connect_flags, reason_code, properties):
    print(f"連線結果:{reason_code}")
    client.subscribe("ha")


def on_message(client, userdata, msg):
    print(f"訂閱主題:{msg.topic},收到訊息:{msg.payload.decode('utf-8')}")


client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect

client.on_message = on_message

client.username_pw_set("singular", "Singular#1234")

client.connect("mqtt.singularinnovation-ai.com", 1883, 60)

client.loop_forever()
