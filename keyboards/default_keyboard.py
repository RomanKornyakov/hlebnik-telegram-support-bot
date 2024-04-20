from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# начальные кнопки
main_buttons_list = [
    [
        KeyboardButton(text='Заказ'),
        KeyboardButton(text='Мобильное приложение')
    ],
    [
        KeyboardButton(text='Ассортимент'),
        KeyboardButton(text='Доставка'),
        KeyboardButton(text='Адреса')
    ],
    [
        KeyboardButton(text='Подписка'),
        KeyboardButton(text='Купоны'),
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
        KeyboardButton(text='Популярное')
    ],
    [
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
        KeyboardButton(text='Пироги'),
        KeyboardButton(text='Хлеб'),
        KeyboardButton(text='Печенье'),
        KeyboardButton(text='Кулинария')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_menu = ReplyKeyboardMarkup(keyboard=buttons_menu_list, resize_keyboard=True)

# кнопки ассортимент → меню → кулинария
buttons_cookery_list = [
    [
        KeyboardButton(text='Онигири с цыпленком терияки')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_cookery = ReplyKeyboardMarkup(keyboard=buttons_cookery_list, resize_keyboard=True)

# кнопки ассортимент → меню → хлеб
buttons_bread_list = [
    [
        KeyboardButton(text='Багет французский')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_bread = ReplyKeyboardMarkup(keyboard=buttons_bread_list, resize_keyboard=True)

# кнопки ассортимент → меню → печенье
buttons_cookies_list = [
    [
        KeyboardButton(text='Орешки с вареной сгущенкой')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_cookies = ReplyKeyboardMarkup(keyboard=buttons_cookies_list, resize_keyboard=True)

# кнопки ассортимент → меню → пироги
buttons_pies_list = [
    [
        KeyboardButton(text='Пирог с яблоком и брусникой')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_pies = ReplyKeyboardMarkup(keyboard=buttons_pies_list, resize_keyboard=True)

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
        KeyboardButton(text='Ближайшая пекарня к Вам', request_location=True),
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

# подписка кнопки
buttons_subscription_list = [
    [
        KeyboardButton(text='Возможности подписки'),
        KeyboardButton(text='Моя подписка'),
        KeyboardButton(text='Оформить подписку')
    ],
    [
        KeyboardButton(text='Главное меню')
    ]
]
buttons_subscription = ReplyKeyboardMarkup(keyboard=buttons_subscription_list, resize_keyboard=True)

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
