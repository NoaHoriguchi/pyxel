import math
import random
import pyxel

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200
BUBBLE_MAX_SPEED = 1.8
BUBBLE_INITIAL_COUNT = 5
BUBBLE_EXPLODE_COUNT = 3

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Bubble:
    
    #define bubble
    
    def __init__(self):
        self.r = random.uniform(3, 10) #radius

        self.pos = Vec2( #position
            random.uniform(self.r, SCREEN_WIDTH - self.r),
            random.uniform(self.r, SCREEN_HEIGHT - self.r),
        )

        self.vel = Vec2( #movement velocity
            random.uniform(-BUBBLE_MAX_SPEED, BUBBLE_MAX_SPEED),
            random.uniform(-BUBBLE_MAX_SPEED, BUBBLE_MAX_SPEED),
        )

        self.color = random.randint(1, 15) #color

    def update(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

        #define rebound and movement

        if self.vel.x < 0 and self.pos.x < self.r:
            self.vel.x *= -1

        if self.vel.x > 0 and self.pos.x > SCREEN_WIDTH - self.r:
            self.vel.x *= -1

        if self.vel.y < 0 and self.pos.y < self.r:
            self.vel.y *= -1

        if self.vel.y > 0 and self.pos.y > SCREEN_HEIGHT - self.r:
            self.vel.y *= -1

class App:
    def __init__(self):
        #window size and caption + mouse show
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Pyxel Bubbles")
        pyxel.mouse(True)
        
        self.score = 500
        self.click = 0
        #変数？
        self.bx = 500
        self.by = 0
        self.vy = 10
        self.time = 60

        self.is_exploded = False
        self.bubbles = [Bubble() for _ in range(BUBBLE_INITIAL_COUNT)] #最強コード

        pyxel.run(self.update, self.draw) #def bubble draw and update

    def update(self):

        bubble_count = len(self.bubbles)
        #len(self.bubbles) =  number of bubbles
        self.by += self.vy
        if self.by >= 300 or self.by <= 0:
            self.vy = -self.vy
            self.time -= 1

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            for i in range(bubble_count):
                bubble = self.bubbles[i]
                dx = bubble.pos.x - pyxel.mouse_x
                dy = bubble.pos.y - pyxel.mouse_y
                

                #check if bubble clicked
                if dx * dx + dy * dy < bubble.r * bubble.r:
                    self.is_exploded = True
                    new_r = math.sqrt(bubble.r * bubble.r / BUBBLE_EXPLODE_COUNT)
                    #more explode count = smaller bubble explosion
                    self.score += (int(100 * (1 / bubble.r)))
                    self.click += 1

                    for j in range(BUBBLE_EXPLODE_COUNT):
                        angle = math.pi * 2 * j / BUBBLE_EXPLODE_COUNT
                        #angle less for more explosion
                        new_bubble = Bubble()
                        new_bubble.r = new_r
                        new_bubble.pos.x = bubble.pos.x + (bubble.r + new_r) * math.cos(angle)
                        new_bubble.pos.y = bubble.pos.y + (bubble.r + new_r) * math.sin(angle)
                        new_bubble.vel.x = math.cos(angle) * BUBBLE_MAX_SPEED
                        new_bubble.vel.y = math.sin(angle) * BUBBLE_MAX_SPEED
                        #new bubble speed depends on max speed
                        self.bubbles.append(new_bubble)

                    del self.bubbles[i]
                    #delete exploded bubble
                    break

        for i in range(bubble_count - 1, -1, -1):
            bi = self.bubbles[i]
            bi.update()

            for j in range(i - 1, -1, -1):
                bj = self.bubbles[j]
                dx = bi.pos.x - bj.pos.x
                dy = bi.pos.y - bj.pos.y
                total_r = bi.r + bj.r
                #radius of both bubble combined

                if dx * dx + dy * dy < total_r * total_r:
                    new_bubble = Bubble()
                    new_bubble.r = math.sqrt(bi.r * bi.r + bj.r * bj.r) + 1
                    new_bubble.pos.x = (bi.pos.x * bi.r + bj.pos.x * bj.r) / total_r
                    new_bubble.pos.y = (bi.pos.y * bi.r + bj.pos.y * bj.r) / total_r
                    new_bubble.vel.x = (bi.vel.x * bi.r + bj.vel.x * bj.r) / total_r
                    new_bubble.vel.y = (bi.vel.y * bi.r + bj.vel.y * bj.r) / total_r
                    #everything averaged out by total radius
                    self.bubbles.append(new_bubble)
                    self.score -= (int(bi.r))

                    del self.bubbles[i]
                    del self.bubbles[j]
                    #delete merged bubble
                    bubble_count -= 1
                    #-1-1+1 = -1
                    break
        

    def draw(self):
        pyxel.cls(0)

        if self.score <= 0 or self.time <= 0:
            pyxel.text(80, 90, "GAME OVER", pyxel.frame_count % 15 + 1)
            pyxel.text(65, 30, "EXPLOSIONS: " + (str(self.click)), pyxel.frame_count % 15 + 1)
            pyxel.stop()
        else:
            for bubble in self.bubbles:
                pyxel.circ(bubble.pos.x, bubble.pos.y, bubble.r, bubble.color)
                pyxel.circ(self.bx, self.by, 10, 6)
                pyxel.text(10, 30, "TIME: " + (str(self.time)), pyxel.frame_count % 15 + 1)

            if not self.is_exploded and pyxel.frame_count % 20 < 10:
                pyxel.text(80, 50, "CLICK ON BUBBLE", pyxel.frame_count % 15 + 1)
        
            if self.score >= 0:
                pyxel.text(10, 10, "LIFE: " + (str(self.score)), pyxel.frame_count % 15 + 1)
                pyxel.text(10, 20, "EXPLOSIONS: " + (str(self.click)), pyxel.frame_count % 15 + 1)

App()

