import pyxel
import random
import math

pyxel.init(200,200)

ballx = [0, 0, 0]
for i in range(0, 3):
    ballx[i] = random.randint(0, 199)
bally = [0, 0, 0]
vx = [0, 0, 0]
vy = [0, 0, 0]
for i in range(0, 3):
    angle = math.radians(random.randint(30, 150))
    vx[i] = math.cos(angle) 
    vy[i] = math.sin(angle)
speed = 5
padx = 100
score = 0
miss = 0
balls = 1
p = 0
num1 = 10
num2 = 7
b = 0

pyxel.sound(0).set(note='c3e3g3c4c4', tone='s', volume='4', effect=('n' * 4 + 'f'), speed=7)
pyxel.sound(1).set(note='f3 b2 f2 b1  f1 f1 f1 f1',tone='p',volume=('4' * 4 + '4321'),effect=('n' * 7 + 'f'),speed=9,)

def update():
    global ballx, bally, angle, vx, vy, padx, speed, score, miss, balls, p, num1, num2, b
    for i in range(0, balls):
        if ballx[i] >= 200 or ballx[i] <= 0:
            vx[i] = -vx[i]
            num1 = random.randint(4,10)
            num2 = random.randint(1,15)
        ballx[i] += vx[i]
        bally[i] += vy[i]
        if bally[i] >= 200:
            pyxel.play(0, 1)
            ballx[i] = random.randint(0, 199)
            bally[i] = 0
            angle = math.radians(random.randint(30,150))
            vx[i] = math.cos(angle) * speed
            vy[i] = math.sin(angle) * speed
            miss += 1
            num1 = random.randint(0, 10)
            num2 = random.randint(1,15)
        padx = pyxel.mouse_x
        if bally[i] >= 195 and padx-20 <= ballx[i] <= padx+20:
            pyxel.play(0, 0)
            score += 10
            speed += 0.2
            ballx[i] = random.randint(0, 199)
            bally[i] = 0
            angle =math.radians(random.randint(30,150))
            vx[i] = math.cos(angle) * speed
            vy[i] = math.sin(angle) * speed
            p += 1
            num1 = random.randint(4,10)
            num2 = random.randint(1,15)
            if p == 10 and balls < 3:
                balls += 1
                speed -= 2
                p = 0



def draw():
    global ballx, bally, angle, vx, vy, padx, speed, score, miss, balls, p, num1, num2, b
    if miss >= 10:
        pyxel.text(80, 90, "GAME OVER", 7)
        pyxel.stop()
    else:
        pyxel.cls(num2 - 1)
        for i in range(0, balls):
            pyxel.circ(ballx[i], bally[i], num1, num2)
        pyxel.rect(padx-20, 195, 40, 5, 15)
        pyxel.text(10, 10, "score: " + str(score), 7)



pyxel.run(update, draw)
