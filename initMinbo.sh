#!/bin/bash
# 1. Verifica si estan corriendo los procesos
PROCESOMINBO=`ps aux | grep -c minbo.py`
#echo $PROCESOMINBO
if [[ $PROCESOMINBO -eq 1 ]]
 then
   python minbo.py &
 else
   DATE=`date +%Y-%m-%d:%H:%M:%S`
   echo $DATE
   echo $PROCESOMINBO
fi
exit $1
