import os
from dotenv import load_dotenv
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from database import Database

load_dotenv()
bot = Bot(os.getenv('TOKEN'), parse_mode='HTML')

db = Database('database/hlebnik_database.db')

dp = Dispatcher(storage=MemoryStorage())

# чат операторов
operators_chat = -1001646453733

# словарь с id и username операторов
operators = {1238334856: '@shaylushay84'}

bakeries = {'Санкт-Петербург, Гражданский проспект, 107к4': [60.028681, 30.414665],
            'Санкт-Петербург, Тихорецкий проспект, 7к1': [60.013452, 30.369192],
            'Санкт-Петербург, проспект Просвещения, 87к1': [60.036097, 30.414521],
            'Санкт-Петербург, улица Есенина, 12': [60.039018, 30.33131],
            'Санкт-Петербург, Фермское шоссе, 35-37': [60.01673, 30.313056],
            'Санкт-Петербург, Стародеревенская улица, 34к2': [60.006854, 30.246464],
            'Санкт-Петербург, улица Восстания, 3-5': [59.93268, 30.360398],
            'Санкт-Петербург, Будапештская улица, 33к2': [59.859483, 30.376316]}
