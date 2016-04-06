import RPi.GPIO as GPIO
import time


CODE = {' ': ' ',
        'D': '-..',
        'E': '.',
        'H': '....',
        'L': '.-..',
        'O': '---',
        'R': '.-.',
        'W': '.--',}
ledPin=11
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)


def dot():
	GPIO.output(ledPin,1)
	time.sleep(0.3)
	GPIO.output(ledPin,0)
	time.sleep(0.3)

def dash():
	GPIO.output(ledPin,1)
	time.sleep(0.9)
	GPIO.output(ledPin,0)
	time.sleep(0.3)

while True:
	input = raw_input('Input Message Here')
	for letter in input:
			for symbol in CODE[letter.upper()]:
				if symbol == '-':
					dash()
				elif symbol == '.':
					dot()
				else:
					time.sleep(0.3)
			time.sleep(0.3)