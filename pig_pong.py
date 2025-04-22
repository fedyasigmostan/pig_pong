import pygame as p

clock = p.time.Clock()
window = p.display.set_mode((900, 600), )
window.fill((175, 238, 238))

class GameSprite(p.sprite.Sprite):
    def __init__(self, image, x, y, width, height, speed):
        super().__init__()
        self.image = p.transform.scale(p.image.load(image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw_sprite(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move_player1(self):
        keys = p.key.get_pressed()
        if keys[p.K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[p.K_s] and self.rect.y <= 400:
            self.rect.y += self.speed

    def move_player2(self):
        keys = p.key.get_pressed()
        if keys[p.K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[p.K_DOWN] and self.rect.y <= 400:
            self.rect.y += self.speed

racket1 = Player('./images/roketka.png', 20, 20, 200, 200, 10)
racket2 = Player('./images/roketka.png', 700, 20, 200, 200, 10)
pig = GameSprite('./images/svin.png', 350, 200, 100, 100, 5)

speed_x = 3
speed_y = -3
run = True
while run:
    window.fill((175, 238, 238))

    for e in p.event.get():
        if e.type == p.QUIT:
            run = False

    if pig.rect.y >= 500 or pig.rect.y <= 0:
        speed_y *= -1

    if p.sprite.collide_rect(pig, racket1) or p.sprite.collide_rect(pig, racket2):
        speed_x *= -1

    if pig.rect.x >= 800:
        run = False
    if pig.rect.x <= 0:
        run = False
    pig.rect.y += speed_y
    pig.rect.x += speed_x


    racket1.draw_sprite()
    racket1.move_player1()
    racket2.draw_sprite()
    racket2.move_player2()

    pig.draw_sprite()

    p.display.update()
    clock.tick(60)








