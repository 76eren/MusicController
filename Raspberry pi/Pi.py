import BtnEvents as btn
from gpiozero import LED
import threading as t


RUN_LED = True


def burn():
	led = LED(17)
	while True:
		try:
			led.on()
		except Exception:
			led.off()


if RUN_LED:
	x = t.Thread(target=burn, args=())
	x.start()

listener = btn.events(27)
listener.listen()


