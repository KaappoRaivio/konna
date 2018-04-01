from graphics import *
import math


class Konna:
    def __init__(self, window_dim_x=640, window_dim_y=480):
        self.line_color = 'black'
        self.__line_width = 1
        self.__orientation = 0

        self.__pos_x = 0
        self.__pos_y = 0

        self.pen_down = False

        self.window = GraphWin('Konna', window_dim_x, window_dim_y)

        self.__window_dim_x = window_dim_x
        self.__window_dim_y = window_dim_y

        self.drawSelf()

    def drawSelf(self):
        circle = Circle(self.position, 5)
        circle.setFill('black')
        circle.draw(self.window)

    def penDown(self):
        self.pen_down = True

    def penUp(self):
        self.pen_down = False

    def turn(self, amount):
        self.orientation += amount

    def move(self, distance):
        print(self.pos_x)
        print(self.pos_y)
        self.pos_x += int(math.sin(math.radians(self.orientation)) * distance)
        self.pos_y -= int(math.cos(math.radians(self.orientation)) * distance)

    @property
    def position(self):
        return Point(self.pos_x + self.__window_dim_x / 2, self.pos_y + self.__window_dim_y / 2)

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

    @property
    def pos_x(self):
        return self.__pos_x

    @pos_x.setter
    def pos_x(self, pos_x):
        if pos_x < -(self.__window_dim_x / 2):
            self.__pos_x = -(self.__window_dim_x / 2)
        elif pos_x > self.__window_dim_x / 2:
            self.__pos_x = (self.__window_dim_x / 2)
        else:
            self.__pos_x = pos_x

    @property
    def pos_y(self):
        return self.__pos_y

    @pos_y.setter
    def pos_y(self, pos_y):
        if pos_y < -(self.__window_dim_y / 2):
            self.__pos_y = -(self.__window_dim_y / 2)
        elif pos_y > self.__window_dim_y / 2:
            self.__pos_y = (self.__window_dim_y / 2)
        else:
            self.__pos_y = pos_y

    def __del__(self):
        self.window.close()
        del self

a = Konna()

a.pos_x = 0
a.pos_y = 0

a.orientation = 12
a.move(100)

# a.drawSelf()

while True:
    try:
        pass
    except KeyBoardInterrupt:
        break


print(a.pos_x, a.pos_y)
