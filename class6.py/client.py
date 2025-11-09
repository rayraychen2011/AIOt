import socket

client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 4444))

while True:
    msg = input("Enter message to send to server (type 'bye' to quit): ")
    client_socket.send(msg.encode("utf-8"))

    reply = client_socket.recv(128).decode("utf-8")

    if reply == "quit":
        print("Server requested to close the connection.")
        client_socket.close()
        break
    print(reply)
