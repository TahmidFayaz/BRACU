
import socket

server_port = 8080
format = 'utf-8'
buffer_for_message_length = 16

hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)

adddress = (host_ip, server_port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(adddress)


def message_to_be_sent(message):
    message = message.encode(format)

    message_length = str(len(message)).encode(format)
    message_length += b' ' * (buffer_for_message_length - len(message_length))


    client.send(message_length)
    client.send(message)


    print(client.recv(2048).decode(format))


while True:
    msgg = input("Enter how many hours a person works: ")
    message_to_be_sent(msgg)