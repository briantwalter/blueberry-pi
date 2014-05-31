#!/bin/bash

#
# backlight.sh		LCD TFT backlight set up
# version		0.0.1
# author		Brian Walter @briantwalter
# description		Create the GPIO connection to control the LCD TFT
#			screen, allowing to turn just the display on and off
#

ID=`id -u`
IO=252
BASEDIR=/sys/class/gpio

# check for root permissions
if [ ${ID} != 0 ]; then
  echo "FATAL: you must run $0 as root"
  exit 1
fi
# check if the GPIO has already been setup
if [ ! -d ${BASEDIR}/gpio${IO} ]; then
  echo ${IO} > ${BASEDIR}/export
fi
# set the gpio to output mode
echo 'out' > ${BASEDIR}/gpio${IO}/direction
# turn the display off [default]
echo '0' > ${BASEDIR}/gpio${IO}/value
# turn the display on
echo '1' > ${BASEDIR}/gpio${IO}/value
