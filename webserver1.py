# import socket module
from socket import *

# In order to terminate the program
import sys

# Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
### YOUR CODE HERE ###
serverPort = 960
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024) ### YOUR CODE HERE ###
        
        print('Message is: ', message)

        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() ### YOUR CODE HERE ###

        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) ### YOUR CODE HERE ###

        # Send the content of the requested file into socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        # Close client socket
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode()) 
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode()) ### YOUR CODE HERE ###

        # Close client socket
        connectionSocket.close() ### YOUR CODE HERE ###

# Close server socket
serverSocket.close()

# Terminate the program after sending the corresponding data
sys.exit()

