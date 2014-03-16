#!/usr/sbin/python

#import threading
from time import sleep

import canvas

class Animation(canvas.Canvas):
    def __init__(self, w, h):
        canvas.Canvas.__init__(self, w, h)
        self.__effects = []
        ##self.__animationSpeed = 0.04
        #self._animationCanvas = canvas.Canvas(w, h)

    #    def startAnimation(self, speed, paintMethod):
        
    #    def __animate(self, speed, paintMethod):
            
    #    def stop(self):

    def requestAnimationFrame(self):
        """Moves the animation one step and returns the resulting frame as canvas"""
        for effect in self.__effects:
            effect.applyStep(self)
        return self

    def addEffect(self, e):
        """Adds the effect e to the animation's effect queue"""
        self.__effects.append(e)

    def insertEffect(self, e, pos):
        """Adds the effect e to the animation's effect queue in the position pos"""
        self.__effects.insert(pos, e)