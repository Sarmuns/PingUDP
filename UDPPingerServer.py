# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
import time
from socket import *
# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('127.0.0.1', 12000))
while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10) 
    # Receive the client packet along with the address it is coming from 
    message, address = serverSocket.recvfrom(1024)
    # Capitalize the message from the client
    if rand < 4:
        print("kek")
        continue
    # Otherwise, the server responds 

    print(message.decode("utf-8"))
    serverSocket.sendto(b"pong", address)