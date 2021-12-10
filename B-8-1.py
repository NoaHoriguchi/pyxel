import pyxel

pyxel.init(200,200)

ballx = 100
bally = 0
vx = 0.866
vy = 0.5
speed = 2

def update():
    global ballx, bally, vx, vy, speed
    ballx += vx*speed
    bally += vy*speed
    if ballx >= 200:
        vx = -0.866
    if ballx <= 0:
        vx = 0.866
    if bally >= 200:
        ballx = 100
        bally = 0
        vx = 0.866

def draw():
    global ballx, bally, vx, vy
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)

pyxel.run(update, draw)
