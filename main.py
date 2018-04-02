import math
import konna
from graphics import Point, Rectangle

a = konna.Konna(no_bounds=True, framerate=100, window_dim_x=1000, window_dim_y=1000)

# print(a.__framerate, 'asd')

rect = Rectangle(Point(0, 0), Point(1000, 1000))
rect.setFill('black')

# rect.draw(a.window)

a.penDown()

a.orientation = 0
a.line_color = 'blue'
a.line_width = 1


värit = ['red', 'orange', 'yellow', 'green', 'blue', 'red']#, 'purple']#, 'black']

i = 10

span = 500

while KeyboardInterrupt:
    i += 1
    a.orientation += 29

    # a.line_color = värit[i % len(värit)]

    a.move(i)

    # for c in range(len(värit)):
    #     if (c - 1) * span < c * (i % span) < c * span:
    #         a.line_color = värit[c]

    if i % 4 == 0:
        a.jump(10, 10)

    if i % 3 == 0:
        a.jump(-10, -10)
