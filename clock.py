#!/usr/sbin/python

from datetime import datetime
from time import sleep

from maxdraw import MaxDraw

from fonts import tiems_new_broman

a = MaxDraw(4)
a.init()
c = a.prepareString(datetime.now().strftime('%H:%M:%S'), tiems_new_broman.Font())

while(True):
    c = a.prepareString(datetime.now().strftime('%H:%M: %S'), tiems_new_broman.Font())
    a._displayCanvas.placeImage(c, 1)
    a.paintCanvas()
    sleep(1)
