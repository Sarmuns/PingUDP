# We will need the following module to generate randomized lost packets
import random
from socket import *

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10) 

    # Receive the client packet along with the address it is coming from 
    message, address = serverSocket.recvfrom(1024)

    if rand >= 4: # if randomly this is lower than four then it won't do anything
        print(message.decode("utf-8"))
        serverSocket.sendto(b"pong", address)