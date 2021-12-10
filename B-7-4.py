import pyxel

pyxel.init(200,200)
pyxel.mouse(True)

x = pyxel.mouse_x
y = pyxel.mouse_y
a = pyxel.mouse_x
b = pyxel.mouse_y
c = 0
v = pyxel.mouse_x
w = pyxel.mouse_y

def update():
    global x, y, a, b, c, v, w

    if pyxel.btnp(pyxel.KEY_SPACE):
        c += 1

        if c % 2 == 0:
            pyxel.btn(pyxel.KEY_SPACE)
            a = pyxel.mouse_x
            b = pyxel.mouse_y
            v = pyxel.mouse_x
            w = pyxel.mouse_y

        else:
            pyxel.btn(pyxel.KEY_SPACE)
            x = pyxel.mouse_x
            y = pyxel.mouse_y


def draw():
    global x, y, a, b, v, w
    pyxel.cls(7)
    if c % 2 == 1:
        pyxel.line(x, y, a, b, 0)
    else:
        pyxel.line(v, w, pyxel.mouse_x, pyxel.mouse_y, 0)

pyxel.run(update, draw)
