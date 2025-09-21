
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

            if message == "Disconnect":
                Connected = False
                print("Terminating connection with", address)
                connection.send("The session is terminated".encode(format))
                print("\n")
            else:
                # Vowel Logic
                vowels = "aeiou"
                vowel_count = sum(1 for char in message.lower() if char in vowels)

                response = ""
                if vowel_count == 0:
                    response = "Not enough vowels"
                elif 1 <= vowel_count <= 2:
                    response = "Enough vowels I guess"
                else:
                    response = "Too many vowels"

                print(f"Received message: '{message}'")
                print(f"Vowel count: {vowel_count}")
                print(f"Sending response: '{response}'")

                connection.send(response.encode(format))
                print("\n")

    connection.close()