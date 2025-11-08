# ======================================================================================================
# SERVER SIDE PROGRAM — SOCKET PROGRAMMING

# This program creates a server socket, waits for a client to connect,
# receives messages from the client, and sends replies back.
# ======================================================================================================

import socket

# Step 1: Create a socket
s = socket.socket()
print('Socket created successfully')

# Step 2: Bind the socket to an IP address and port number
s.bind(("192.168.10.64", 6000))  # Use your local IP address and any available port
s.listen(3)  # Server can listen to 3 connections at once
print('Waiting for connection...')

# Step 3: Accept connection and communicate
while True:
    c, address = s.accept()
    print('Connected with client address:', address)

    # Receive message from client
    res = c.recv(1024).decode()  # 1024 bytes buffer size
    print('Message from client:', res)

    # Send message to client
    c.send(bytes('Welcome client, I am the server.', 'utf-8'))

    # Receive another message from client
    res1 = c.recv(1024).decode()
    print('Client name received:', res1)

    # Send reply to client
    name = input('Enter your name (Server): ')
    c.send(bytes(f'Hello {res1}, I am {name}.', 'utf-8'))

    c.close()
    print('Connection closed.\n')
