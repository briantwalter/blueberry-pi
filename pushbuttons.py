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

# button logic
def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
      input_state18 =  GPIO.input(18)
      if input_state18 == False:
        # shutdown the system  
        subprocess.call('/sbin/shutdown -h now', shell=True)
      input_state27 =  GPIO.input(27)
      if input_state27 == False:
        # reboot the system
        subprocess.call('/sbin/reboot', shell=True)
      input_state22 =  GPIO.input(22)
      if input_state22 == False:
        # toggle display on and off
        subprocess.call('/var/local/bin/backlight.sh toggle', shell=True)
      input_state23 =  GPIO.input(23)
      if input_state23 == False:
        # display random 320x240 picture
        subprocess.call('/var/local/bin/splashimg.sh catfact', shell=True)
      time.sleep(0.1)
    GPIO.cleanup()

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

# execute the app according to argument
app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
