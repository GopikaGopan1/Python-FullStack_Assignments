# ======================================================================================================
# CLIENT SIDE PROGRAM — SOCKET PROGRAMMING
# ======================================================================================================
# This program connects to the server, sends and receives messages.
# ======================================================================================================

import socket

# Step 1: Create socket
c = socket.socket()

# Step 2: Connect to the server (Use the same IP & port as the server)
c.connect(('192.168.10.64', 6000))
print('Connected to server successfully')

# Step 3: Send message to server
c.send(bytes('Hello server, this is client.', 'utf-8'))

# Step 4: Receive server reply
re = c.recv(1024).decode()
print('Message from server:', re)

# Step 5: Send your name to server
name = input('Enter your name (Client): ')
c.send(bytes(name, 'utf-8'))

# Step 6: Receive final message from server
final = c.recv(1024).decode()
print('Final reply from server:', final)

c.close()
print('Connection closed.')
