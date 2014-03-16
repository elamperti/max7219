#!/usr/sbin/python

from max7219 import Max7219

class MaxDisplay(Max7219):
    def __init__(self, display_count=1, spi_port=0, spi_clock=1000000):
        self.__displayCount = display_count
        self.__canvasSize = {
            'width': 8 * display_count,
            'height': 8
        }
        Max7219.__init__(self, spi_port, spi_clock, display_count)

    def __del__(self):
        self.stop()

    def stop(self):
        """Stops using the display"""
        self.shutdown()

    def paintCanvas(self, c):
        """Sends canvas c to the MAX7219 to be displayed"""
        for d in range(self._max.getDisplayCount()):
            self._max.setDisplay(d+1)
            for x in range(8):
                #print "X: " + str(x) + " - COL: " + str(d*8+x) +  " - BIN: " + str(self._displayCanvas.getCol(d*8 + x))
                self._max.send(self._max.DIGIT_0 + x, ord(c.getCol(d*8 + x).tobytes()))            
