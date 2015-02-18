#!/usr/sbin/python

from canvas import Canvas

class Drawing:

    def prepareString(self, str, font):
        """Returns a Canvas object with the rasterized string"""
        tmpCanvas = Canvas(8*len(str), 8)
        offset = 0
        for char in str:
            glyph = font.getChar(char)
            tmpCanvas.fromBytes(glyph, offset)
            offset += font.getCharSize(char) + font.getLetterSpace(char)
        return tmpCanvas

        