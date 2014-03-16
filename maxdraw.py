#!/usr/sbin/python

import random

from time import sleep

from max7219 import Max7219
from canvas import Canvas


class MaxDraw():
    def __init__(self, display_count=1, spi_port=0, spi_clock=1000000):
        self.__displayCount = display_count
        self._displayCanvas = Canvas(8*display_count, 8)
        self._max = Max7219(spi_port, spi_clock, display_count)
        self.width = self._displayCanvas.getWidth()
        self.height = self._displayCanvas.getHeight()
        #self._displayCanvas = self._max._displayCanvas

    def __del__(self):
        #self.stop()
        pass

    def init(self):
        """Initializes the display"""
        self._max.init(0x00)

    def stop(self):
        """Stops using the display"""
        self._max.shutdown()


    def prepareString(self, str, font):
        """Returns a Canvas object with the rasterized string"""
        tmpCanvas = Canvas(8*len(str), 8)
        offset = 0
        for char in str:
            glyph = font.getChar(char)
            tmpCanvas.fromBytes(glyph, offset)
            offset += font.getCharSize(char) + font.getLetterSpace(char)
        return tmpCanvas


    def paintCanvas(self):
        """Sends _displayCanvas to the MAX7219 to be displayed"""
        for d in range(self._max.getDisplayCount()):
            self._max.setDisplay(d+1)
            for x in range(8):
                #print "X: " + str(x) + " - COL: " + str(d*8+x) +  " - BIN: " + str(self._displayCanvas.getCol(d*8 + x))
                self._max.send(self._max.DIGIT_0 + x, ord(self._displayCanvas.getCol(d*8 + x).tobytes()))            

    def paintNoise(self, ratio):
        """Returns a canvas filled with random noise using ratio as threshold."""
        tmpCanvas = Canvas(self.width, self.height)
        for b in range(tmpCanvas.getSize()):
            tmpCanvas._c[b] = False if random.random() > ratio else True
        return tmpCanvas