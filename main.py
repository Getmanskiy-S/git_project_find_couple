import os
import sys
import pygame


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Menu(pygame.sprite.Sprite):
    image = load_image("background_menu.png")

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Menu.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    menu_sprites = pygame.sprite.Group()
    Menu(menu_sprites)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
        menu_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
