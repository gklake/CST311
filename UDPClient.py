from socket import *

serverName = "10.0.0.1"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Input lowercase sentence:")

clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())


# Second Attempt
# serverName = "localhost"
# serverPort = 12000
#
# clientSocket = socket(AF_INET, SOCK_DGRAM)
# message = input("Input lowercase sentence:")
#
# clientSocket.sendto(message.encode(), (serverName, serverPort))
#
# modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
#
# print(modifiedMessage.decode())
