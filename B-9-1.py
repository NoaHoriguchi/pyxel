import pyxel
import random
import math

pyxel.init(200,200)

ballx = 100
bally = 0
vx = 0.866
vy = 0.5
speed = 2
padx = 100
score = 0
angle = 0

def update():
    global ballx, bally, vx, vy, speed, padx, score, angle
    ballx += vx * speed
    bally += vy * speed
    if ballx >= 200:
        vx = -vx
    if ballx <= 0:
        vx = -vx
    if bally >= 200:
        angle = math.radians(random.randint(30, 150))
        vx = math.cos(angle)
        vy = math.sin(angle)
        ballx = (random.randint(0, 199))
        bally = 0
    padx = pyxel.mouse_x
    if padx - 20 <= ballx <=padx + 20 and bally >= 195:
        angle = math.radians(random.randint(30, 150))
        vx = math.cos(angle)
        vy = math.sin(angle)
        ballx = (random.randint(0, 199))
        score += 1
        bally = 0
        speed += 1

def draw():
    global ballx, bally, vx, vy, speed, padx, score, angle
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)
    pyxel.text(10, 10, "Score:" + str(score), 1)

pyxel.run(update, draw)
