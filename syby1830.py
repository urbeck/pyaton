from pygame import*
okno = display.set_mode((600,400)) #создание окна
display.set_caption("коунтер-майнбравлокс")#название окна (по желанию)

fon = image.load('pngtree.jpg')

game = True #переменная для работы игры
############### игровой цикл:
while game: #игра работает, пока game не равен False
    for i in event.get(): #перебор событий
        if i.type == QUIT: #нажатие на крестик
            game = False # выключить игру
    #okno.fill((255,255,0))
    okno.blit(fon, (0,0))

    display.update() # всегда последняя команда цикла - обновить экран
