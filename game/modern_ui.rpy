# coding: utf-8

# --- Современный интерфейс для Ren'Py 8.x ---
# Этот файл полностью заменяет стандартное главное меню и навигацию,
# добавляя современный дизайн и экран выбора языка.

# --- Шаг 1: Настройка стилей (легко редактировать) ---
# Здесь вы можете изменить цвета, шрифты, размеры и другие параметры интерфейса.

style main_menu_frame:
    # Фон главного меню. Замените "gui/main_menu.png" на путь к вашему изображению.
    background "gui/main_menu.png"
    # Если у вас нет изображения, можно использовать сплошной цвет:
    # background Color("#000b1c")

style main_menu_vbox:
    # Контейнер для кнопок меню.
    xalign 0.08  # Смещение по горизонтали (0.0 - лево, 1.0 - право)
    yalign 0.5   # Смещение по вертикали (0.5 - центр)
    spacing 15   # Расстояние между кнопками

style main_menu_textbutton is button:
    # Стиль для кнопок в главном меню.
    properties gui.button_properties("main_menu_button")
    size_group "main_menu"

style main_menu_text is text:
    # Стиль текста кнопок.
    properties gui.text_properties("main_menu", accent=True)
    # Вы можете задать свой шрифт и размер:
    # font "MyCoolFont.ttf"
    # size 30


# --- Шаг 2: Инициализация языка и интеграция в меню настроек ---

# Используем `init` с низким приоритетом, чтобы код выполнился после стандартных настроек.
init -2 python:
    # Определяем доступные языки как обычную переменную.
    store.available_languages = [
        ("English", None),
        ("Русский", "russian")
    ]
    # Словарь для отображения названия текущего языка в меню настроек.
    language_names = {identifier: name for name, identifier in store.available_languages}

    # Добавляем опцию "Язык" в стандартный экран настроек (современный способ для 8.x).
    config.preferences.add(
        _("Language"),
        language_names.get(persistent.language, "English"),
        ShowMenu("language_screen")
    )


# --- Шаг 3: Определение экранов ---

# Экран главного меню. Тег `main_menu` заставляет Ren'Py использовать этот экран
# вместо стандартного.
screen main_menu():
    tag menu

    # Добавляем стилизованный фрейм (фон).
    add "gui/main_menu.png" # Замените на путь к вашему фону

    # Контейнер для кнопок навигации.
    vbox:
        style "main_menu_vbox"

        # Кнопки меню.
        textbutton _("New Game") action Start() style "main_menu_textbutton"

        # Кнопка "Продолжить" будет активна только если есть что продолжать.
        textbutton _("Continue") action Continue() sensitive If(renpy.can_continue()) style "main_menu_textbutton"

        textbutton _("Load") action ShowMenu("load") style "main_menu_textbutton"
        textbutton _("Preferences") action ShowMenu("preferences") style "main_menu_textbutton"
        textbutton _("Quit") action Quit(confirm=True) style "main_menu_textbutton"


# Экран выбора языка.
screen language_screen():
    tag menu
    # Используем стандартный шаблон для единообразия с другими меню (настройки, сохранения).
    use game_menu(_("Language"), scroll="viewport"):
        vbox:
            style "menu_vbox"
            xalign 0.5
            yalign 0.5

            # Кнопки для каждого языка.
            for name, identifier in store.available_languages:
                textbutton name:
                    style "menu_textbutton"
                    action Language(identifier)
                    # Подсвечиваем текущий язык.
                    selected (persistent.language == identifier)

            # Кнопка для возврата в меню настроек.
            textbutton _("Return"):
                style "menu_textbutton"
                action Return()


# --- Шаг 4: Перевод всех строк интерфейса на русский ---

translate russian strings:
    # Главное меню
    old "New Game"
    new "Новая игра"

    old "Continue"
    new "Продолжить"

    old "Load"
    new "Загрузить"

    old "Preferences"
    new "Настройки"

    old "Quit"
    new "Выход"

    # Экран выбора языка
    old "Language"
    new "Язык"

    old "Return"
    new "Возврат"

    old "English"
    new "English"

    old "Русский"
    new "Русский"


# --- Шаг 5: Инициализация переменной языка ---
# Устанавливаем язык по умолчанию при первом запуске, чтобы избежать ошибок.
default persistent.language = None
