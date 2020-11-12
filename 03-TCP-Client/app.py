import socket

target_host = "www.google.com"
target_port = 80

# Create a socket oject
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET means we are gong to use standart IPv4 address or hostname
# SOCK_STREAM indicates that this will be a TCP client

# Connect te client
client.connect((target_host, target_port))

# Send Data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive some Data
response = client.recv(4096)

print response
