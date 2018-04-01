from graphics import *

class Konna:
    def __init__(self):
        self.line_color = 'black'
        self.__line_width = 1
        self.__orientation = 0

    @property
    def orientation(self):
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation):
        self.__orientation = orientation % 360

    @property
    def line_width(self):
        return self.__line_width

    @line_width.setter
    def line_width(self, line_width):
        self.__line_width = line_width if line_width >= 0 else 0
