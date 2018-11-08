import math
import konna
from graphics import Point, Rectangle
import random

a = konna.Konna(no_bounds=True, framerate=10, window_dim_x=1000, window_dim_y=1000)

# print(a.__framerate, 'asd')

rect = Rectangle(Point(0, 0), Point(1000, 1000))
rect.setFill('black')

# rect.draw(a.window)

a.penDown()

a.orientation = 0
a.line_color = 'blue'
a.line_width = 1

def etäisyysNäytöllä(piste_1, piste_2):
    pos_1_x, pos_1_y, pos_2_x, pos_2_y = 0, 0, 0, 0

    if isinstance(piste_1, Point):
        pos_1_x = piste_1.x
        pos_1_y = piste_1.y
    else:
        pos_1_x = piste_1[0]
        pos_1_y = piste_1[1]

    if isinstance(piste_2, Point):
        pos_2_x = piste_2.x
        pos_2_y = piste_2.y
    else:
        pos_2_x = piste_2[0]
        pos_2_y = piste_2[1]

    pos_x_delta = abs(pos_2_x - pos_1_x)
    pos_y_delta = abs(pos_2_y - pos_1_y)

    return math.sqrt(pos_x_delta ** 2 + pos_y_delta ** 2)


# print(etäisyysNäytöllä((4, 0), (10, 6)))

# quit()

kulmien_määrä = 10

i = kulmien_määrä - 1

kulmien_summa = (kulmien_määrä - 2) * 180

kulma_1 = kulmien_summa / kulmien_määrä

# kulmat = [kulma_1  for i in range(kulmien_määrä)]
kulmat = []

for i in range(kulmien_määrä):
    temp = random.randint(kulma_1 / 2, 180)
    kulmat.append(temp)


vajaa = kulmien_summa - sum(kulmat)
for i in range(len(kulmat)):

    kulmat[i] += vajaa / kulmien_määrä

kulmat = sorted(kulmat)
kulmat = kulmat[::-1]


sivut = [i for i in range(kulmien_määrä - 1, kulmien_määrä * 2 - 1)]

print(len(kulmat))
print(len(sivut))
# quit()

indeksi = 0
while i <= 2 * kulmien_määrä - 2:
    index = random.randint(0, len(kulmat) - 1)

    sivu = sivut.pop(index)
    kulma = kulmat.pop(index)

    a.move(sivu)
    a.orientation += 180 - kulma

    indeksi += 1

    # print(i)

input()
    # kulma =
