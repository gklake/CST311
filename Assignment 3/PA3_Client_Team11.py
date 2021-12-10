# Team 11 Members: Gabrielle Lake, Amy Wall, Erik Gallardo-Cruz & Noah Ahmed
from socket import *

def createSocket(serverName, serverPort):
    # Creating a client socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    return clientSocket

def rcvMsgs(clientSocket):
    # Receiving messages from the server and printing
    serverMessage = clientSocket.recv(1024)
    print(serverMessage.decode())


def sendMsg(clientSocket):
    global sentence
    # Sending a message to the server
    sentence = input('Enter message to send to server:')
    clientSocket.send(sentence.encode())


def main():

    serverName = gethostbyname(gethostname())
    serverPort = 12000

    clientSocket = createSocket(serverName, serverPort)

    rcvMsgs(clientSocket)

    sendMsg(clientSocket)

    rcvMsgs(clientSocket)


if __name__ == "__main__":
    main()

