import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

# Create the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the server
server.bind((bind_ip, bind_port))

# Server online and listenning
server.listen(5)

print "[*] Listenning on %s:%d" % (bind_ip, bind_port)

# this is our client-handing thread
def handle_client(client_socket):
    # print out what the client sends
    request = client_socket.recv(1024)

    print "[*] Received %s" % request

    # Send back a packet
    client_socket.send("ACK!")

    client_socket.close()

while True:
    client, addr = server.accept()
    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

    # Spin up our client thread to handle incoming Data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
