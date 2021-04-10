import pygame
import random
clock = pygame.time.Clock()
wind = pygame.display.set_mode((600, 500))
game = True
#переменная всего одна, т.к. карт кроме места различий нет
class karta(pygame.sprite.Sprite):
    def __init__(self, x): 
        super().__init__()
        self.image = pygame.Surface((90,140)) #размер карточки
        self.image.fill((200,200,10))
        self.rect = self.image.get_rect()
        self.rect.x = x
    def put(self):
        wind.blit(self.image, (self.rect.x, 200))

pygame.font.init()
class goal(pygame.sprite.Sprite):
    def __init__(self, x): 
        super().__init__()
        self.image = pygame.font.SysFont('verdana', 25).render("ЖМИ", True, (0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
    def put(self):
        wind.blit(self.image, (self.rect.x+13, 260))


mesta = [100,200,300,400] #четыре положения карты - в списке
asd = karta(100)
sdf = goal(100)
n=0
while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
    wind.fill((50,50,250))
    asd.put()
    sdf.put()
    n +=1 #переменную n = 0 надо создать ДО while!
    if n>15:
        random.shuffle(mesta) #шаффл меняет цифры местами
        asd.rect.x = mesta[0] #берём первую цифру из перетасованного списка
        sdf.rect.x = mesta[0]
        n=0
    #задержка на экране
    pygame.display.update()
    clock.tick(60)