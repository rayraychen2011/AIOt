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

        if not self.sta.active():
            self.sta.active.connect(ssid, password)
            while not self.sta.isconnected():
                pass
        self.ip = self.sta.ifconfig()[0]
        print("已連接到 WiFi 網路", self.sta.ifconfig())
        return True
