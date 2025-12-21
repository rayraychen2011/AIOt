import sys
from machine import Pin, PWM
from umqtt.simple import MQTTClient


class gpio:
    def __init__(self):
        self._D0 = 16
        self._D1 = 5
        self._D2 = 4
        self._D3 = 0
        self._D4 = 2
        self._D5 = 14
        self._D6 = 12
        self._D7 = 13
        self._D8 = 15
        self._SD3 = 10
        self._SD2 = 9

    @property
    def D0(self):
        return self._D0

    @property
    def D1(self):
        return self._D1

    @property
    def D2(self):
        return self._D2

    @property
    def D3(self):
        return self._D3

    @property
    def D4(self):
        return self._D4

    @property
    def D5(self):
        return self._D5

    @property
    def D6(self):
        return self._D6

    @property
    def D7(self):
        return self._D7

    @property
    def D8(self):
        return self._D8

    @property
    def SD3(self):
        return self._SD3

    @property
    def SD2(self):
        return self._SD2


import network


class wifi:
    def __init__(self, ssid=None, password=None):
        """
        初始化 WiFi 模組
        ssid: WiFi 名稱
        password: WiFi 密碼
        """
        self.ssid = ssid
        self.password = password
        self.ip = None
        self.sta_active = False
        self.ap_active = False
        self.ap = network.WLAN(network.AP_IF)
        self.sta = network.WLAN(network.STA_IF)

    def setup(self, ap_active=False, sta_active=False):
        """
        設定 WiFi 模組
        ap_active: 是否啟用熱點模式
        sta_active: 是否啟用站台模式

        使用方法:
        wi.setup(ap_active=True|False, sta_active=True|False)

        """
        self.ap_active = ap_active
        self.sta_active = sta_active
        self.ap.active(ap_active)
        self.sta.active(sta_active)

    def scan(self):
        """
        掃描附近的 WiFi 熱點
        回傳值: WiFi 熱點列表
        使用方法:
        wi.scan()
        """
        if self.sta_active:
            wifi_list = self.sta.scan()
            print("附近的 WiFi 熱點：")
            for i in range(len(wifi_list)):
                print(wifi_list[i])
        else:
            print("請先啟用站台模式")

    def connect(self, ssid=None, password=None) -> bool:
        """
        連接到指定的 WiFi 熱點
        ssid: WiFi 名稱
        password: WiFi 密碼
        回傳值: 是否成功連接
        使用方法:
        wi.connect(ssid, password)
        """
        ssid = ssid if ssid is not None else self.ssid
        password = password if password is not None else self.password

        if not self.sta_active:
            print("請先啟用站台模式")
            return False

        if ssid is None or password is None:
            print("請提供 WiFi 名稱和密碼")
            return False

        # 啟用站台介面 (如果尚未啟用)
        if not self.sta.active():
            # 在 MicroPython 中，active() 需要一個布林參數來啟用介面
            self.sta.active(True)

        # 使用正確的 API connect
        try:
            self.sta.connect(ssid, password)
        except Exception:
            # 在某些環境下 connect 會拋例外或不可用，回傳 False
            print("WiFi connect 呼叫失敗")
            return False

        # 等待連線成功
        while not self.sta.isconnected():
            pass
        self.ip = self.sta.ifconfig()[0]
        print("已連接到 WiFi 網路", self.sta.ifconfig())
        return True


class LED:
    def __init__(self, r_pin, g_pin, b_pin, pwm: bool = False):
        """
        LED類別用於控制RGB LED燈

        屬性:
            RED(Pin): 紅色LED
            GREEN(Pin): 綠色LED
            BLUE(Pin): 藍色LED

        方法:
            _init_(r_pin, g_pin, b_pin, pwm=False): 初始化LED物件
            當pwm=True時，使用PWM控制LED
            當pwm=False時，使用PWM控制LED
            RED.value(value): 設定紅色LED的亮度
            GREEN.value(value): 設定綠色LED的亮度
            BLUE.value(value): 設定藍色LED的亮度
            RED.duty(duty): 設定紅色LED的PWM佔空比
            GREEN.duty(duty): 設定綠色LED的PWM佔空比
            BLUE.duty(duty): 設定藍色LED的PWM佔空比
        """
        self.pwm = pwm
        if pwm == False:
            self.RED = Pin(r_pin, Pin.OUT)
            self.GREEN = Pin(g_pin, Pin.OUT)
            self.BLUE = Pin(b_pin, Pin.OUT)
        else:
            frequency = 1000  # 設定PWM頻率為1kHz
            duty_Cycle = 0
            self.RED = PWM(Pin(r_pin), freq=frequency, duty=duty_Cycle)
            self.GREEN = PWM(Pin(g_pin), freq=frequency, duty=duty_Cycle)
            self.BLUE = PWM(Pin(b_pin), freq=frequency, duty=duty_Cycle)

    def LED_open(self, RED_value, GREEN_value, BLUE_value):
        """
        LED 開啟方法
        LED_open(RED_value, GREEN_value, BLUE_value)
        例如:
        led=LED(r_pin=5, g_pin=4, b_pin=0, pwm=False)
        led.LED_open(1,0,0) # 紅色

        led=LED(r_pin=5, g_pin=4, b_pin=0, pwm=True)
        led.LED_open(512,0,0) # 紅色
        """
        if self.pwm == False:
            self.RED.value(RED_value)
            self.GREEN.value(GREEN_value)
            self.BLUE.value(BLUE_value)
        else:
            self.RED.duty(RED_value)
            self.GREEN.duty(GREEN_value)
            self.BLUE.duty(BLUE_value)


class MQTT:
    def __init__(self, client_id, server, user, password, keepalive):
        self.client = MQTTClient(
            client_id, server, user=user, password=password, keepalive=keepalive
        )

    def connect(self):
        try:
            self.client.connect()
        except:
            sys.exit()
        finally:
            print("connected to %s" % self.client.server)

    def subscribe(self, topic: str, callback: function):
        self.client.set_callback(callback)
        self.client.subscribe(topic)

    def check_msg(self):
        self.client.check_msg()
        self.client.ping()

    def publish(self, topic: str, msg: str):
        topic = topic.encode("utf-8")
        msg = msg.encode("utf-8")
        self.client.publish(topic, msg)
