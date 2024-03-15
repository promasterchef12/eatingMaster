from pygame import*
from random import randint
from time import time as timer

class Igrac(sprite.Sprite):
    def __init__(self, slika_igraca, x_ig, y_ig, duz, sir, brzina_ig):
        super().__init__()
        self.image = transform.scale(image.load(slika_igraca), (duz,sir))
        self.brzina = brzina_ig
        self.rect = self.image.get_rect()
        self.rect.x = x_ig
        self.rect.y = y_ig
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Igrac):
    def update_R(self):
        tipke = key.get_pressed()
        if tipke[K_UP] and self.rect.y > 5:
            self.rect.y -= self.brzina
        if tipke[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.brzina
        

    def update_L(self):
            tipke = key.get_pressed()
            if tipke[K_w] and self.rect.y > 5:
                self.rect.y -= self.brzina
            if tipke[K_s] and self.rect.y < 420:
                self.rect.y += self.brzina   

merjem = Player('USTA.png', 500,89,100,100,10)
luk = Player('merjem.png', 250,99,100,100,10)
iman = Player('USTA.png', 0,89,100,100,10)


back = (138,208,222)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
clock = time.Clock()
FPS = 68
game = True

while game:
    window.fill(back)

    for e in event.get():
        if e.type == QUIT:
            game = False
    luk.reset()
    iman.update_L()
    iman.reset()
    merjem.update_R()
    merjem.reset()
    display.update()
    clock.tick(FPS)