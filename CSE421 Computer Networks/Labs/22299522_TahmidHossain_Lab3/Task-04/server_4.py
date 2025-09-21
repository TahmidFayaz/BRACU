
import socket


server_port = 8080
format = "utf-8"
buffer_for_message_length = 16

hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)

address = (host_ip, server_port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)

server.listen()
print("The server is listening.....")

while True:
    connection, address = server.accept()
    print("Connected to:", address)
    Connected = True

    while Connected:
        message_length = connection.recv(buffer_for_message_length).decode(format)
        print("Upcoming message length:", message_length)

        if message_length:
            message_length = int(message_length)
            message = connection.recv(message_length).decode(format)

            if message == "off":
                Connected = False
                print("Terminating connection with", address)
                connection.send("Bye . ".encode(format))
                print("\n")
            else:
                hours = int(message)
                money = 0
                if hours <= 40:
                    money = hours * 200
                else:
                    money = ((hours - 40) * 300) + 8000

                response = str(float(money)) + "tk"
                connection.send(response.encode(format))
                print("\n")

    connection.close()
