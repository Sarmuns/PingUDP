== Livro Kurose ==

**You need to implement the following client program.**


The client should send 10 pings to the server. Because UDP is an unreliable protocol, a packet sent from the client to the server may be lost in the network, or vice versa. For this reason, the client cannot wait indefinitely for a reply to a ping message. You should get the client wait up to one second for a reply; if no reply is received within one second, your client program should assume that the packet was lost during transmission across the network. 

You will need to look up the Python documentation to find out how to set the timeout value on a datagram socket. 


Specifically, your client program should :

1. send the ping message using UDP (Note: Unlike TCP, you do not need to establish a connection first, since UDP is a connectionless protocol.)
  
2. print the response message from server, if any
  
3. calculate and print the round trip time (RTT), in seconds, of each packet, if server responses
  
4. otherwise, print “Request timed out”
  
  

During development, you should run the UDPPingerServer.py on your machine, and test your client by sending packets to localhost (or, 127.0.0.1). After you have fully debugged your code, you should see how your application communicates across the network with the ping server and ping client **running on different machines**.


###Usando o server e o client em máquinas diferentes :sparkles:

Você vai precisar ultilizar de [port forwarding]([Sabe o que é port forwarding e qual a sua utilização?](https://pplware.sapo.pt/tutoriais/networking/sabe-port-forwarding-qual-utilizacao/))

- No código do client trocar o IP e Porta do adress
  

```python
addr = ("127.0.0.1", 12000)
```

> IP: 127.0.0.1 é um IP local
> 
> Porta: 12000, só uma porta teoricamente livre
> 
> Substituir o IP local pelo IP público de quem está com o **server**
> 
> Substituir a porta 12000 pela porta ultilizada no processo de port forwarding
> 
> No processo de port forwarding apontar a porta para o IP local de quem está com o **server**
