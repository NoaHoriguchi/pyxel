import pyxel
import random
import math

pyxel.init(200,200)

bx = 500
by = 0
vx = 0
vy = 10
time = 100
a = True
pyxel.load("my_resource.pyxres")

def update():
    global bx, by, vx, vy, time, a
    by += vy
    if by >= 300 or by <= 0:
        vy = -vy
        time -= 1
        
def draw():
    global bx, by, vx, vy, time, a
    pyxel.cls(7)
    pyxel.circ(bx, by, 10, 6)
    pyxel.text(80, 90, "TIME: " + (str(time)), 0)
    if a == True:
        pyxel.playm(4, loop=False)

pyxel.run(update, draw)