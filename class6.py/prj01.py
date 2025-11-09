######################### 匯入模組 #########################
import socket

######################### 伺服器設定 #########################
# HOST: 監聽的主機位址，使用 localhost（僅本機）
# PORT: 監聽的埠號
HOST = "localhost"
PORT = 4444

# 建立一個 TCP socket（預設為 AF_INET, SOCK_STREAM）
server_socket = socket.socket()

# bind() 將 socket 綁到指定的 (HOST, PORT)
server_socket.bind((HOST, PORT))

# listen() 開始監聽連線，參數為允許排隊的最大連線數
server_socket.listen(5)
print(f"server: {HOST} port: {PORT} start")

# accept() 阻塞直到有 client 連線，返回 (client_socket, address)
client, addr = server_socket.accept()
print(f"client address:{addr[0]} port:{addr[1]} connected")

######################### 接收與回應邏輯 #########################
# 進入主迴圈，不斷接收來自 client 的訊息並回應
while True:
    # recv(28) 會接收最多 28 bytes 的資料；實務上可用更大的緩衝區或協議來處理
    # decode("utf-8") 將位元組轉為字串
    msg = client.recv(28).decode("utf-8")
    # 若 client 主動關閉連線，recv() 可能會回傳空字串，這裡可檢查並跳出
    if not msg:
        print("client closed connection")
        break

    print(f"receive message:{msg}")
    reply = ""

    # 根據接收到的訊息回傳不同回覆
    if msg == "Hello Server":
        # 當收到 Hello Server 時回傳 Hello Client
        reply = "Hello Client"
        client.send(reply.encode("utf-8"))
    elif msg == "bye":
        # 當收到 bye 時告知 client 要結束（傳回 quit）並跳出迴圈結束連線
        client.send(b"quit")
        break
    else:
        # 其他不認識的訊息一律回傳 what?
        reply = "what?"
        client.send(reply.encode("utf-8"))

######################### 程式結束清理 #########################
client.close()
server_socket.close()
# 關閉 client socket 與 server socket，釋放資源
