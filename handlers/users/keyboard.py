from aiogram import Router, F
from aiogram.types import Message
from data.config import operators_chat, bakeries
from keyboards.default_keyboard import (main_buttons, buttons_mobile_app, buttons_mobile_app_where_download,
                                        buttons_mobile_app_loyalty_system, buttons_assortment, buttons_new_products,
                                        buttons_popular, buttons_quick_to_prepare, buttons_menu, buttons_delivery,
                                        buttons_addresses, buttons_work, buttons_list_bakeries)

router = Router()


# кнопка главное меню
@router.message(F.text.lower() == 'главное меню')
async def button_main_menu(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите интересующую Вас категорию или задайте вопрос.', reply_markup=main_buttons)


# кнопка мобильное приложение
@router.message(F.text.lower() == 'мобильное приложение')
async def button_mobile_app(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите следующую категорию.', reply_markup=buttons_mobile_app)


# кнопка мобильное приложение → где скачать?
@router.message(F.text.lower() == 'где скачать?')
async def button_where_download(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Где вам удобно скачать наше приложение?', reply_markup=buttons_mobile_app_where_download)


# кнопка мобильное приложение → где скачать? → google play
@router.message(F.text.lower() == 'google play')
async def button_google_play(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь будет ссылка.')


# кнопка мобильное приложение → где скачать? → app store
@router.message(F.text.lower() == 'app store')
async def button_app_store(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь будет ссылка.ж')


# кнопка мобильное приложение → где скачать? → app gallery
@router.message(F.text.lower() == 'app gallery')
async def button_app_gallery(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь будет ссылка.')


# кнопка мобильное приложение → как пользоваться?
@router.message(F.text.lower() == 'как пользоваться?')
async def button_how_to_use(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро я узнаю ответ на этот вопрос.')


# кнопка мобильное приложение → система лояльности
@router.message(F.text.lower() == 'система лояльности')
async def button_loyalty_system(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите следующую категорию.', reply_markup=buttons_mobile_app_loyalty_system)


# кнопка мобильное приложение → система лояльности → что такое система лояльности?
@router.message(F.text.lower() == 'что такое система лояльности?')
async def button_what_loyalty_system(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Программа лояльности «Любимая пекарня» — построенная на системе накопления и применения '
                             'Бонусных рублей программа потребительской лояльности.')


# кнопка мобильное приложение → система лояльности → кто такой тайный гость?
@router.message(F.text.lower() == 'кто такой тайный гость?')
async def button_who_secret_guest(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('В проверке тайного гостя могут принять участие только лица, достигшие совершеннолетия.\n'
                             'Для участия в проверке необходимо совершить покупку в пекарне'
                             ' (подробная инструкция о ходе проверки высылается отдельно).\n'
                             'Бонусные баллы начисляются только при полном заполнении отчета. '
                             'В отчет потребуется прикрепить фото и аудиозапись.\n '
                             'После приема отчета мы зачисляем 800 баллов на тот аккаунт, '
                             'с которого Вы были авторизованы. Потратить баллы можно в той пекарне, '
                             'где проходила проверка, для этого необходимо переключить локацию в приложении.')


# кнопка мобильное приложение → система лояльности → бонусные баллы
@router.message(F.text.lower() == 'бонусные баллы')
async def button_bonus_points(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Для накопления Бонусных баллов Участник выбирает одну «Любимую пекарню» из всех, '
                             'доступных для заказа.\n'
                             'При каждой покупке продукции в «Любимой пекарне» Участнику начисляются Бонусные баллы '
                             'в размере 7% от суммы покупки (в рублях).\n'
                             'Бонусные баллы могут быть использованы для накопления Бонусов и/или оплаты ими покупок '
                             'в «Любимой пекарне»: в Приложении при оформлении заказа и оплату через Приложение.\n'
                             'Бонусные баллы не начисляются на мерч компании и другие акционные предложения.\n')


# кнопка ассортимент
@router.message(F.text.lower() == 'ассортимент')
async def button_assortment(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Что Вас интересует?', reply_markup=buttons_assortment)


# кнопка ассортимент → новинки
@router.message(F.text.lower() == 'новинки')
async def button_new_products(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите интересующий Вас продукт.', reply_markup=buttons_new_products)


# кнопка ассортимент → новинки → молочный ломтик
@router.message(F.text.lower() == 'молочный ломтик')
async def button_milk_slice(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Шоколадное пирожное с нежнейшей прослойкой сливочного мусса и шоколадной карамели. '
                             'Украшено маршмеллоу и молочным шоколадом.\n'
                             '125 г - 150 рублей.\n'
                             'Состав: '
                             'Шоколадные коржи, сливочный мусс, шоколадная карамель, маршмеллоу, молочный шоколад.\n'
                             'Может содержать аллергены.\n'
                             'Пищевая ценность на 100 г:\n'
                             'Энерг. ценность: 439 ккал\n'
                             'Белки: 5.4 г\n'
                             'Жиры:31 \n'
                             'Углеводы:34.6 г')


# кнопка ассортимент → популярное
@router.message(F.text.lower() == 'популярное')
async def button_popular(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите интересующий Вас продукт.', reply_markup=buttons_popular)


# кнопка ассортимент → популярное → облепиха-имбирь
@router.message(F.text.lower() == 'облепиха-имбирь')
async def button_buckthorn_ginger(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Согревающий напиток на основе протертой облепихи и имбиря с долькой апельсина'
                             ' и звездочкой бадьяна. Украшен свежей мятой.\n'
                             '220 мл - 119 рублей.\n'
                             '400 мл - 169 рублей.\n'
                             'Состав: Вода, основа для напитка, свежая мята, облепиха, бадьян, долька апельсина.\n'
                             'Пищевая ценность на 100 г:\n'
                             'Энерг. ценность: 26 ккал\n'
                             'Белки: 0.1 г\n'
                             'Жиры: 0 г\n'
                             'Углеводы: 6.8 г')


# кнопка ассортимент → быстроприготовимое
@router.message(F.text.lower() == 'быстроприготовимое')
async def button_quick_to_prepar(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите интересующий Вас продукт.', reply_markup=buttons_popular)


# кнопка ассортимент → быстроприготовимое → круассан с ветчиной
@router.message(F.text.lower() == 'круассан с ветчиной')
async def button_ham_croissant(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Классический круассан с сырно-майонезным соусом, ломтиком ветчины, '
                             'слайсами томата и огурца, листом салата.\n'
                             '190 г -159 рублей.\n'
                             'Состав: Круассан классический, ветчина, огурец, укроп, томаты, салат листовой, '
                             'майонез, сыр сливочный.\n'
                             'Пищевая ценность на 100 г:\n'
                             'Энерг. ценность: 255.6 ккал\n'
                             'Белки: 4.7 г\n'
                             'Жиры: 17 г\n'
                             'Углеводы: 21.1 г')


# кнопка ассортимент → меню
@router.message(F.text.lower() == 'меню')
async def button_menu(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите интересующий Вас раздел.', reply_markup=buttons_menu)


# кнопка ассортимент → меню → горячие напитки
@router.message(F.text.lower() == 'горячие напитки')
async def button_hot_drinks(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → холодные напитки
@router.message(F.text.lower() == 'холодные напитки')
async def button_cold_drinks(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → сэндвичи
@router.message(F.text.lower() == 'сэндвичи')
async def button_sandwiches(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → слойки
@router.message(F.text.lower() == 'слойки')
async def button_puffs(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → пироги
@router.message(F.text.lower() == 'пироги')
async def button_pies(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → выпечка
@router.message(F.text.lower() == 'выпечка')
async def button_bakery_products(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → пирожные
@router.message(F.text.lower() == 'пирожные')
async def button_mini_cakes(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → торты
@router.message(F.text.lower() == 'торты')
async def button_cakes(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → хлеб
@router.message(F.text.lower() == 'хлеб')
async def button_bread(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → печенье
@router.message(F.text.lower() == 'печенье')
async def button_cookies(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → азия
@router.message(F.text.lower() == 'азия')
async def button_asia(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → кулинария
@router.message(F.text.lower() == 'кулинария')
async def button_culinary(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → мерч
@router.message(F.text.lower() == 'мерч')
async def button_merch(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь будет наш мерч.')


# кнопка доставка
@router.message(F.text.lower() == 'доставка')
async def button_delivery(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите следующую категорию.', reply_markup=buttons_delivery)


# кнопка доставка → как заказать?
@router.message(F.text.lower() == 'как заказать?')
async def button_how_order(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро я узнаю ответ на этот вопрос.')


# кнопка доставка → как оплатить?
@router.message(F.text.lower() == 'как оплатить?')
async def button_how_pay(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро я узнаю ответ на этот вопрос.')


# кнопка доставка → время доставки
@router.message(F.text.lower() == 'время доставки')
async def button_delivery_time(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро я узнаю ответ на этот вопрос.')


# кнопка адреса
@router.message(F.text.lower() == 'адреса')
async def button_addresses(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите следующую категорию.', reply_markup=buttons_addresses)


# кнопка адреса → самая близкая пекарня к Вам
@router.message(F.location)
async def button_nearest_bakery(message: Message):
    if message.chat.id != operators_chat:
        location = message.location
        latitude = location.latitude
        longitude = location.longitude

        import requests

        token = '5b3ce3597851110001cf624880917488c66c4d4eb6c8c0401fd1e12c'

        def matrix(locations: list, profile=0):
            headers = {
                'Content-Type': 'application/json; charset=utf-8',
                'Accept': 'application/json',
                'Authorization': token
            }
            profile_dict = {
                0: 'driving-car',
                1: 'foot-walking'
            }
            data = {"locations": [i[::-1] for i in locations], "metrics": ["distance", "duration"], "units": "m"}
            res = requests.post(f'https://api.openrouteservice.org/v2/matrix/{profile_dict[profile]}',
                                headers=headers,
                                json=data).json()
            return dict(durations=res['durations'][0][1], distances=res['distances'][0][1])

        time = 99**99
        for key, value in bakeries.items():
            result = matrix([[latitude, longitude], value], 1)
            time_minute = int(result["durations"] / 60)
            if time_minute <= time:
                time = time_minute
                adress = key

        await message.answer(f'Ближайшая к Вам пекарня находится по адресу:\n'
                             f'{adress}')


# кнопка адреса → список пекарен
@router.message(F.text.lower() == 'список пекарен')
async def button_list_bakeries(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите город', reply_markup=buttons_list_bakeries)


# кнопка адреса → список пекарен → санкт-петербург
@router.message(F.text.lower() == 'санкт-петербург')
async def button_saint_petersburg(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Большой проспект ВО 53/10\n'
                             'Большой проспект ПС, 50\n'
                             'Будапештская улица, 33к2\n'
                             'Вознесенский проспект 34Г\n'
                             'Гороховая улица 54\n'
                             'Гражданский проспект 107к4\n'
                             'Дачный проспект 21к1\n'
                             'Замшина улица 31')


# кнопка работа у нас
@router.message(F.text.lower() == 'работа у нас')
async def button_work(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Мы можем Вам предложить следующие вакансии: '
                             'управляющий, пекарь-повар, продавец-кассир.\n'
                             'Выберете интересующую Вас вакансию и заполните анкету.', reply_markup=buttons_work)


# кнопка работа у нас → управляющий
@router.message(F.text.lower() == 'управляющий')
async def button_manager(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь появится подробная информация по вакансии.')


# кнопка работа у нас → пекарь-повар
@router.message(F.text.lower() == 'пекарь-повар')
async def button_baker_cook(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь появится подробная информация по вакансии.')


# кнопка работа у нас → продавец-кассир
@router.message(F.text.lower() == 'продавец-кассир')
async def button_seller_cashier(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Скоро здесь появится подробная информация по вакансии.')
