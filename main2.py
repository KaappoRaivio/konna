import math
import time

import graphics

import colorgenerator
import konna

k = konna.Konna(window_dim_x=1500, window_dim_y=1000, no_bounds=True, update_interval=10, show_circle=False)
k.goTo(0, 0)
# input()
k.penDown()

k.orientation = 90
k.line_color = 'blue'
k.line_width = 10

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


generator = colorgenerator.colorGenerator(500)

try:
    for counter, i in enumerate(sinGenerator(10)):

        k.orientation += i - 10
        k.move(5)
        k.update()
        k.line_color = next(generator)

except KeyboardInterrupt:
    input()