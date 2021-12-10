import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(10, 200, 20):
    for b in range(0, 200, 20):
        if a <= 100-b:
            pyxel.circ(a, 10+b, 10, 2)
        elif a <= 200-b:
            pyxel.circ(a, 10+b, 10, 3)
        elif a <= 300-b:
            pyxel.circ(a, 10+b, 10, 6)
        else:
            pyxel.circ(a, 10+b, 10, 14)
pyxel.show()
