from socket import *

serverName = "localhost"
severPort = 120000
clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM)
message = raw_input("input lowercase stuff")
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
raw_input("")
clientSocket.close()