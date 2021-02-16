import keyboard
from pynput.keyboard import Controller, KeyCode

class Commands():
	def __init__(self):
		self.keyboard = Controller()
	
	def GetInfo(self, num):
		if int(num) == 1:
			self.pause()

		if int(num) == 2:
			self.skip()

		if int(num) == 3:
			self.previous()

	def pause(self):
		self.keyboard.press(KeyCode.from_vk(0xB3))


	def skip(self):
		self.keyboard.press(KeyCode.from_vk(0xB0))


	def previous(self):
		self.keyboard.press(KeyCode.from_vk(0xB1))













