from pygame import*
import random
clock = pygame.time.Clock()
wind = pygame.display.set_mode((600, 500))
game = True

class chel (pygame.sprite.Sprite):
    def __init__(self, img, x, y): 
        super().__init__()
        self.image = transform.scale(image.load(img), (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def put(self):
        wind.blit(self.image, (self.rect.x, self.rect.y))
    
naruto = chel("h4.jpg",0,200)
mesta = [100,200,300,400]
n=0
while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
    wind.fill((50,50,250))
    n +=1 #переменную n = 0 надо создать ДО while!
    if n>15:
        random.shuffle(mesta) #шаффл меняет цифры местами
        naruto.rect.x = mesta[0] #берём первую цифру из перетасованного списка
        n=0
    naruto.put()
    pygame.display.update()
    clock.tick(60)
