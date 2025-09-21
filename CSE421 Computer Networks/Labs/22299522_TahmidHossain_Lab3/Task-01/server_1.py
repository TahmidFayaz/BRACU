

import socket


server_port = 8080
format = "utf-8"
buffer_for_message_length = 16

hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)

address = (host_ip, server_port)

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)

server.listen()
print("The server is listening.....")

while True:
    connection ,address = server.accept()
    print("Connected to:", address)
    Connected= True

    while Connected:
        message_length = connection.recv(buffer_for_message_length).decode(format)
        print("Upcoming message length:", message_length)

        if message_length :
            message_length = int(message_length)
            message = connection.recv(message_length).decode(format)

            if message == "Disconnect":
                Connected = False
                print("Terminating connection with",address)
                connection.send("The session is terminated".encode(format))
                print("\n")
            else:
                print(message)
                connection.send("The server has recieved the message".encode(format))
                print("\n")



    connection.close()
