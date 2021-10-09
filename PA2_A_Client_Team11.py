# Team #11 Members: Gabrielle Lake, Amy Wall, Erik Gallardo, & Noah Ahmed
import time
from socket import *

serverName = "localhost"
serverPort = 12000

minRTT = 100
maxRTT = 0
totalRTT = 0
packetLoss = 0
packetReceived = 0
hasInitialValue = False
allRTTTimes = []

for i in range(1, 11, 1):
    print()
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    message = "Ping" + str(i)
    startTime = (time.time()) * 1000
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    # modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        endTime = (time.time()) * 1000
        elapsedTime = (endTime - startTime)
        allRTTTimes.append(elapsedTime)
        if i == 1 or not hasInitialValue:
            estimatedRTT = elapsedTime
            devRTT = (estimatedRTT / 2)
            hasInitialValue = True
        else:
            estimatedRTT = (.875 * estimatedRTT) + (.125 * elapsedTime)
            devRTT = (0.75 * devRTT) + (0.25 * abs(elapsedTime - estimatedRTT))
        packetReceived += 1
        print("Mesg sent:", modifiedMessage.decode())
        print("Mesg rcvd:", modifiedMessage.decode().upper())
        print("Pong", i, "RTT: ", elapsedTime, "ms")
        print()
    except:
        packetLoss += 1
        print("Mesg sent:", message)
        print("No Message Rcvd")
        print("Ping", i, "Request Timed out")
        print()
print("Min RTT: ", min(allRTTTimes), "ms")
print("Max RTT: ", max(allRTTTimes), "ms")
print("Avg RTT: ", sum(allRTTTimes) / packetReceived, "ms")
print("Packet Loss: ", (packetLoss * 10.0))
print("Estimated RTT:", estimatedRTT, "ms")
print("Dev RTT: ", devRTT, "ms")
print("Timeout Interval: ", (estimatedRTT + (4 * devRTT)), "ms")
