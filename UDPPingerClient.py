# UDP Pinger

from socket import *
import time
import select

TIMEOUT_SECONDS = 2
BUFFER_SIZE = 1024

serverName = 'localhost'
serverPort = 12000


#create socket
# AF_INET -- refers to IP Addr
try:
    clientSocket = socket(AF_INET, SOCK_DGRAM)
except OSError as err:
    print(err)
    clientSocket.close()
    clientSocket = None
    sys.exit(1)

message = "ping"
isTimeout = False
#clientSocket.connect((serverName, serverPort))
clientSocket.settimeout(TIMEOUT_SECONDS)
#clientSocket.setblocking(True)
for x in range(0, 10):
	start = time.time()
	clientSocket.sendto(message.encode(), (serverName, serverPort))
	#sets timeout time to one second	
	#clientSocket.settimeout(TIMEOUT_SECONDS)
	try: 
		modMessage, serverAddr = clientSocket.recvfrom(BUFFER_SIZE)
	except OSError as err:
		print("Timeout exception occurred, message lost.")
		isTimeout = True
	stop = time.time()
	if (isTimeout == False):
		print(modMessage.decode())
		print(str((stop - start)*1000 + "milliseconds"))
	
clientSocket.close()



