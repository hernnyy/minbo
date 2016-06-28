# 1. Verifica si estan corriendo los procesos
PROCESOMINBO=`ps aux | grep -c minbo`
if [[ $PROCESOMINBO -eq 1 ]]
 then
   python minbo.py &
fi
exit $1
