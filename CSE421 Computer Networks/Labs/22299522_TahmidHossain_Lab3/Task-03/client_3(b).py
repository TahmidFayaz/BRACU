

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
    client_recv = client.recv(2048).decode(format)
    print(client_recv)



while True:
    in_msg = input("Enter some text with vowels: ")
    if in_msg == "Done":
        message_to_be_sent("off")
        break
    else:
        message_to_be_sent(in_msg)