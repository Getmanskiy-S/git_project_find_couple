import os
import sys
import sqlite3
import pygame
from random import randrange, choices, shuffle
from math import ceil, sqrt


def load_image(file_name):
    fullname = os.path.join('data', file_name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def draw_image(dr_file_name, dr_x=0, dr_y=0, dr_weight=800, dr_height=200):
    dr_fon = pygame.transform.scale(load_image(dr_file_name), (dr_weight, dr_height))
    screen.blit(dr_fon, (dr_x, dr_y))


def terminate():
    pygame.quit()
    sys.exit()


class Menu(pygame.sprite.Sprite):
    def __init__(self, image):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__()
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class TrueOrFalse(pygame.sprite.Sprite):
    def __init__(self, group, cl_flag=False, cl_x=0, cl_y=0):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.cl_flag = cl_flag
        if self.cl_flag:
            self.image = load_image('right.png')
        else:
            self.image = load_image('wrong.png')
        self.rect = self.image.get_rect()
        self.rect.x = cl_x
        self.rect.y = cl_y


class Button(pygame.sprite.Sprite):
    def __init__(self, group, cl_x=0, cl_y=0, cl_weight=800, cl_height=200):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = pygame.transform.scale(load_image('button.png'), (cl_weight, cl_height))
        self.rect = self.image.get_rect()
        self.rect.x = cl_x
        self.rect.y = cl_y

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            return True
        else:
            return False


class MobileText(pygame.sprite.Sprite):
    def __init__(self, *group, text, text_size=100, cl_x=0, cl_y=0, color='white', outline_color='black',
                 outline_width=3):
        # Вызов конструктора родительского класса Sprite.
        super().__init__(*group)
        self.font = pygame.font.Font(None, text_size)
        self.text = text
        self.color = color
        self.outline_color = outline_color
        self.outline_width = outline_width
        self.x = cl_x
        self.y = cl_y
        self.update()

    def update(self):
        # Создание текста с обводкой
        # Обводка: рисуем текст несколько раз с небольшими смещениями
        outline_surface = pygame.Surface((self.font.size(self.text)[0] + self.outline_width * 2,
                                          self.font.size(self.text)[1] + self.outline_width * 2),
                                         pygame.SRCALPHA)

        for dx in range(-self.outline_width, self.outline_width + 1):
            for dy in range(-self.outline_width, self.outline_width + 1):
                if dx != 0 or dy != 0:  # Не рисуем в центре
                    outline_surface.blit(self.font.render(self.text, True, pygame.Color(self.outline_color)),
                                         (self.outline_width + dx, self.outline_width + dy))

        # Основной текст
        self.string = self.font.render(self.text, True, pygame.Color(self.color))

        # Отрисовка на экран
        screen.blit(outline_surface, (self.x - self.outline_width, self.y - self.outline_width))
        screen.blit(self.string, (self.x, self.y))


class Card(pygame.sprite.Sprite):

    def __init__(self, *group, file_path, cl_x=0, cl_y=0, cl_weight=200, cl_height=200):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.file_path = 'card_empty.png'
        self.image = load_image(self.file_path)
        self.image_card = file_path
        self.image = pygame.transform.scale(self.image, (cl_weight, cl_height))
        self.rect = self.image.get_rect()
        self.rect.x = cl_x
        self.rect.y = cl_y

    def update(self, *args):
        if (args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos) and
                self.file_path == 'card_empty.png' and len(couple) < 2):
            self.file_path = self.image_card
            self.image = load_image(self.file_path)
            couple.append(self)
            if len(couple) == 2:
                pygame.time.set_timer(pygame.USEREVENT, 3000)
                if couple[0].file_path == couple[1].file_path:
                    TrueOrFalse(temporary_sprites, True, couple[0].rect.x, couple[0].rect.y)
                    TrueOrFalse(temporary_sprites, True, couple[1].rect.x, couple[1].rect.y)
                else:
                    TrueOrFalse(temporary_sprites, False, couple[0].rect.x, couple[0].rect.y)
                    TrueOrFalse(temporary_sprites, False, couple[1].rect.x, couple[1].rect.y)


def start_screen():
    menu.image = load_image('menu.png')
    Button(button_sprites, cl_x=100, cl_y=20, cl_height=150)
    Button(button_sprites, cl_x=100, cl_y=180, cl_height=150)
    Button(button_sprites, cl_x=100, cl_y=470, cl_height=150)
    Button(button_sprites, cl_x=100, cl_y=630, cl_height=150)

    MobileText(text_sprites, text='Новая игра', cl_x=300, cl_y=60)
    MobileText(text_sprites, text='Загрузить Сохранение', cl_x=120, cl_y=220)
    MobileText(text_sprites, text='Игра: угадай пару', cl_x=30, cl_y=350, text_size=150,
               color='black', outline_color='white')
    MobileText(text_sprites, text='Настройки', cl_x=325, cl_y=510)
    MobileText(text_sprites, text='Выйти', cl_x=400, cl_y=670)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                i = 0
                for s in button_sprites:
                    if s.update(event):
                        if i == 0:
                            button_sprites.empty()
                            text_sprites.empty()
                            return  # начинаем игру
                        elif i == 1:
                            for ss in text_sprites:
                                ss.x = randrange(1000)
                                ss.y = randrange(800)
                        elif i == 2:
                            pass
                        else:
                            terminate()
                    else:
                        i += 1
        screen.blit(menu.image, menu.rect)
        button_sprites.draw(screen)
        text_sprites.update()
        pygame.display.flip()
        clock.tick(fps)


def load_level():
    menu.image = load_image(f'backgrounds/background{randrange(10)}.png')
    cards_radom = choices(range(50), k=col_cards // 2)
    cards_radom *= 2
    shuffle(cards_radom)
    for i in range(col_cards):
        Card(cards_sprites, file_path=f'cards/card{cards_radom[i]}.png', cl_x=i * 200)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 800
    fps = 60
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    menu = Menu('menu.png')
    button_sprites = pygame.sprite.Group()
    cards_sprites = pygame.sprite.Group()
    text_sprites = pygame.sprite.Group()
    temporary_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    player_id = 0
    start_screen()

    # Подключение к БД
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    name, col_victory, col_defeat = cur.execute("""SELECT name, col_victory, col_defeat
     FROM users WHERE id = ?""", (player_id,)).fetchone()
    score, col_hint, col_cards = cur.execute("""SELECT score, col_hint, col_cards FROM saves 
    WHERE id = ?""", (player_id,)).fetchone()

    # введение переменных
    couple = []  # пара карточек

    # цикл уровня
    load_level()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                cards_sprites.update(event)
                x, y = event.pos
            if event.type == pygame.USEREVENT and couple:
                for s in temporary_sprites:
                    if s.cl_flag:
                        couple[0].kill()
                        couple[1].kill()
                        break
                temporary_sprites.empty()
                couple[0].file_path = 'card_empty.png'
                couple[0].image = load_image(couple[0].file_path)
                couple[1].file_path = 'card_empty.png'
                couple[1].image = load_image(couple[1].file_path)
                couple = []
        screen.blit(menu.image, menu.rect)
        button_sprites.draw(screen)
        text_sprites.update()
        cards_sprites.draw(screen)
        temporary_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
    con.close()
