#!/usr/bin/python

import time, sys
import RPi.GPIO as GPIO
import requests

url = 'http://dweet.io/dweet/for/thermofan'

def registerTemp( temp ):
	global url
	temp = str(temp)
	payload = {'temp': temp}
	requests.get(url, params=payload)

spinpin = int(sys.argv[1])

GPIO.setmode(11)
GPIO.setup(spinpin, GPIO.IN, GPIO.PUD_UP)

last = 0
newval = 0
Running = 1
lasttime = 0
lastdiff = 0

lasttime = int(round(time.time() * 1000))		

while Running:
	newval = GPIO.input(spinpin)
	if newval != last and newval == 0:
		thistime = int(time.time() * 1000)
		diff = thistime - lasttime
		if diff != lastdiff and thistime % 2 == 0:
			print diff
			registerTemp( diff )
		lasttime = thistime
		lastdiff = diff

	last = newval	

GPIO.cleanup()
