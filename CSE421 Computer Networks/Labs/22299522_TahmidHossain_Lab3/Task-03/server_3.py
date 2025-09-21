
import socket
import threading

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


def handl_server(connection, address):
    print("Connected to:", address)
    Connected = True

    while Connected:
        message_length = connection.recv(buffer_for_message_length).decode(format)
        print("Length", message_length)

        if message_length:
            message_length = int(message_length)
            message = connection.recv(message_length).decode(format)

            if message == "off": 
                connection.send("Bye . ".encode(format))
                print("Terminate conncetion with", address)
                Connected = False
            else:
                vowels = ["a","e","i","o","u","A","E","I","O","U"]
                count = 0
                for x in message:
                    if x in vowels:
                        count += 1
                if count == 0:
                    connection.send("Not enough vowels".encode(format))
                elif count <= 2:
                    connection.send("Enough vowels I guess".encode(format))
                else:
                    connection.send("Too many vowels".encode(format))

    connection.close()


while True:
    connection, address = server.accept()
    thread = threading.Thread(target=handl_server, args=(connection, address))
    thread.start()
