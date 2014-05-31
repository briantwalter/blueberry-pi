#!/bin/bash

#
# splashimg.sh		Paint image on LCD display
# version		0.0.1
# author		Brian Walter @briantwalter
# description		Show a 320x240 JPG image on the LCD TFT display
#

ID=`id -u`
IMG=$1
CMD="/usr/bin/fbi -T 2 -d /dev/fb1 -noverbose -a ${IMG}"

# check for root permissions
if [ ${ID} != 0 ]; then
  echo "FATAL: you must run $0 as root"
  exit 1
fi
# make sure we got an argument
if [ "${IMG}" == "" ]; then
  echo "FATAL: usage $0 /path/to/image.jpg"
  exit 1
fi
# check for image and show it
if [ -f ${IMG} ]; then
  ${CMD} > /dev/null 2>&1
else
  echo "FATAL: ${IMG} is not a file"
fi
