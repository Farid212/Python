import socket

target_host = "127.0.0.1"
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some Data
client.sendto("AAABBBCCC", (target_host, target_port))

# Receive some Data
data, addr = client.recvfrom(4096)

print data
