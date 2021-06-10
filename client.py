from socket import *
import time

for pings in range(10):
    # configura o socket para UDP e para ter um timeout de 1s
    udp_client_socket = socket(AF_INET, SOCK_DGRAM)
    udp_client_socket.settimeout(1)

    client_msg = f'ping {pings+1}' # mensagem que o client vai enviar para o server através de udp
    bytesToSend = str.encode(client_msg) # converte a string para bytes (coisa de python)

    addr = ("127.0.0.1", 12000)
    bufferSize = 1024

    start = time.time() # registra o momento antes de enviar o ping
    udp_client_socket.sendto(bytesToSend, addr) # efetivamente excuta o ping
    try:
        data, adress = udp_client_socket.recvfrom(bufferSize)
        end = time.time() # registra o momento após receber a resposta do ping
        elapsed = end - start

        print(f'ping_n: {pings} | data: {data.decode("utf-8")} | RTT: {elapsed}') # apresenta o resultado de um ping

    except:
        print('REQUEST TIMED OUT')
