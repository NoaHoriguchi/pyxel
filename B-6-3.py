import pyxel

pyxel.init(200,200)

a = 0
b = 0

def update():
    global a
    global b
    if b % 2 == 0:
        a += 1
    elif b % 2 == 1:
        a -= 1
    if a == 200:
        b += 1
    elif a == 0:
        b += 1



def draw():
    global a
    pyxel.cls(7)
    pyxel.circ(a, a, 10, 0)



pyxel.run(update, draw)
