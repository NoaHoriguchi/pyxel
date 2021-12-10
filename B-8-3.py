import pyxel

pyxel.init(200,200)

ballx = 100
bally = 0
vx = 0.866
vy = 0.5
speed = 5
padx = 100
score = 0

def update():
    global ballx, bally, vx, vy, speed, padx, score
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
    if (pyxel.mouse_x - 20 <= ballx <=pyxel.mouse_x + 20) and bally >= 195:
        score += 1
        ballx = 100
        bally = 0
        vx = 0.866
    padx = pyxel.mouse_x


def draw():
    global ballx, bally, vx, vy, padx, score
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)
    pyxel.text(10, 10, "Score:" + str(score), 1)

pyxel.run(update, draw)
