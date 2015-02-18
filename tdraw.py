#!/usr/sbin/python

from time import sleep

from maxdraw import MaxDraw

from fonts import cp437

a = MaxDraw(4)
a.init()

c = a.prepareString(u'   THE    GAME'.encode('utf8'), cp437.Font())

for f in range(c.getWidth()):
    a._displayCanvas.placeImage(c)
    a.paintCanvas()
    c.lshift(8)
    sleep(0.26)
