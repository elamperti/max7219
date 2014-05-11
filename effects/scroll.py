#!/usr/sbin/python

from effect import Effect

class Scroll(Effect):
    DIRECTION_RIGHT = 0
    DIRECTION_LEFT = 1
    DIRECTION_UP = 2
    DIRECTION_DOWN = 3

    def __init__(self, direction=1):
        self.setDirection(direction)

    def setDirection(self, d):
        """Sets the direction in which the canvas will scroll and updates applyStep to point to the according function"""
        if d == self.DIRECTION_RIGHT:
                self.applyStep = self.scrollRight
        elif d == self.DIRECTION_LEFT:
                self.applyStep = self.scrollLeft
        elif d == self.DIRECTION_UP:
                self.applyStep = self.scrollUp
        elif d == self.DIRECTION_DOWN:
                self.applyStep = self.scrollDown

    def scrollRight(self, a):
        a.rshift(8)

    def scrollLeft(self, a):
        a.lshift(8)

    def scrollUp(self, a):
        a.placeImage(a._c, 0, 1)

    def scrollDown(self, a):
        a.placeImage(a.getImage(0,1,a.getWidth(),7))