import pygame as pg
#pygame初始化
pg.init()

#設定視窗
width, height = 640, 480                      
screen = pg.display.set_mode((width, height)) 
pg.display.set_caption("Sean's game")        

#建立畫布bg
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255,255,255))           #白色
#顯示
screen.blit(bg, (0,0))
pg.display.update()

#關閉程式的程式碼
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit() 
