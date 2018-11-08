import graphics

import colorsys
import colors


def colorGenerator(interval):
    while True:
        for index, i in enumerate(rgbiter()):
            for a in range(interval):
                yield graphics.color_rgb(*ik)

            index = 0


def rgbiter():
    h, s, v, = 0, 100 / 100, 0.99,

    while h < 1:
        h += 0.005
        yield tuple(map(lambda x: int(x*256), colorsys.hsv_to_rgb(h, s, v)))

    while h >= 0:
        h -= 0.005
        yield tuple(map(lambda x: int(x * 256), colorsys.hsv_to_rgb(h, s, v)))



#
# def _iter(_iterable, interval=1):
#     index = 0
#     counter = 0
#     while index < len(_iterable):
#         counter += 1
#         yield _iterable[index]
#
#         if not counter % interval:
#             index += 1
#             counter = 0