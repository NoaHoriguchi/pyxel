import pyxel

pyxel.init(200,200)

a = 0
b = True

def update():
    global a
    global b
    if a >= 200:
        b = False
    if a <= 0:
        b = True
    if pyxel.btnp(pyxel.KEY_SPACE):
        if b == True :
            b = False
        else:
            b = True
    if b == True :
        a += 1
    else:
        a -= 1

def draw():
    global a
    pyxel.cls(7)
    pyxel.circ(a, a, 10, 0)



pyxel.run(update, draw)
