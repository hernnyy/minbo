#!/bin/bash##
# 1. Verifica si estan corriendo los procesos
PROCESOMINBO=`ps aux | grep -c minbo`
if [[ $PROCESOMINBO -eq 1 ]]
 then
   phyton minbo.py &
fi
exit $1