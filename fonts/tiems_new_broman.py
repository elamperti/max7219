#!/usr/sbin/python

class Font:
    name = 'Tiems New Broman'

    def getCharSize(self, char):
        if char == ":":
            return 2
        if char == " ":
            return 0
        else:
            return 3
            
    def getLetterSpace(self, char): return 1
    def getChar(self, char):
        if ord(char) in self.__glyph:
            return self.__glyph[ord(char)]
        else:
            return [ 0x00 ]

    __glyph = {
        32: [ 0x00 ], # ' '
        48: [ 0xFF,0x81,0xFF ], # '0'
        49: [ 0x82,0xFF,0x80 ], # '1'
        50: [ 0xE3,0x91,0x8F ], # '2'
        51: [ 0x42,0x91,0x6E ], # '3'
        52: [ 0x1F,0x10,0xFF ], # '4'
        53: [ 0xCF,0x91,0x71 ], # '5'
        54: [ 0x7E,0x91,0x62 ], # '6'
        55: [ 0xC1,0x31,0x0F ], # '7'
        56: [ 0x6E,0x91,0x6E ], # '8'
        57: [ 0x8E,0x91,0x7E ], # '9'
        58: [ 0x66,0x66 ] # ':'
    }
