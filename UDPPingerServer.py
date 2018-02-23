# UDP Pinger

# Must have this server running before you can run the UDP Pinger Client code

import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('localhost', 12000)) #localhost can be replaced by I.P address
print("Server is running")
while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    #print(message.decode())
    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
    # Otherwise, the server responds
    message = "pong"
    serverSocket.sendto(message.encode(), address)
