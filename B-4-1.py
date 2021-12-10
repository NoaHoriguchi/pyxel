import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(10, 200, 20):
    for b in range(10, 200, 40):
        if ((a-10)/20) % 2 == 0:
            pyxel.circ(a, b, 10, 6)
        else:
            pyxel.circ(a, b, 10, 14)

for a in range(10, 200, 20):
    for b in range(10, 200, 40):
        if ((a-10)/20) % 2 == 0:
            pyxel.circ(a, b+20, 10, 14)
        else:
            pyxel.circ(a, b+20, 10, 6)

pyxel.show()
