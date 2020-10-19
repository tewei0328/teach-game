import sys, time
import random

import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT, USEREVENT

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
IMAGEWIDTH = 300
IMAGEHEIGHT = 200
FPS = 60

def get_random_position(widow_width, window_height, image_width, image_height):
    random_x = random.randint(image_width, widow_width - image_width)
    random_y = random.randint(image_height, window_height - image_height)

    return random_x, random_y


# init mosquito random position
class Mosquito(pygame.sprite.Sprite):
    def __init__(self, width, height, random_x, random_y, widow_width, window_height):
        super().__init__()
        self.raw_image = pygame.image.load('./mosquito.png').convert_alpha()
        self.image = pygame.transform.scale(self.raw_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (random_x, random_y)
        self.width = width
        self.height = height
        self.widow_width = widow_width
        self.window_height = window_height

def main():
    pygame.init()

    # load window surface
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Mosquito War')
    random_x, random_y = get_random_position(WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEHEIGHT)
    mosquito = Mosquito(IMAGEWIDTH, IMAGEHEIGHT, random_x, random_y, WINDOW_WIDTH, WINDOW_HEIGHT)
    reload_mosquito_event = USEREVENT + 1
    pygame.time.set_timer(reload_mosquito_event, 300)
    points = 0
    my_font = pygame.font.SysFont(None, 30)
    my_hit_font = pygame.font.SysFont(None, 40)
    hit_text_surface = None
    main_clock = pygame.time.Clock()

    while True:
        # 偵測事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == reload_mosquito_event:
                # 偵測到重新整理事件，固定時間移除蚊子，換新位置
                mosquito.kill()
                # 蚊子新位置
                random_x, random_y = get_random_position(WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEHEIGHT)
                mosquito = Mosquito(IMAGEWIDTH, IMAGEHEIGHT, random_x, random_y, WINDOW_WIDTH, WINDOW_HEIGHT)
            elif event.type == MOUSEBUTTONDOWN:
                # 當使用者點擊滑鼠時，檢查是否滑鼠位置 x, y 有在蚊子圖片上
                if random_x < pygame.mouse.get_pos()[0] < random_x + IMAGEWIDTH and random_y < pygame.mouse.get_pos()[1] < random_y + IMAGEHEIGHT:
                    mosquito.kill()
                    random_x, random_y = get_random_position(WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEHEIGHT)
                    mosquito = Mosquito(IMAGEWIDTH, IMAGEHEIGHT, random_x, random_y, WINDOW_WIDTH, WINDOW_HEIGHT)
                    hit_text_surface = my_hit_font.render('Hit!!', True, (0, 0, 0))
                    points += 5

        # 背景顏色，清除畫面
        window_surface.fill(WHITE)

        # 遊戲分數儀表板
        text_surface = my_font.render('Points: {}'.format(points), True, (0, 0, 0))
        # 渲染物件
        window_surface.blit(mosquito.image, mosquito.rect)
        window_surface.blit(text_surface, (10, 0))

        # 顯示打中提示文字
        if hit_text_surface:
            window_surface.blit(hit_text_surface, (10, 10))
            hit_text_surface = None

        pygame.display.update()
        # 控制遊戲迴圈迭代速率
        main_clock.tick(FPS)

if __name__ == '__main__':    
    main()
