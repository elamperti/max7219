#!/usr/sbin/python

from bitarray import bitarray

class Canvas():
    width = 8
    height = 8

    #_c # The canvas itself.

    def __init__(self, w, h):
        self._c = (w * h) * bitarray('0')
        self.width = w
        self.height = h

    def lshift(self, count):
        """Shifts the canvas to the left as many places as count."""
        self._c = self._c[count:] + (bitarray('0') * count)

    def rshift(self, count):
        """Shifts the canvas to the right as many places as count."""
        self._c = (bitarray('0') * count) + self._c[:-count]

    def getRow(self, n, offset=0):
        """Returns a bitarray of the requested row, starting from offset."""
        return self._c[n + offset*self.height::self.height]

    def getCol(self, n, offset=0):
        """Returns a bitarray of the requested column, starting from offset."""
        return self._c[(n*self.height + offset):((n+1) * self.height)]

    def getSize(self):
        """Returns the count of pixels."""
        return self.width * self.height;

    def writeCol(self, col, data, offset=0):
        """Overwrites a column with data, starting from offset."""
        for d in data:
            if offset > self.height: break
            self._c[col*self.height + offset] = d
            offset += 1

    def writeRow(self, row, data, offset=0):
        """Overwrites a row with data, starting from offset."""
        for d in data:
            if offset > self.width: break
            self._c[row + offset*self.height] = d
            offset += 1

    def getPoint(self, x, y):
        """Returns the logic value of a given coordinate."""
        return self._c[y*self.height + x]

    def setPoint(self, x, y, value):
        """Overwrites a certain pixel of the canvas."""
        self._c[y*self.height + x] = value

    def getImage(self, x, y, w, h):
        """Returns a Canvas object with a portion of the current canvas"""
        w = min(w, self.width - x)
        h = min(h, self.height - y)
        r = Canvas(w, h)

        for col in range(w):
            r.writeCol(col, self.getCol(x+col, y))

        return r

    def placeImage(self, img, x=0, y=0):
        """Places a Canvas object over the canvas considering offset."""
        if img.getSize() == self.getSize() and img.width == self.width:
            # Same dimensions
            self._c = img._c

        elif x == 0 and self.height == img.height:
            # Same height, just overwrite a block
            p_start = y * self.height
            p_end = y*self.height + img.getSize()
            self._c[p_start:p_end] = img._c

        else:
            # Different dimensions
            for dx in range(img.width):
                self.writeCol(x+dx, img.getCol(dx), y)

    def invert(self):
        """Flips the values of the whole canvas. Pretty simple."""
        self._c = ~self._c

    def fromBytes(self, str, startCol=0):
        """
        Transforms from bytes to pixels and writes them starting from a certain column.
        This is useful to load images from strings or to quickly redraw a part of the image.

        """
        # Convert string and store it in a temporary bitarray.
        tmp = bitarray()
        tmp.fromstring(str)

        # Apply to current canvas without altering its current size.
        p_start = startCol * self.height
        p_end = min(p_start + tmp.length(), self.getSize())
        p_size = min(p_end - p_start, tmp.length)
        self._c[p_start:p_end] = tmp[0:p_size]
