import pyxel

pyxel.init(200,200)
pyxel.mouse(True)

x=0
y=0
a=0
b=0

def update():
    global x, y, a, b

    if pyxel.btnp(pyxel.KEY_SPACE):
        x = pyxel.mouse_x
        y = pyxel.mouse_y
        c + 1

    if pyxel.btn(pyxel.KEY_SPACE):
        a = pyxel.mouse_x
        b = pyxel.mouse_y


def draw():
    global x, y, a, b, c
    pyxel.cls(7)
    pyxel.line(x, y, pyxel.mouse_x, pyxel.mouse_y, 0)



pyxel.run(update, draw)
