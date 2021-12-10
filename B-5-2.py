import pyxel
import math

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(0, 360, 1):
    b = math.radians(a)
    if a <= 90:
        pyxel.line(120, 120, 100+100*math.sin(b), 100+100*math.cos(b), 0)
    elif 90 < a <= 180:
        pyxel.line(120, 80, 100+100*math.sin(b), 100+100*math.cos(b), 0)
    elif 180 < a <= 270:
        pyxel.line(80, 80, 100+100*math.sin(b), 100+100*math.cos(b), 0)
    else:
        pyxel.line(80, 120, 100+100*math.sin(b), 100+100*math.cos(b), 0)
pyxel.show()
