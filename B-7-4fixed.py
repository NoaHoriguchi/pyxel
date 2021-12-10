import pyxel

pyxel.init(200,200)
pyxel.mouse(True)

x1 = 0
y1 = 0
x2 = 0
y2 = 0
a = False

def update():
    global x1, y1, x2, y2, a

    if a == False:
        if pyxel.btnp(pyxel.KEY_SPACE):
            x1 = pyxel.mouse_x
            y1 = pyxel.mouse_y
            x2 = pyxel.mouse_x
            y2 = pyxel.mouse_y
            a = True
    else:
        x2 = pyxel.mouse_x
        y2 = pyxel.mouse_y
        if pyxel.btnp(pyxel.KEY_SPACE):
            a = False
    
def draw():
    global x1, y1, x2, y2, a
    pyxel.cls(7)
    pyxel.line(x1, y1, x2, y2, 0)

pyxel.run(update, draw)
