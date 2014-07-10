#!/bin/bash

#
# splashimg.sh		Paint image on LCD display
# version		0.0.1
# author		Brian Walter @briantwalter
# description		Show a 320x240 JPG image on the LCD TFT display
#

ID=`id -u`
IMG=$1
CMD="/usr/bin/fbi -T 2 -d /dev/fb1 -noverbose -a"
DIR=/var/local/splash
CATAPI='http://ycf.apps.walternet.us/api'

# check for root permissions
if [ ${ID} != 0 ]; then
  echo "FATAL: you must run $0 as root"
  exit 1
fi
# make sure we got an argument
if [ "${IMG}" == "" ]; then
  echo "FATAL: usage $0 </path/to/image.jpg> or <random> or <catfact>"
  exit 1
fi
# special case to show a random image
if [ "${IMG}" == "random" ]; then
  IMG=`ls ${DIR}/*.jpg | shuf -n 1`
fi
# special case to show a Yoda cat fact
if [ "${IMG}" == "catfact" ]; then
  ${CMD} ${DIR}/loading0.jpg
  CATFACT=`curl -s ${CATAPI} | grep catfact | awk -F \" '{print $4}'`
  convert -background white -fill black -font Chinacat-Regular \
  -extent 320x240 -size 300x220 -gravity center caption:"${CATFACT}" \
  ${DIR}/yodacatfact.jpg &
  IDX=1
  while [ ! -f ${DIR}/yodacatfact.jpg ]
  do
    ${CMD} ${DIR}/loading${IDX}.jpg
    sleep 1
    IDX=`expr ${IDX} + 1`
  done    
  IMG="${DIR}/yodacatfact.jpg"
fi
# check for image and show it
if [ -f ${IMG} ]; then
  killall -9 /usr/bin/fbi > /dev/null 2>&1
  ${CMD} ${IMG} > /dev/null 2>&1
  if [ -f ${DIR}/yodacatfact.jpg ]; then
    rm -f ${DIR}/yodacatfact.jpg
  fi
else
  echo "FATAL: ${IMG} is not a file"
fi
