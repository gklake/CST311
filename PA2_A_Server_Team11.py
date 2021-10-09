# Server.py
# We will need the following module to generate randomized lost packets
#Team #11 Members: Gabrielle Lake, Amy Wall, Erik Gallardo, & Noah Ahmed

import random
from socket import *



# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

print("Waiting for client...")
print()
i = 1

while i < 11:
    print("PING", i, "Received")
    # Generate random number5 in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    print("Mesg rcvd:", message.decode())
    i += 1
    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        print()
        continue
    # Otherwise, the server responds
    modifiedMessage = message.decode().upper()
    print("Mesg sent:", modifiedMessage)
    print()

    serverSocket.sendto(message, address)
