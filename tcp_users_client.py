import socket

# создаем TCP-клиент
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# подключаемся к серверу
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# отправляем сообщение серверу
message = "Нормально!"
client_socket.send(message.encode())

# получаем ответ от сервера
print(client_socket.recv(1024).decode())

client_socket.close()