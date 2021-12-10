# Team 11 Members: Gabrielle Lake, Amy Wall, Erik Gallardo-Cruz & Noah Ahmed

# Answer to Question 11:
"""
The Server program needs to be able to handle simultaneous connections from two different
clients so it can share the data between the threads. Multithreading lets both clients communicate with the server at
the same time. Since a new thread will be created for each client that is connected, each client can run on their own
and won't have to wait until the other(current) client has closed their connection.
"""

from socket import *
import threading

global clientName, rcvdMsgs, threads, clientDict, threadCount
clientDict = {}  # Storing client's letter as the key, and the msg as the value
clientName = {}  # Storing client's letter as the key, and the socket as the value
rcvdMsgs = []  # Storing all messages that are received
totalThreads = []  # Storing the threads that are created
threadCount = 0  # Keeping track of the number of threads


# Function used to run the thread
def gettingClientMessage(clientSocket, addr):
    # Initializing server's message & client's letter
    serverMsg = ""
    clientLetter = ""

    # If the threadCount is 1, then call the client X
    if threadCount == 1:
        serverMsg = 'From Server: Client X Connected'
        clientLetter = "X"
        print("Accepted first connection, calling it client", clientLetter)

    # If the threadCount is 2, then call the client Y
    if threadCount == 2:
        serverMsg = 'From Server: Client Y Connected'
        clientLetter = "Y"
        print("Accepted second connection, calling it client", clientLetter)

    # Wait until both clients are connected
    while threadCount != 2:
        continue

    # Let the client know they have been connected to the server
    clientSocket.send(serverMsg.encode())

    # Store the clientLetter & the socket
    clientName[clientLetter] = clientSocket

    # Receive the message from the client
    clientMsg = clientSocket.recv(1024)

    # Store the message in the list
    rcvdMsgs.append(clientMsg.decode())

    # Store the clientLetter & decoded message in the dictionary
    clientDict[clientLetter] = clientMsg.decode()

    # If the length of the rcvdMsgs list is 1, then the client X sent a message
    if len(rcvdMsgs) == 1:
        print('Client', clientLetter, 'sent message 1:', rcvdMsgs[0])

    # If the length of rcvdMsgs list is 2, then client Y sent a message
    if len(rcvdMsgs) == 2:
        print('Client', clientLetter, 'sent message 2:', rcvdMsgs[1])

    # If both clients have sent messages, then return the results
    if len(rcvdMsgs) == 2:
        sendToClients()


# Function to send the messages rcvd from the sever in the same order it was sent to the clients
def sendToClients():
    for (clientLetter, connectionSocket) in clientName.items():
        for key in clientName:
            if clientDict.get(key) == rcvdMsgs[0]:
                clientLetter1 = key
            if clientDict.get(key) == rcvdMsgs[1]:
                clientLetter2 = key
        message = 'From Server: ' + clientLetter1 + ' : ' \
                  + rcvdMsgs[0] + ' received before ' + clientLetter2 + ' : ' + rcvdMsgs[1]
        connectionSocket.send(message.encode())
        connectionSocket.close()


def setUpServerSocket():

    serverName = gethostbyname(gethostname())
    serverPort = 12000

    # Create a TCP socket
    # Notice the use of SOCK_STREAM for TCP packets
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))

    # Waiting for client connection
    print('The server is waiting to receive 2 connections...', "\n")
    serverSocket.listen(1)

    return serverSocket


def gettingNewConnection(serverSocket):
    # Keeping track of the number of threads
    global threadCount
    threadCount = 0

    # Loop until the thread count is equal to 2
    while threadCount != 2:
        clientSocket, addr = serverSocket.accept()

        # Incrementing thread count when a new connection is made
        threadCount += 1

        # Create another thread when another client connects
        thread = threading.Thread(target=gettingClientMessage, args=[clientSocket, addr])
        # print(threadCount)

        # adding threads to the list and starting the thread
        totalThreads.append(thread)
        thread.start()


def main():
    global clientName, rcvdMsgs

    serverSocket = setUpServerSocket()

    gettingNewConnection(serverSocket)

    print('\n')
    print('Waiting to receive messages from Client X and Client Y...', '\n')

    for t in totalThreads:
        t.join()

    print('\n')
    print("Waiting a bit for clients to close their connections.")
    print("Done.", '\n')

    serverSocket.close()


if __name__ == "__main__":
    main()
