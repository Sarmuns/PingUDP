<div style="bold">
You need to implement the following client program.
</div>


The client should send 10 pings to the server. Because UDP is an unreliable protocol, a packet sent from the client to the server may be lost in the network, or vice versa. For this reason, the client cannot wait indefinitely for a reply to a ping message. You should get the client wait up to one second for a reply; if no reply is received within one second, your client program should assume that the packet was lost during transmission across the network. 

You will need to look up the Python documentation to find out how to set the timeout value on a datagram socket. 


Specifically, your client program should :

- [ ] send the ping message using UDP (Note: Unlike TCP, you do not need to establish a connection first, since UDP is a connectionless protocol.)
  

- [ ] print the response message from server, if any
  

- [ ]  calculate and print the round trip time (RTT), in seconds, of each packet, if server responses 
  

- [ ] otherwise, print “Request timed out”
  
  

During development, you should run the UDPPingerServer.py on your machine, and test your client by sending packets to localhost (or, 127.0.0.1). After you have fully debugged your code, you should see how your application communicates across the network with the ping server and ping client **running on different machines**.