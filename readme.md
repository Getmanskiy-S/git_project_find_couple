![menu.png](data%2Fmenu.png)
# КРАТКОЕ ОПИСАНИЕ ПРОГРАММЫ

Программа предназначена для развлечения. 

Ваша задача - подобрать две пары одинаковых карт
за определённое время

Программа представляет собой игру, сделанную на python
В игре используется база данных *users*
В Базе данных содержится две таблицы:
- *users* - содержит id, имя пользователя, количество побед и поражений
- *saves* - содержит id, количество очков, количество пар карточек, сложность и громкость игры

База данных создана в приложении [SQLiteStudio](https://sqlitestudio.pl/)

# ИНСТРУКЦИЯ ПО ИСПОЛЬЗОВАНИЮ

Для запуска программы необходимо запустить файл main.exe

В главном меню есть 4 кнопки:
1. Играть
2. Загрузить сохранение
3. Настройки
4. Выход

Для начала нужно загрузить сохранение, нажав на вторую кнопку.
Для загрузки сохранений сделан интерфейс в [QtDesigner](https://build-system.fman.io/qt-designer-download).

В этой вкладке есть 3 кнопки:
1. Загрузить сохранение по id
2. Загрузить сохранение по имени
3. Создать

Если у вас нет сохранения, нажмите клавишу *Создать*
Если есть, выберите либо 1-ю, либо 2-ю клавишу

Если вы хотя бы один раз сохранились, ваши данные
останутся при следующем запуске игры

После того, как вы сохранились, можно настроить игру,
а можно сразу начать играть.
Для настроек игры сделан интерфейс в [QtDesigner](https://build-system.fman.io/qt-designer-download).

В этой вкладке есть следующие настройки:
1. Сложность
2. Количество пар карточек
3. Громкость

После всего вышеперечисленного, вы можете
начать игру.

Нажмите кнопку *Начать*, и вы запустите игру.

С самого начала время приостановлено. его можно
запустить с помощью кнопки:

![pause.png](data%2Fpause.png)

После этого кнопка изменится:

![play.png](data%2Fplay.png)

Вы можете на неё нажать повторно. Тогда игра
вновь приостановится.

Также есть кнопка настройки музыки:

![sound_on.png](data%2Fsound_on.png)

Вы можнете нажать на неё, и музыка в игре выключится.
Однако звуки игры останутся.

после удаление всех карт или по окончании времени
ваша игра завершается.
При завершении игры в случае победы вам начисляются очки.

Также есть кнопка подсказки.
Нажатие на неё стоит целых 10 000 очков.
Когда вы нажимаете на неё, то все карты открываются
на 1 секунду.

Есть звуковая часть игры. Подробнее о ней
вы можете узнать сами поиграв в игру.

# ГДЕ СКАЧАТЬ?

Скачать игру можно в [репозитории в ветке release_version](https://github.com/Getmanskiy-S/git_project_find_couple/tree/release-version).
Там же можно посмотреть подробнее информацию об создании игры.