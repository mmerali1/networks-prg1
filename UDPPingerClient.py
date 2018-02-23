# UDP Pinger

from socket import *
import time

# Global vars
TIMEOUT_SECONDS = 1
BUFFER_SIZE = 1024


def main():
    # Set server name and server port number
    # 'localhost' -----> '127.0.0.1'
    serverName = 'localhost'
    serverPort = 12000
    try:
        # Creates client socket
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        # Connects to server
        clientSocket.connect((serverName, serverPort))
    except OSError as err:
        # Handles error if server cannot be found or connected to
        print(err)
        clientSocket.close()
        clientSocket = None
        # Ends client program if server cannot be found
        sys.exit(1)
    # Message being sent to client
    message = "ping"
    # Number of messages sent
    msgCount = 10
    # Sets timeout for client to one second
    clientSocket.settimeout(TIMEOUT_SECONDS)
    while(msgCount > 0):
        isTimeout = False
        try:
            # Starts timer
            start = time.time()
            # Sends message to client
            clientSocket.sendto(message.encode(), (serverName, serverPort))
            # Wait for client to send back message
            modMessage, serverAddr = clientSocket.recvfrom(BUFFER_SIZE)
            # Stops timer
            stop = time.time()
        except timeout as err:
            # If timeout occurs, exception handled here
            print("Timeout exception occurred, message lost.", err)
            isTimeout = True
        if (isTimeout == False):
            # Time in milliseconds
            elapseTime = (stop - start)*1000
            # Print statement for pinger
            print(modMessage.decode() + "\t " + str(elapseTime) + " milliseconds")
            msgCount -= 1
    # Closes client socket
    clientSocket.close()


if __name__ == "__main__":
    main()

