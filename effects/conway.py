#!/usr/sbin/python

from effect import Effect

import canvas

class Conway(Effect):

    def __init__(self):
        pass

    def applyStep(self, a):
        """Applies a step of this effect to the animation canvas"""
        canvas_width = a.getWidth()
        canvas_height = a.getHeight()
        tmpCanvas = canvas.Canvas(canvas_width, canvas_height)
        for y in range(canvas_height):
            for x in range(canvas_width):
                tmpCanvas.setPoint(x, y, self.__isAlive(a, x, y, canvas_width, canvas_height))
        a._c = tmpCanvas._c

    def __isAlive(self, c, pos_x, pos_y, max_width, max_height):
        """Returns the status of the cell in {x,y} for the next iteration"""
        neighbours = 0

        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if x == 0 and y == 0:
                    currentStatus = c.getPoint(pos_x, pos_y)
                elif c.getPoint((max_width+pos_x+x) % max_width, (max_height+pos_y+y) % max_height):
                    neighbours += 1
        
        # 1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
        # 2. Any live cell with two or three live neighbours lives on to the next generation.
        # 3. Any live cell with more than three live neighbours dies, as if by overcrowding.
        # 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        if neighbours == 3: # rule 4
            return True
        elif 2 > neighbours or neighbours > 3: # rules 1 and 3
            return False
        else: # rule 2
            return currentStatus 