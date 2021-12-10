import pyxel
import random
import math

pyxel.init(200,200)

ballx = [0]
for i in range(0, len(ballx)):
    ballx[i] = random.randint(0, 199)
bally = [0, 0, 0]
vx = [0]
vy = [0]
for i in range(0, len(ballx)):
    angle = math.radians(random.randint(30, 150))
    vx[i] = math.cos(angle) 
    vy[i] = math.sin(angle)
speed = 2
padx = 100
score = 0
miss = 0
add1 = 0
add2 = 0
pyxel.sound(0).set(note='c3e3g3c4c4', tone='s', volume='4', effect=('n' * 4 + 'f'), speed=7)
pyxel.sound(1).set(note='f3 b2 f2 b1  f1 f1 f1 f1',tone='p',volume=('4' * 4 + '4321'),effect=('n' * 7 + 'f'),speed=9,)

def update():
    global ballx, bally, vx, vy, speed, padx, score, angle, miss, add1, add2
    for i in range(0, len(ballx)):
        if ballx[i] >= 200 or ballx[i] <= 0:
            vx[i] = -vx[i]
        ballx[i] += vx[i]
        bally[i] += vy[i]
        if bally[i] >= 200:
            angle = math.radians(random.randint(30, 150))
            vx[i] = math.cos(angle) * speed
            vy[i] = math.sin(angle) * speed
            ballx[i] = (random.randint(0, 199))
            bally[i] = 0
            pyxel.play(0,1)
            miss += 1
        padx = pyxel.mouse_x
        if padx - 20 <= ballx[i] <=padx + 20 and bally[i] >= 195:
            angle = math.radians(random.randint(30, 150))
            speed += 0.5
            vx[i] = math.cos(angle) * speed
            vy[i] = math.sin(angle) * speed
            ballx[i] = (random.randint(0, 199))
            score += 1
            bally[i] = 0
            pyxel.play(0,0)
    if score == 10:
            add1 += 1
    if score == 20:
            add2 += 1
    if add1 == 1:
        ballx.append(random.randint(0, 199))
        bally.append(random.randint(0, 199))
        angle = math.radians(random.randint(30, 150))
        vx.append (math.cos(angle))
        vy.append (math.sin(angle))
        speed = 2
    if add2 == 2:
        ballx.append(random.randint(0, 199))
        bally.append(random.randint(0, 199))
        angle = math.radians(random.randint(30, 150))
        vx.append (math.cos(angle))
        vy.append (math.sin(angle))
        speed = 2

def draw():
    global ballx, bally, vx, vy, speed, padx, score, angle, miss, add
    pyxel.cls(7)
    for i in range(0, len(ballx)):
        pyxel.circ(ballx[i], bally[i], 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)
    pyxel.text(10, 10, "Score:" + str(score), 1)
    if miss >= 10:
        pyxel.cls(1)
        pyxel.text(80, 100, "GAME OVER", 7)
        bally = [0, 0, 0]



pyxel.run(update, draw)
