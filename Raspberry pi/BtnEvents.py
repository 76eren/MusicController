import time
from gpiozero import LED, Button
import threading as t
import networking

class events():
	def __init__(self, BtnPin):
		self.btn = Button(BtnPin)
		self.clicks = 0
		self.clicking = False
		self.delay = 0.5
		self.isTiming = False
		self.networker = networking.Networking()

	def listen(self):
		while True:
			if self.btn.is_pressed and self.clicking == False:
				self.clicking = True
				self.clicks += 1
				
				if self.isTiming==False:
					self.isTiming=True

					x = t.Thread(target=self.timer, args=())
					x.start()
					
		
			if self.btn.is_pressed == False and self.clicking == True:	
				self.clicking=False


	def timer(self):
		time.sleep(self.delay)
		print(f"Clicked {self.clicks} times")
		self.isTiming = False
		clicksString = str(self.clicks)
		self.networker.send(clicksString.encode())
		self.clicks = 0









