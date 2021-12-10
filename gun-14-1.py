from random import randint
import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Pyxel Jump")

        pyxel.load("assets/jump_game.pyxres")

        self.leng = 40
        self.vleng = 1

        # 球の変数を定義
        self.shot_x = 72
        self.shot_y = -16
        self.shot_vx = 5
        self.shot_is_active = False

        self.life = 100
        self.player_x = 72
        self.player_y = -16
        self.player_vy = 0
        self.player_is_alive = True
        self.far_cloud = [(-10, 75), (40, 65), (90, 60)]
        self.near_cloud = [(10, 25), (70, 35), (120, 15)]
        self.floor = [(i * 60, randint(8, 104), True) for i in range(4)]
        self.fruit = [(i * 60, randint(0, 104), randint(0, 2), True) for i in range(4)]

        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        #ここに弾のupdateメソッド呼び出しを入れる
        self.update_shot()
        self.update_player()
        for i, v in enumerate(self.floor):
            self.floor[i] = self.update_floor(*v)

        for i, v in enumerate(self.fruit):
            self.fruit[i] = self.update_fruit(*v)

    def update_shot(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.shot_x = self.player_x + 10
            self.shot_y = self.player_y
            self.shot_is_active = True

        if self.shot_is_active == True:
            self.shot_x += self.shot_vx

        if self.shot_x > pyxel.width:
            self.shot_x = 72
            self.shot_y = -16
            self.shot_is_active = False

    def update_player(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 5, 0)

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 5, pyxel.width - 16)

        if pyxel.btn(pyxel.KEY_UP) :
            self.player_y = min(self.player_y - 5, pyxel.width - 16)

        if pyxel.btn(pyxel.KEY_DOWN) :
            self.player_y = min(self.player_y + 10, pyxel.width - 16)


        self.player_y += self.player_vy
        self.player_vy = min(self.player_vy + 1, 8)

        if self.player_y > pyxel.height:
            if self.player_is_alive:
                self.player_is_alive = False
                pyxel.play(3, 5)


        if pyxel.btn(pyxel.KEY_ENTER):
            self.life = 0
            self.player_x = 72
            self.player_y = -16
            self.player_vy = 0
            self.player_is_alive = True

    def update_floor(self, x, y, is_active):
        if is_active:
            if (
                self.player_x + 16 >= x
                and self.player_x <= x + self.leng
                and self.player_y + 16 >= y
                and self.player_y <= y + 8
                and self.player_vy > 0
            ):
                is_active = False
                self.player_vy = -12
                pyxel.play(3, 3)
        else:
            y += 6

        x -= 4

        if x < -40:
            x += 240
            y = randint(8, 104)
            is_active = True

        self.leng += self.vleng

        if self.leng >= 64 or self.leng <= 0:
            self.vleng = -self.vleng

        return x, y, is_active

    def update_fruit(self, x, y, kind, is_active):
        #弾が当たった時の処理を追加
        if is_active and ((abs(x - self.player_x) < 12 and abs(y - self.player_y) < 12)
        or (abs(x - self.shot_x) < 12 and abs(y - self.shot_y) < 12)):
            is_active = False
            if kind == 2:
                self.life -= (kind + 1) * 100
            else:
                self.life += (kind + 1) * 100
            self.player_vy = min(self.player_vy, -8)
            pyxel.play(3, 4)

        x -= 2

        if x < -40:
            x += 240
            y = randint(0, 104)
            kind = randint(0, 2)
            is_active = True

        return (x, y, kind, is_active)


    def draw(self):
        pyxel.cls(12)

        # draw sky
        pyxel.blt(0, 1, 1, 1, 1, 1, 32)

        # draw mountain
        pyxel.blt(0, 88, 0, 0, 64, 160, 24, 12)

        # draw forest
        offset = pyxel.frame_count % 160
        for i in range(2):
            pyxel.blt(i * 160 - offset, 104, 0, 0, 48, 160, 16, 12)

        # draw clouds
        offset = (pyxel.frame_count // 16) % 160
        for i in range(2):
            for x, y in self.far_cloud:
                pyxel.blt(x + i * 160 - offset, y, 0, 64, 32, 32, 8, 12)

        offset = (pyxel.frame_count // 8) % 160
        for i in range(2):
            for x, y in self.near_cloud:
                pyxel.blt(x + i * 160 - offset, y, 0, 0, 32, 56, 8, 12)

        # draw floors
        for x, y, is_active in self.floor:
            pyxel.blt(x, y, 0, 0, 16, self.leng, 8, 12)

        # draw fruits
        for x, y, kind, is_active in self.fruit:
            if is_active:
                pyxel.blt(x, y, 0, 32 + kind * 16, 0, 16, 16, 12)

        # draw player
        pyxel.blt(
            self.player_x,
            self.player_y,
            0,
            16 if self.player_vy > 0 else 0,
            0,
            16,
            16,
            12,
        )

        # draw shot
        pyxel.blt(
            self.shot_x,
            self.shot_y,
            0,
            80,
            0,
            16,
            16,
            12,
        )

        # draw
        s = "Life {:>4}".format(self.life)
        pyxel.text(5, 4, s, 1)
        pyxel.text(4, 4, s, 7)

        if self.player_is_alive == False or self.life <= 0 :
            pyxel.cls(1)
            pyxel.text(60, 50,"GAME OVER" , pyxel.frame_count % 15 + 1)
            pyxel.text(40, 60,"PUSH ENTER RESTART" , pyxel.frame_count % 15 + 1)
            pyxel.stop()

        if pyxel.btn(pyxel.KEY_ENTER):
            self.life = 100
            pyxel.playm(0, loop=True)

App()