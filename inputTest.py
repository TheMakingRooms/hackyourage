import RPi.GPIO as GPIO
from recorder import Recorder

buttons = [24,23,18]
recordButon = 25

GPIO.setmode(GPIO.BCM)

for i in buttons:
	GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(recordButon, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:
	if GPIO.input(recordButon):
		for i in buttons:
			if GPIO.input(i):
				print("record on " + str(i))		
	else:
		for i in buttons:
			if GPIO.input(i):
				print("play " + str(i))
