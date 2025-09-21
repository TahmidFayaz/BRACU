
import socket

server_port =8080
format = 'utf-8'
buffer_for_message_length =16

hostname= socket.gethostname()
host_ip =socket.gethostbyname(hostname)

adddress = (host_ip, server_port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(adddress)


def message_to_be_sent(message):
    message = message.encode(format)
    
    message_length =str(len(message))
    message_length = message_length.encode(format)

    padding = b' ' * (buffer_for_message_length - len(message_length))

    message_length = padding + message_length


    client.send(message_length)
    client.send(message)


    print(client.recv(2048).decode(format))



message_to_be_sent(f"Hostname: {hostname} and IP: {host_ip}")
message_to_be_sent(f"Disconnect")






