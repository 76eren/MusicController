import socket


class Networking():
	def __init__(self):
		self.ip = "SERVER IP"
		self.port = 6969
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((self.ip, self.port))
		self.s.sendall(b"assign")


	def send(self, message):
		self.s.sendall(message)










