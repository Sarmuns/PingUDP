from socket import *
import time

serverAddressPort   = ("127.0.0.1", 12000)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket(AF_INET, SOCK_DGRAM)
UDPClientSocket.settimeout(1)

for n in range(10):
    msgFromClient = f'ping {n+1}'
    bytesToSend = str.encode(msgFromClient)

    try:
        t1 = time.time()
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        response, adress = UDPClientSocket.recvfrom(bufferSize)
        t2 = time.time()
        tim = str(t2-t1)
        print(response.decode("utf-8"), "RTT:" + tim)

    except:
        print("Timeout raised and caught.")

      
