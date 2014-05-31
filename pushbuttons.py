#!/usr/bin/python

#
# pushbuttons.py	LCD TFT push button controls
# version		0.0.1
# author		Brian Walter @briantwalter
# description		Simple loop control for the 4 buttons on the top of
#			of the Adafuit touch panel LCD for the RPi
#

import time
import subprocess
import RPi.GPIO as GPIO
from daemon import runner

# daemon properties
class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/var/local/log/pushbuttons.log'
        self.stderr_path = '/var/local/log/pushbuttons.log'
        self.pidfile_path =  '/tmp/pushbuttons.pid'
        self.pidfile_timeout = 5
    def run(self):
        main()

# button logic
def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
      input_state =  GPIO.input(18)
      print input_state
      if input_state == False:
        # shutdown the system  
        print "DEBUG: input 18"
      #if GPIO.input(27):
        # toggle display on and off
        #print "DEBUG: input 27"
      #if GPIO.input(22):
        # display random 320x240 picture
        #print "DEBUG: input 22"
      #if GPIO.input(23):
        # show console login prompt
        #print "DEBUG: input 23"
      time.sleep(0.1)
    GPIO.cleanup()

# execute the app according to argument
app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
