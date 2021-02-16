import socket
import threading as t
import commands
class Networking():
	def __init__(self, IP, PORT):
		self.ip = IP
		self.port = PORT
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((self.ip, self.port))
		self.s.sendall(b"HEY") # We have to send a message just to connect to the server
		self.cmd = commands.Commands()


	def receive(self):
		while True:
			self.data = self.s.recv(1024)
			self.data = self.data.decode()
			print(self.data)

			# now we have to do stuff with our received data
			self.cmd.GetInfo(self.data) 




networker = Networking("SERVER IP", 6969)
x = t.Thread(target=networker.receive, args=())
x.start()



