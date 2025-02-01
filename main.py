import os
import sys
import sqlite3
import pygame
from random import randrange, shuffle
from math import ceil, sqrt
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox, QTableWidgetItem
from settings import Ui_MainWindow
from uploading_save import Ui_MainWindow2

try:
    def load_image(file_name):
        fullname = os.path.join('data', file_name)
        image = pygame.image.load(fullname)
        return image


    def draw_image(dr_file_name, dr_x=0, dr_y=0, dr_weight=800, dr_height=200):
        dr_fon = pygame.transform.scale(load_image(dr_file_name), (dr_weight, dr_height))
        screen.blit(dr_fon, (dr_x, dr_y))


    def except_hook(cls, exception, traceback):
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка в интерфейсе")
        msg.setText(f"Произошла непредвиденная ошибка: {exception} в интерфейсе. Приносим Извинения!")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.button(QMessageBox.StandardButton.Ok)
        msg.exec()
        # sys.__excepthook__(cls, exception, traceback)


    def terminate():
        pygame.quit()
        sys.exit()


    class Settings(QMainWindow, Ui_MainWindow):
        def __init__(self):
            super().__init__()
            # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
            # остальное без изменений
            self.setupUi(self)
            if difficulty == 1:
                self.rb_easy.setChecked(True)
            elif difficulty == 2:
                self.rb_normal.setChecked(True)
            else:
                self.rb_hard.setChecked(True)
            self.cards_slider.setValue(col_couples_cards)
            self.cards_spinbox.setValue(col_couples_cards)
            self.volume_slider.setValue(volume)
            self.volume_spinbox.setValue(volume)
            self.cards_slider.valueChanged.connect(self.change_cards)
            self.cards_spinbox.valueChanged.connect(self.change_cards)
            self.volume_slider.valueChanged.connect(self.change_volume)
            self.volume_spinbox.valueChanged.connect(self.change_volume)
            self.save_btn.clicked.connect(self.save_result)

        def run(self):
            self.label.setText("OK")

        def change_cards(self):
            if self.sender().objectName() == 'cards_slider':
                self.cards_spinbox.setValue(self.cards_slider.value())
            else:
                self.cards_slider.setValue(self.cards_spinbox.value())

        def change_volume(self):
            if self.sender().objectName() == 'volume_slider':
                self.volume_spinbox.setValue(self.volume_slider.value())
            else:
                self.volume_slider.setValue(self.volume_spinbox.value())

        def save_result(self):
            global volume, difficulty, col_couples_cards
            self.save_btn.setEnabled(False)
            volume = self.volume_slider.value()
            name_btn = self.buttonGroup.checkedButton().objectName()
            col_couples_cards = self.cards_slider.value()
            if name_btn == 'rb_easy':
                difficulty = 1
            elif name_btn == 'rb_normal':
                difficulty = 2
            else:
                difficulty = 3

            # сохранение данных в БД
            cur = con.cursor()
            cur.execute('''UPDATE saves SET volume = ?, difficulty = ?, col_couples_cards = ? WHERE id = ?''',
                        (volume, difficulty, col_couples_cards, player_id))
            con.commit()
            cur.close()
            self.close()

        def closeEvent(self, event):
            name_btn = self.buttonGroup.checkedButton().objectName()
            if name_btn == 'rb_easy':
                difficulty2 = 1
            elif name_btn == 'rb_normal':
                difficulty2 = 2
            else:
                difficulty2 = 3
            if (self.volume_slider.value() != volume or difficulty2 != difficulty or
                    col_couples_cards != self.cards_slider.value()):
                msg = QMessageBox()
                msg.setWindowTitle("Вопрос")
                msg.setText("У вас есть изменения в параметрах. Вы хотите их сохранить?")
                msg.setIcon(QMessageBox.Icon.Question)
                msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                msg.button(QMessageBox.StandardButton.Yes).setText("Да")
                msg.button(QMessageBox.StandardButton.No).setText("Нет")

                # Отображение окна и получение результата
                result = msg.exec()

                # Обработка нажатия кнопок
                if result == QMessageBox.StandardButton.Yes:
                    self.save_result()
            event.accept()


    class UploadingSave(QMainWindow, Ui_MainWindow2):
        def __init__(self):
            super().__init__()
            # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
            # остальное без изменений
            self.setupUi(self)
            self.update()
            self.btn_create.clicked.connect(self.create_account)
            self.btn_id.clicked.connect(self.load_account_id)
            self.btn_name.clicked.connect(self.load_account_name)

        def create_account(self):
            global player_id
            # сохранение данных в БД
            cur = con.cursor()
            name1, ok_pressed = QInputDialog.getText(self, "Запрос данных",
                                                     "Введите ваше игровое имя")
            if ok_pressed:
                player_id = cur.execute('''SELECT id FROM users''').fetchall()
                player_id = player_id[-1][0] + 1
                cur.execute('''INSERT INTO users(id,name) VALUES(?, ?)''',
                            (player_id, name1))
                cur.execute('''INSERT INTO saves(id) VALUES(?)''',
                            (player_id,))
                con.commit()
                self.update()
                cur.close()

        def load_account_id(self):
            global col_victory, col_defeat, score, col_couples_cards, difficulty, volume, player_id
            # сохранение данных в БД
            idd, ok_pressed = QInputDialog.getInt(self, "Запрос данных",
                                                  "Введите id пользователя")
            player_id = idd
            if ok_pressed:
                cur = con.cursor()
                col_victory, col_defeat = cur.execute('''SELECT 
                col_victory, col_defeat FROM users WHERE id = ?''', (idd,)).fetchone()
                score, col_couples_cards, difficulty, volume = cur.execute('''SELECT 
                score, col_couples_cards, difficulty, volume 
                FROM saves WHERE id = ?''', (idd,)).fetchone()
                self.update()
                cur.close()

        def load_account_name(self):
            global col_victory, col_defeat, score, col_couples_cards, difficulty, volume, player_id
            # сохранение данных в БД
            name1, ok_pressed = QInputDialog.getText(self, "Запрос данных",
                                                     "Введите имя пользователя")
            if ok_pressed:
                cur = con.cursor()
                idd = cur.execute('SELECT id FROM users WHERE name = ?', (name1,)).fetchone()
                idd = idd[0]
                player_id = idd
                col_victory, col_defeat = cur.execute('''SELECT 
                        col_victory, col_defeat FROM users WHERE id = ?''', (idd,)).fetchone()
                score, col_couples_cards, difficulty, volume = cur.execute('''SELECT 
                        score, col_couples_cards, difficulty, volume 
                        FROM saves WHERE id = ?''', (idd,)).fetchone()
                print(col_victory, col_defeat, score, col_couples_cards, difficulty, volume, player_id)
                self.update()
                cur.close()

        def update(self):
            cur = con.cursor()
            res = cur.execute('SELECT users.id, users.name, saves.score, users.col_victory, users.col_defeat '
                              'FROM users INNER JOIN saves ON saves.id = users.id').fetchall()
            # Заполним размеры таблицы
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setRowCount(0)
            self.tableWidget.setHorizontalHeaderLabels(['id', 'имя', 'очки', 'кол-во побед', 'кол-во поражений'])
            # Заполняем таблицу элементами
            for i, row in enumerate(res):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(str(elem)))
            self.tableWidget.resizeColumnsToContents()


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
        def __init__(self, group, cl_flag=False, cl_x=0, cl_y=0, cl_weight=200, cl_height=200):
            # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
            # Это очень важно !!!
            super().__init__(group)
            self.cl_flag = cl_flag
            if self.cl_flag:
                self.image = pygame.transform.scale(load_image('right.png'), (cl_weight, cl_height))
            else:
                self.image = pygame.transform.scale(load_image('wrong.png'), (cl_weight, cl_height))
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


    class ImageButton(pygame.sprite.Sprite):
        def __init__(self, group, image1, image2, cl_x=0, cl_y=0, cl_weight=800, cl_height=200):
            # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
            # Это очень важно !!!
            super().__init__(group)
            self.image1 = image1
            self.image2 = image2
            self.file_path = self.image1
            self.cl_weight = cl_weight
            self.cl_height = cl_height
            self.image = pygame.transform.scale(load_image(self.file_path), (self.cl_weight, self.cl_height))
            self.rect = self.image.get_rect()
            self.rect.x = cl_x
            self.rect.y = cl_y

        def update(self, *args):
            if (args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos) and
                    not (is_timer and self.image1 != 'sound_on.png')):
                if self.file_path == self.image1:
                    self.file_path = self.image2
                else:
                    self.file_path = self.image1
                self.image = pygame.transform.scale(load_image(self.file_path), (self.cl_weight, self.cl_height))
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
            self.image_card = file_path
            self.cl_weight = cl_weight
            self.cl_height = cl_height
            self.image = pygame.transform.scale(load_image(self.file_path), (self.cl_weight, self.cl_height))
            self.rect = self.image.get_rect()
            self.rect.x = cl_x
            self.rect.y = cl_y

        def update(self, *args):
            global is_timer, is_stop
            if (args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos) and
                    self.file_path == 'card_empty.png' and not is_timer and not is_stop):
                self.file_path = self.image_card
                self.image = pygame.transform.scale(load_image(self.file_path), (self.cl_weight, self.cl_height))
                couple.append(self)
                if len(couple) == 2:
                    is_timer = True
                    if difficulty == 1:
                        koef = 2000
                    elif difficulty == 2:
                        koef = 1000
                    else:
                        koef = 500
                    if couple[0].file_path == couple[1].file_path:
                        pygame.time.set_timer(pygame.USEREVENT, koef // 2)
                        TrueOrFalse(temporary_sprites, True, couple[0].rect.x, couple[0].rect.y,
                                    self.cl_weight, self.cl_height)
                        TrueOrFalse(temporary_sprites, True, couple[1].rect.x, couple[1].rect.y,
                                    self.cl_weight, self.cl_height)
                    else:
                        pygame.time.set_timer(pygame.USEREVENT, koef)
                        TrueOrFalse(temporary_sprites, False, couple[0].rect.x, couple[0].rect.y,
                                    self.cl_weight, self.cl_height)
                        TrueOrFalse(temporary_sprites, False, couple[1].rect.x, couple[1].rect.y,
                                    self.cl_weight, self.cl_height)


    def start_screen():
        menu.image = load_image('menu.png')
        Button(button_sprites, cl_x=100, cl_y=20, cl_height=150)
        Button(button_sprites, cl_x=100, cl_y=180, cl_height=150)
        Button(button_sprites, cl_x=100, cl_y=470, cl_height=150)
        Button(button_sprites, cl_x=100, cl_y=630, cl_height=150)

        MobileText(text_sprites, text='Играть', cl_x=400, cl_y=60)
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
                            if i == 0 and player_id != -1:
                                button_sprites.empty()
                                text_sprites.empty()
                                return  # начинаем игру
                            elif i == 1:
                                ex = UploadingSave()
                                ex.show()
                                app.exec()
                            elif i == 2 and player_id != -1:
                                ex = Settings()
                                ex.show()
                                app.exec()
                            elif i == 3:
                                terminate()
                            else:
                                msg = QMessageBox()
                                msg.setWindowTitle("Ошибка")
                                msg.setText("Вы не загрузили данные")
                                msg.setIcon(QMessageBox.Icon.Warning)
                                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                                msg.button(QMessageBox.StandardButton.Ok)
                                msg.exec()
                        else:
                            i += 1
            screen.blit(menu.image, menu.rect)
            button_sprites.draw(screen)
            text_sprites.update()
            pygame.display.flip()
            clock.tick(fps)


    def load_level():
        global couple, is_timer, is_stop, seconds_left
        pygame.time.set_timer(pygame.USEREVENT + 1, 100)  # таймер, срабатывающий раз в 100 милисекунд
        button_sprites.empty()
        cards_sprites.empty()
        text_sprites.empty()
        temporary_sprites.empty()
        couple = []
        is_timer = False
        is_stop = True
        if difficulty == 1:
            seconds_left = col_couples_cards * 20
        elif difficulty == 2:
            seconds_left = col_couples_cards * 15
        else:
            seconds_left = col_couples_cards * 10
        seconds_left += 100 * (col_couples_cards // 5)
        menu.image = load_image(f'backgrounds/background{randrange(10)}.png')
        Button(button_sprites, 730, 20, 240, 120)
        MobileText(text_sprites, text='Подсказка (-10 тыс.)', text_size=30, cl_x=750, cl_y=70, outline_width=2)
        ImageButton(button_sprites, 'sound_on.png', 'sound_off.png', cl_x=730, cl_y=150, cl_weight=240, cl_height=240)
        ImageButton(button_sprites, 'pause.png', 'play.png', cl_x=750, cl_y=400, cl_weight=240, cl_height=240)
        important_sprites.append(MobileText(text_sprites, text=f'Осталось времени: {seconds_left // 600} мин. '
                                                               f'{seconds_left % 600 // 10} сек.',
                                            text_size=30, cl_x=20, cl_y=750, outline_width=2))
        important_sprites.append(MobileText(text_sprites, text=f'Кол-во очков: {score}',
                                            text_size=30, cl_x=420, cl_y=750, outline_width=2))

        cards_radom = list(range(50))
        shuffle(cards_radom)
        cards_radom = cards_radom[:col_couples_cards]
        cards_radom *= 2
        shuffle(cards_radom)
        card_a = 700 // ceil(sqrt(col_couples_cards * 2))
        for card_y in range(20, card_a * ceil(sqrt(col_couples_cards * 2)) + 20, card_a):
            for card_x in range(20, card_a * ceil(sqrt(col_couples_cards * 2)) + 20, card_a):
                if cards_radom:
                    card = cards_radom.pop()
                    Card(cards_sprites, file_path=f'cards/card{card}.png', cl_x=card_x, cl_y=card_y, cl_weight=card_a,
                         cl_height=card_a)
                else:
                    break
            if not cards_radom:
                break


    def end_screen():
        global seconds_left, col_victory, col_defeat, important_sprites, score
        pygame.time.set_timer(pygame.USEREVENT + 1, 0)
        button_sprites.empty()
        cards_sprites.empty()
        text_sprites.empty()
        temporary_sprites.empty()
        koef = 1
        if difficulty == 2:
            koef = 1.2
        elif difficulty == 3:
            koef = 1.5
        if seconds_left < 0:
            seconds_left = 0
        if seconds_left == 0:
            MobileText(text_sprites, text='Вы проиграли', cl_x=150, cl_y=50, text_size=150,
                       color='black', outline_color='white')
            col_defeat += 1
        else:
            score += (col_couples_cards * 2) ** 2
            MobileText(text_sprites, text='Вы выиграли!', cl_x=150, cl_y=50, text_size=150,
                       color='black', outline_color='white', outline_width=5)
            MobileText(text_sprites, text=f'(добавлено {ceil((col_couples_cards * 2) ** 2 * koef)} очков)',
                       cl_x=100, cl_y=300)
            col_victory += 1
        MobileText(text_sprites, text=f'У вас {col_victory} побед. и {col_defeat} поражен.', text_size=30, cl_x=150,
                   cl_y=770, outline_width=2)
        important_sprites.append(MobileText(text_sprites, text=f'Осталось времени: {seconds_left // 600} мин. '
                                                               f'{seconds_left % 600 // 10} сек.',
                                            text_size=30, cl_x=550, cl_y=770, outline_width=2))
        important_sprites.append(MobileText(text_sprites, text=f'Кол-во очков: {score}',
                                            text_size=100, cl_x=150, cl_y=200, outline_width=3))
        Button(button_sprites, cl_x=100, cl_y=400, cl_height=150)
        MobileText(text_sprites, text='Вернуться в меню', cl_x=200, cl_y=440)
        Button(button_sprites, cl_x=100, cl_y=600, cl_height=150)
        MobileText(text_sprites, text='Выйти', cl_x=400, cl_y=640)

        # сохранение данных в БД
        cur = con.cursor()
        cur.execute('''UPDATE saves SET score = ? WHERE id = ?''',
                    (score, player_id))
        cur.execute('''UPDATE users SET col_victory = ?, col_defeat = ? WHERE id = ?''',
                    (col_victory, col_defeat, player_id))
        con.commit()
        cur.close()

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
                                important_sprites = []
                                return  # начинаем игру
                            else:
                                terminate()
                        else:
                            i += 1
            screen.blit(menu.image, menu.rect)
            button_sprites.draw(screen)
            text_sprites.update()
            pygame.display.flip()
            clock.tick(fps)


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

        # введение переменных
        sys.excepthook = except_hook
        player_id = -1  # id игрока
        seconds_left = 500  # время до поражения, 1 seconds_left = 100 милисекунд
        important_sprites = []  # спрайт с таймером и с счётчиком очков
        couple = []  # пара карточек
        is_timer = False  # запущен ли таймер
        is_stop = True  # остановлено ли время
        app = QApplication(sys.argv)
        con = sqlite3.connect("users.db")

        start_screen()

        # Подключение к БД
        cur1 = con.cursor()
        name, col_victory, col_defeat = cur1.execute("""SELECT 
        name, col_victory, col_defeat 
        FROM users WHERE id = ?""", (player_id,)).fetchone()
        volume, difficulty, score, col_couples_cards = cur1.execute("""SELECT 
        volume, difficulty, score, col_couples_cards 
        FROM saves WHERE id = ?""", (player_id,)).fetchone()
        cur1.close()

        # цикл уровня и меню
        load_level()
        running = True
        while running:
            for event1 in pygame.event.get():
                if event1.type == pygame.QUIT:
                    running = False
                if event1.type == pygame.MOUSEBUTTONDOWN:
                    cards_sprites.update(event1)
                    i1 = 0
                    for s1 in button_sprites:
                        if s1.update(event1):
                            if i1 == 0:
                                if score >= 10000:
                                    pygame.time.set_timer(pygame.USEREVENT + 2, 1000)
                                    score -= 10000
                                    cur = con.cursor()
                                    cur.execute('''UPDATE saves SET score = ? WHERE id = ?''',
                                                (score, player_id))
                                    con.commit()
                                    cur.close()
                                    for s3 in cards_sprites:
                                        s3.file_path = s3.image_card
                                        s3.image = pygame.transform.scale(load_image(s3.file_path),
                                                                          (s3.cl_weight, s3.cl_height))
                                else:
                                    msg1 = QMessageBox()
                                    msg1.setWindowTitle("Ошибка")
                                    msg1.setText(f"Недостаточно средств")
                                    msg1.setIcon(QMessageBox.Icon.Question)
                                    msg1.setStandardButtons(QMessageBox.StandardButton.Ok)
                                    msg1.button(QMessageBox.StandardButton.Ok)
                                    msg1.exec()
                                    break
                            elif i1 == 1:
                                pass
                            else:
                                if s1.file_path == s1.image1:
                                    is_stop = True
                                else:
                                    is_stop = False
                                break
                        else:
                            i1 += 1
                if event1.type == pygame.USEREVENT:
                    pygame.time.set_timer(pygame.USEREVENT, 0)
                    for s2 in temporary_sprites:
                        if s2.cl_flag:
                            temporary_sprites.empty()
                            couple[0].kill()
                            couple[1].kill()
                            couple = []
                            break
                    if len(couple) == 2:
                        temporary_sprites.empty()
                        couple[0].file_path = 'card_empty.png'
                        couple[0].image = pygame.transform.scale(load_image(couple[0].file_path),
                                                                 (couple[0].cl_weight, couple[0].cl_height))
                        couple[1].file_path = 'card_empty.png'
                        couple[1].image = pygame.transform.scale(load_image(couple[1].file_path),
                                                                 (couple[1].cl_weight, couple[1].cl_height))
                        couple = []
                    is_timer = False
                if event1.type == pygame.USEREVENT + 1 and not is_timer and not is_stop:
                    seconds_left -= 1
                    if seconds_left > 0:
                        important_sprites[0].text = (f'Осталось времени: '
                                                     f'{seconds_left // 600} мин. {seconds_left % 600 // 10} сек.')
                    else:
                        end_screen()
                        start_screen()
                        load_level()
                if event1.type == pygame.USEREVENT + 2 and not is_timer and not is_stop:
                    for s3 in cards_sprites:
                        pygame.time.set_timer(pygame.USEREVENT + 2, 0)
                        s3.file_path = 'card_empty.png'
                        s3.image = pygame.transform.scale(load_image(s3.file_path),
                                                            (s3.cl_weight, s3.cl_height))
            if not cards_sprites:
                end_screen()
                start_screen()
                load_level()
            screen.blit(menu.image, menu.rect)
            button_sprites.draw(screen)
            text_sprites.update()
            cards_sprites.draw(screen)
            temporary_sprites.draw(screen)
            pygame.display.flip()
            clock.tick(fps)
        pygame.quit()
        con.close()
except Exception:
    msg1 = QMessageBox()
    msg1.setWindowTitle("Неизвестная ошибка")
    msg1.setText(f"Произошла непредвиденная ошибка. Приносим Извинения!")
    msg1.setIcon(QMessageBox.Icon.Warning)
    msg1.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg1.button(QMessageBox.StandardButton.Ok)
    msg1.exec()
