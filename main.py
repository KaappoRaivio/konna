import math

import konna

a = konna.Konna(no_bounds=False, framerate=10000000, window_dim_x=1000, window_dim_y=1000)

# print(a.__framerate, 'asd')

a.penDown()

a.orientation = 0
a.line_color = 'blue'
a.line_width = 1

i = 0

while True:
    i += 1
    a.orientation += i

    a.move(math.sin(a.orientation * i) * 25)

    # a.line_color = 'green' if i % 2 == 0 else 'red'

    # time.sleep(0.05)

    # a.update()

    # a.drawSelf()
