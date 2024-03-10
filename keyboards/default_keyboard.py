from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# начальные кнопки
main_buttons_list = [
    [
        KeyboardButton(text='Мобильное приложение'),
        KeyboardButton(text='Ассортимент'),
        KeyboardButton(text='Доставка'),
        KeyboardButton(text='Адреса'),
        KeyboardButton(text='Работа у нас')
    ]
]
main_buttons = ReplyKeyboardMarkup(keyboard=main_buttons_list, resize_keyboard=True)

# мобильное приложение кнопки
buttons_mobile_app_list = [
    [
        KeyboardButton(text='Где скачать?'),
        KeyboardButton(text='Как пользоваться?'),
        KeyboardButton(text='Система лояльности')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_mobile_app = ReplyKeyboardMarkup(keyboard=buttons_mobile_app_list, resize_keyboard=True)


# кнопки мобильное приложение → где скачать?
buttons_mobile_app_where_download_list = [
    [
        KeyboardButton(text='Google play'),
        KeyboardButton(text='App store'),
        KeyboardButton(text='App gallery')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_mobile_app_where_download = ReplyKeyboardMarkup(keyboard=buttons_mobile_app_where_download_list, resize_keyboard=True)

# кнопки мобильное приложение → система лояльности
buttons_mobile_app_loyalty_system_list = [
    [
        KeyboardButton(text='Что такое система лояльности?'),
        KeyboardButton(text='Кто такой тайный гость?'),
        KeyboardButton(text='Бонусные баллы')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_mobile_app_loyalty_system = ReplyKeyboardMarkup(keyboard=buttons_mobile_app_loyalty_system_list, resize_keyboard=True)

# ассортимент кнопки
buttons_assortment_list = [
    [
        KeyboardButton(text='Новинки'),
        KeyboardButton(text='Популярное'),
        KeyboardButton(text='Быстроприготовимое'),
        KeyboardButton(text='Меню'),
        KeyboardButton(text='Мерч')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_assortment = ReplyKeyboardMarkup(keyboard=buttons_assortment_list, resize_keyboard=True)

# кнопки ассортимент → новинки
buttons_new_products_list = [
    [
        KeyboardButton(text='Молочный ломтик')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_new_products = ReplyKeyboardMarkup(keyboard=buttons_new_products_list, resize_keyboard=True)

# кнопки ассортимент → популярное
buttons_popular_list = [
    [
        KeyboardButton(text='Облепиха-имбирь')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_popular = ReplyKeyboardMarkup(keyboard=buttons_popular_list, resize_keyboard=True)

# кнопки ассортимент → быстроприготовимое
buttons_quick_to_prepare_list = [
    [
        KeyboardButton(text='Круассан с ветчиной')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_quick_to_prepare = ReplyKeyboardMarkup(keyboard=buttons_quick_to_prepare_list, resize_keyboard=True)

# кнопки ассортимент → меню
buttons_menu_list = [
    [
        KeyboardButton(text='Горячие напитки'),
        KeyboardButton(text='Холодные напитки'),
        KeyboardButton(text='Сэндвичи'),
        KeyboardButton(text='Слойки'),
        KeyboardButton(text='Пироги'),
        KeyboardButton(text='Выпечка'),
        KeyboardButton(text='Пирожные'),
        KeyboardButton(text='Торты'),
        KeyboardButton(text='Хлеб'),
        KeyboardButton(text='Печенье'),
        KeyboardButton(text='Азия'),
        KeyboardButton(text='Кулинария')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_menu = ReplyKeyboardMarkup(keyboard=buttons_menu_list, resize_keyboard=True)

# доставка кнопки
buttons_delivery_list = [
    [
        KeyboardButton(text='Как заказать?'),
        KeyboardButton(text='Как оплатить?'),
        KeyboardButton(text='Время доставки')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_delivery = ReplyKeyboardMarkup(keyboard=buttons_delivery_list, resize_keyboard=True)

# адреса кнопки
buttons_addresses_list = [
    [
        KeyboardButton(text='Самая близкая пекарня к Вам', request_location=True),
        KeyboardButton(text='Список пекарен')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_addresses = ReplyKeyboardMarkup(keyboard=buttons_addresses_list, resize_keyboard=True)

# кнопки адреса → список пекарен
buttons_list_bakeries_list = [
    [
        KeyboardButton(text='Санкт-Петербург')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_list_bakeries = ReplyKeyboardMarkup(keyboard=buttons_list_bakeries_list, resize_keyboard=True)

# работа у нас кнопки
buttons_work_list = [
    [
        KeyboardButton(text='Управляющий'),
        KeyboardButton(text='Пекарь-повар'),
        KeyboardButton(text='Продавец-кассир')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_work = ReplyKeyboardMarkup(keyboard=buttons_work_list, resize_keyboard=True)
