#!/usr/sbin/python

from datetime import datetime
from time import sleep

from maxdraw import MaxDraw
from animation import Animation

from effects import conway
from effects import scroll

from fonts import tiems_new_broman


m = MaxDraw(4)
m.init()

a = Animation(m.width, m.height)

for i in range(3):
    noise = m.prepareString(datetime.now().strftime('%H:%M:%S'), tiems_new_broman.Font())
    m._displayCanvas.placeImage(noise)
    m.paintCanvas()
    sleep(1)

a.placeImage(noise)
a.addEffect(conway.Conway())

for nc in range(40):
    x = a.requestAnimationFrame()
    m._displayCanvas.placeImage(x)
    sleep(0.01)
    m.paintCanvas()
    if nc == 20:
        a.addEffect(scroll.Scroll(1))

m._displayCanvas.clear()
m.paintCanvas()
sleep(0.6)

a.removeEffect()

while(True):
    noise = m.paintNoise(0.25)
    a.placeImage(noise)
    m._displayCanvas.placeImage(noise)

    ## ToDo: check if it has reached a stable state instead of doing 100 iterations
    for i in range(100):
        m.paintCanvas()
        x = a.requestAnimationFrame()
        m._displayCanvas.placeImage(x)
        #sleep(0.2)
