
import socket

server_port = 8080
format = 'utf-8'
buffer_for_message_length = 16

hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)

adddress = (host_ip, server_port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(adddress)
except socket.error as e:
    print(f"Connection failed: {e}")
    exit()

print(f"Connected to {adddress}")
print("Type 'Done' to close the connection.")

def message_to_be_sent(message):
    message_encoded = message.encode(format)
    
    # Prepend the padded message length
    message_length = str(len(message_encoded)).encode(format)
    padding = b' ' * (buffer_for_message_length - len(message_length))
    message_length = padding + message_length

    client.send(message_length)
    client.send(message_encoded)

    # Receive and print the server's response
    print(client.recv(2048).decode(format))

connected = True
while connected:
    input_message = input("Please enter your message\n")

    if input_message == "Done":
        connected = False
        message_to_be_sent("Disconnect")
    else:
        message_to_be_sent(input_message)

client.close()