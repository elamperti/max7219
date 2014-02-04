#!/usr/sbin/python

from time import sleep

import wiringpi2


class Max7219():
    NOOP        = 0x00
    DIGIT_0     = 0x01 
    DIGIT_1     = 0x02 
    DIGIT_2     = 0x03 
    DIGIT_3     = 0x04 
    DIGIT_4     = 0x05 
    DIGIT_5     = 0x06 
    DIGIT_6     = 0x07 
    DIGIT_7     = 0x08 
    DECODE_MODE = 0x09
    BRIGHTNESS  = 0x0A
    SCAN_LIMIT  = 0x0B
    SHUTDOWN    = 0x0C
    TEST        = 0x0F
    NOOP_STR    = "00"
    
   
    def __init__(self, channel=0, speed=1000000, display_count=1, keep_alive=False):
        self.__channel = channel
        self.setDisplayCount(display_count)
        self.keep_alive = keep_alive
        wiringpi2.wiringPiSPISetup(self.__channel, speed)
        self.__display = 0 # Starts on display 0


    def __del__(self):
        if not self.keep_alive:
            self.shutdown()

    def init(self, brightness=0x01, scan_limit=0x07):
        for d in range(self.__display_count):
            self.setDisplay(d+1)
            self.send(self.DECODE_MODE, 0x00)
            self.send(self.BRIGHTNESS, brightness)
            self.send(self.SCAN_LIMIT, scan_limit)
            self.clear(d)
            self.send(self.TEST, 1)
            sleep(0.25)
            self.send(self.TEST, 0)
            self.send(self.SHUTDOWN, 1)


    def shutdown(self, display=0):
        if display == 0:
            for d in range(self.__display_count):
                print "SHUTDOWN " + str(d)
                self.shutdown(d+1)
        else:
            tmpCurrentDisplay = self.getDisplay()
            self.setDisplay(display - 1)

            self.send(self.SHUTDOWN, 0)

            self.setDisplay(tmpCurrentDisplay)



    def clear(self,display=0):
        if display == 0:
            tmpCurrentDisplay = self.getDisplay()
            self.setDisplay(display)
        
        for i in range(8):
            self.send(self.DIGIT_0 + i, 0b00000000)
        
        if display == 0:
            self.setDisplay(tmpCurrentDisplay)

    def clearAll(self):
        for d in range(self.__display_count):
            self.clear(d+1)

    def send(self, address, data):
        #msg = address << 8 | data
        msg =  chr(self.NOOP) * (self.__display_count - self.__display) * 2
        msg += chr(address % 256) + chr(data % 256) # Avoids unicode
        #print  "{0:0>{1}}".format(bin(address)[2:], 16) + " " + "{0:0>{1}}".format(bin(data)[2:], 16)
        msg += chr(self.NOOP) * (self.__display) * 2
        return wiringpi2.wiringPiSPIDataRW(self.__channel, msg)


    def getDisplay(self):
        return self.__display + 1


    def setDisplay(self, n):
        self.__display = n - 1
        

    def getDisplayCount(self):
        return self.__display_count

    def setDisplayCount(self, how_many):
        self.__display_count = how_many
