#!/usr/bin/python

# simple test to check 4 push buttons

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    in18_state = GPIO.input(18)
    if in18_state == False:
        print('18 Pressed')
    in27_state = GPIO.input(27)
    if in27_state == False:
        print('27 Pressed')
    in22_state = GPIO.input(22)
    if in22_state == False:
        print('22 Pressed')
    in23_state = GPIO.input(23)
    if in23_state == False:
        print('23 Pressed')
    time.sleep(0.2)
