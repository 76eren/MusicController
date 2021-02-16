import socket
import threading as t

class Server():
	def __init__(self):
		self.ip = "SERVER IP"
		self.port = 6969
		self.target = None
		self.s = socket.socket()
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.s.bind((self.ip, self.port))
		self.s.listen(5)



	def receive(self, connection):
		while True:
			self.x = connection.recv(1024)
			print(self.x)
			self.send(self.x)


	def send(self, message):
		self.target.sendall(message)


	def getConnection(self):
		while True:
			print("Beginning of loop")
			self.conn, self.addr = self.s.accept() # One is the pc and the other is the Rpi, yes I know dont kill me
			print("Somebody connected")
			self.lol = self.conn.recv(1024)
			print(f"Message is: {self.lol}")
			if self.lol.decode() == "assign":
				f = t.Thread(target=self.receive, args=(self.conn,))
				f.start()
			else:
				print("Assigning a target")
				self.target = self.conn



UwU = Server() 
UwU.getConnection()


