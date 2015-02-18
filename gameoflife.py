#!/usr/sbin/python

from time import sleep

from maxdraw import MaxDraw
from animation import Animation

from effects import conway


m = MaxDraw(4)
m.init()

a = Animation(m.width, m.height)
a.addEffect(conway.Conway())

while(True):
    noise = m.paintNoise(0.25)
    a.placeImage(noise)
    m._displayCanvas.placeImage(noise)

    ## ToDo: check if it has reached a stable state instead of doing 100 iterations
    while(True): #for i in range(100):
        m.paintCanvas()
        x = a.requestAnimationFrame()
        m._displayCanvas.placeImage(x)
        sleep(15)
