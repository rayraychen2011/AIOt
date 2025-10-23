#########################匯入模組#########################
import network


#########################函式與類別定義#########################

#########################宣告與設定#########################
wlan = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)
ap.active(False)
wlan.active(True)
wifi_list = wlan.scan()
print("附近的 WiFi 熱點：")
for i in range(len(wifi_list)):
    print(wifi_list[i])
wlSSID = "Singular_AI"
wlPWD = "Singular#1234"
wlan.connect(wlSSID, wlPWD)
while not wlan.isconnected():
    pass
print("已連接到 WiFi 網路", wlan.ifconfig())


#########################主程式#########################
