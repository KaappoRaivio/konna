import math
import time

import graphics

import konna

k = konna.Konna(window_dim_x=1500, window_dim_y=1000, no_bounds=True, update_interval=10)
k.goTo(0, 0)
# input()
k.penDown()

k.orientation = 90
k.line_color = 'blue'
k.line_width = 1

# graphics.Circle(graphics.Point(0, 0), 10).draw(k.window)
# k.window.update()
# input()





def sinGenerator(gain: int):
    x = 0
    y = 1
    while True:
        y = math.sin(x / gain) * gain
        yield y
        # time.sleep(0.1)
        x += 1


try:
    for counter, i in enumerate(sinGenerator(90)):
        k.orientation += i - 10
        k.move(10)
        k.update()
except KeyboardInterrupt:
    input()