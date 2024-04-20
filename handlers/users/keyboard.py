from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from data.config import operators_chat, bakeries, db
from keyboards.default_keyboard import (main_buttons, buttons_mobile_app, buttons_mobile_app_where_download,
                                        buttons_mobile_app_loyalty_system, buttons_assortment, buttons_new_products,
                                        buttons_popular, buttons_quick_to_prepare, buttons_menu, buttons_delivery,
                                        buttons_addresses, buttons_work, buttons_list_bakeries, buttons_subscription,
                                        buttons_cookery, buttons_cookies, buttons_bread, buttons_pies)
from keyboards.inline_keyboard import inlinebutton_change_subscription

router = Router()


# анкета https://www.xleb.ru/job#form
# будущее нововведение
# данные будут добавляться в бд
class Form(StatesGroup):
    fi = State()
    phone_number = State()
    email = State()
    birthdate = State()
    city = State()
    metro = State()
    workplace = State()


# кнопка главное меню
@router.message(F.text.lower() == 'главное меню')
async def button_main_menu(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите интересующую Вас категорию или задайте вопрос.', reply_markup=main_buttons)


# кнопка заказ
@router.message(F.text.lower() == 'заказ')
async def button_shop(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Функция в доработке.')


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
        await message.answer('https://play.google.com/store/apps/details?id=ru.xleb.app')


# кнопка мобильное приложение → где скачать? → app store
@router.message(F.text.lower() == 'app store')
async def button_app_store(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('https://apps.apple.com/ru/app/%D1%85%D0%BB%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA/id1516812475')


# кнопка мобильное приложение → где скачать? → app gallery
@router.message(F.text.lower() == 'app gallery')
async def button_app_gallery(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('https://appgallery.huawei.com/#/app/C104393367')


# кнопка мобильное приложение → как пользоваться?
@router.message(F.text.lower() == 'как пользоваться?')
async def button_how_to_use(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('С помощью приложения вы сможете заказать интересующие вас позиции онлайн. '
                             'Кроме того, показав qr-код из приложения на кассе при покупке кофе, '
                             'вы сможете получить шестой кофе бесплатно.')


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
# @router.message(F.text.lower() == 'горячие напитки')
# async def button_hot_drinks(message: Message):
#     if message.chat.id != operators_chat:
#         await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → холодные напитки
# @router.message(F.text.lower() == 'холодные напитки')
# async def button_cold_drinks(message: Message):
#     if message.chat.id != operators_chat:
#         await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → сэндвичи
# @router.message(F.text.lower() == 'сэндвичи')
# async def button_sandwiches(message: Message):
#     if message.chat.id != operators_chat:
#         await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → слойки
# @router.message(F.text.lower() == 'слойки')
# async def button_puffs(message: Message):
#     if message.chat.id != operators_chat:
#         await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → пироги
@router.message(F.text.lower() == 'пироги')
async def button_pies(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите интересующий Вас раздел.', reply_markup=buttons_pies)


# кнопка ассортимент → меню → пироги → пирог с яблоком и брусникой
@router.message(F.text.lower() == 'пирог с яблоком и брусникой')
async def button_pie(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Пирог с яблоком и брусникой\n\n'
                             'Состав: Тесто: слоено-дрожжевое тесто. Начинка: яблоки резанные кубик, брусника замороженная, сахар, загуститель\n'
                             'На 100 гр:\n'
                             'Энерг. ценность: 199,9\n'
                             'Белки: 3,3\n'
                             'Жиры: 4,3\n'
                             'Углеводы: 37,3\n\n'
                             'Целый/866 руб.\n'
                             'Порция/109 руб.')


# кнопка ассортимент → меню → выпечка
# @router.message(F.text.lower() == 'выпечка')
# async def button_bakery_products(message: Message):
#     if message.chat.id != operators_chat:
#         await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → пирожные
# @router.message(F.text.lower() == 'пирожные')
# async def button_mini_cakes(message: Message):
#     if message.chat.id != operators_chat:
#         await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → торты
# @router.message(F.text.lower() == 'торты')
# async def button_cakes(message: Message):
#     if message.chat.id != operators_chat:
#         await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → хлеб
@router.message(F.text.lower() == 'хлеб')
async def button_bread(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите интересующий Вас раздел.', reply_markup=buttons_bread)


# кнопка ассортимент → меню → хлеб → багет французский
@router.message(F.text.lower() == 'багет французский')
async def button_baguette(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Багет французский\n\n'
                             'Состав: Мука пшеничная в/с, вода, дрожжи, соль, масло подсолнечное\n'
                             'На 100 гр:\n'
                             'Энерг. ценность: 234,69\n'
                             'Белки: 6,27\n'
                             'Жиры: 3,92\n'
                             'Углеводы: 43,58\n\n'
                             '300 г/81 руб.')


# кнопка ассортимент → меню → печенье
@router.message(F.text.lower() == 'печенье')
async def button_cookies(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите интересующий Вас раздел.', reply_markup=buttons_cookies)


# кнопка ассортимент → меню → печенье → орешки с вареной сгущенкой
@router.message(F.text.lower() == 'орешки с вареной сгущенкой')
async def button_cookie(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Орешки с вареной сгущенкой\n\n'
                             'Состав: Мука пшеничная в/с, сахар, яйцо, маргарин, молоко сгущенное вареное.\n'
                             'На 100 гр:\n'
                             'Энерг. ценность: 457,08\n'
                             'Белки: 8,44\n'
                             'Жиры: 16,25\n'
                             'Углеводы: 69,28\n\n'
                             '15 шт./118 руб.')


# кнопка ассортимент → меню → азия
# @router.message(F.text.lower() == 'азия')
# async def button_asia(message: Message):
#     if message.chat.id != operators_chat:
#         await message.answer('Скоро здесь будут позиции меню.')


# кнопка ассортимент → меню → кулинария
@router.message(F.text.lower() == 'кулинария')
async def button_culinary(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите интересующий Вас раздел.', reply_markup=buttons_cookery)


# кнопка ассортимент → меню → кулинария → онигири с цыпленком терияки
@router.message(F.text.lower() == 'онигири с цыпленком терияки')
async def button_culinar(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Онигири с цыпленком терияки\n\n'
                             'Состав: Рис, вода, филе куриной грудки, меланж яичный, майонез, уксус рисовый, соус терияки, сахар-песок, соус унаги , кунжут белый, водросли нори, соус шрирача, соль, масло подсолнечное, чеснок, комбу, тимьян, шичими.\n'
                             'На 100 гр:\n'
                             'Энерг. ценность: 188,5\n'
                             'Белки: 7\n'
                             'Жиры: 4,5\n'
                             'Углеводы: 30\n\n'
                             '120 г/147 руб.')


# кнопка ассортимент → мерч
@router.message(F.text.lower() == 'мерч')
async def button_merch(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('У нас есть термокружка, кофе в зернах, капсульный кофе, бутылка для воды. Подробнее можете узнать в приложении.')


# кнопка доставка
@router.message(F.text.lower() == 'доставка')
async def button_delivery(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Доставка скоро будет!')#, reply_markup=buttons_delivery)


# кнопка доставка → как заказать?
@router.message(F.text.lower() == 'как заказать?')
async def button_how_order(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('')


# кнопка доставка → как оплатить?
@router.message(F.text.lower() == 'как оплатить?')
async def button_how_pay(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('')


# кнопка доставка → время доставки
@router.message(F.text.lower() == 'время доставки')
async def button_delivery_time(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('')


# кнопка адреса
@router.message(F.text.lower() == 'адреса')
async def button_addresses(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите следующую категорию.', reply_markup=buttons_addresses)


# кнопка адреса → ближайшая пекарня к Вам
@router.message(F.location)
async def button_nearest_bakery(message: Message):
    if message.chat.id != operators_chat:
        user_location = message.location
        user_latitude = user_location.latitude
        user_longitude = user_location.longitude

        from geopy.distance import geodesic
        distance_to_bakeries = {}
        for row in db.view_data_in_addresses():
            address = row[1]
            url = row[2]
            bakery_latitude = row[3]
            bakery_longitude = row[4]

            distance_km = geodesic((user_latitude, user_longitude), (bakery_latitude, bakery_longitude)).kilometers
            distance_to_bakeries[address] = {url: float(f'{distance_km:.2f}')}

        distance_to_bakeries = sorted(distance_to_bakeries.items(), key=lambda item: list(item[1].values())[0])
        await message.answer(f'3 ближайших к Вам пекарни:\n'
                             f'<a href="{list(distance_to_bakeries[0][1].keys())[0]}">{distance_to_bakeries[0][0]}</a> - {list(distance_to_bakeries[0][1].values())[0]} км\n'
                             f'<a href="{list(distance_to_bakeries[1][1].keys())[0]}">{distance_to_bakeries[1][0]}</a> - {list(distance_to_bakeries[1][1].values())[0]} км\n'
                             f'<a href="{list(distance_to_bakeries[2][1].keys())[0]}">{distance_to_bakeries[2][0]}</a> - {list(distance_to_bakeries[2][1].values())[0]} км\n')


# кнопка адреса → список пекарен
@router.message(F.text.lower() == 'список пекарен')
async def button_list_bakeries(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите город', reply_markup=buttons_list_bakeries)


# кнопка адреса → список пекарен → санкт-петербург
@router.message(F.text.lower() == 'санкт-петербург')
async def button_saint_petersburg(message: Message):
    if message.chat.id != operators_chat:
        data = ''
        for row in db.view_data_in_addresses():
            address = row[1]
            url = row[2]
            metro = row[5]
            data += f'<a href="{url}">{address}</a>, метро {metro}\n'

        await message.answer(data)


# кнопка подписка
@router.message(F.text.lower() == 'подписка')
async def button_subscription(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Выберите следующую категорию.', reply_markup=buttons_subscription)


# кнопка подписка → возможности подписки
@router.message(F.text.lower() == 'возможности подписки')
async def button_subscription_options(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('С подпиской у вас будут следующие возможности:\n'
                             '1) скидка 5% на все позиции\n'
                             '2) 3 купона на бесплатные сезонные напитки\n'
                             '3) 4 купона на позиции со скидкой от 10 до 30%\n'
                             'Цена подписки 299 рублей в месяц')


# кнопка подписка → моя подписка
@router.message(F.text.lower() == 'моя подписка')
async def button_my_subscription(message: Message):
    if message.chat.id != operators_chat:
        for row in db.get_user_with_subscription():
            if message.chat.id in row:
                await message.answer(f'Подписка до {db.get_duration_of_subscription(message.chat.id)}\n'
                                     'У вас есть:\n'
                                     '1) скидка 5% на все позиции\n'
                                     '2) 3 купона на бесплатные сезонные напитки\n'
                                     '3) 4 купона на позиции со скидкой от 10 до 30%\n'
                                     'Купоны можете смотреть в разделе купоны в главном меню.', reply_markup=inlinebutton_change_subscription)
                break
        else:
            await message.answer('К сожалению, у Вас нет подписки. Чтобы её оформить, перейдите в раздел Оформить подписку.')


@router.callback_query(F.data == 'prolong_subscription_month')
async def prolong_subscription_month(callback: CallbackQuery):
    await callback.answer()

    await callback.message.edit_text(f'Вы успешно продлили подписку на месяц до {db.prolong_subscription_month(callback.message.chat.id)}')


@router.callback_query(F.data == 'prolong_subscription_year')
async def prolong_subscription_year(callback: CallbackQuery):
    await callback.answer()

    await callback.message.edit_text(f'Вы успешно продлили подписку на год до {db.prolong_subscription_year(callback.message.chat.id)}')


# кнопка подписка → оформить подписку
@router.message(F.text.lower() == 'оформить подписку')
async def button_subscribe(message: Message):
    if message.chat.id != operators_chat:
        for row in db.get_user_with_subscription():
            if message.chat.id in row:
                await message.answer('У вас уже есть подписка. Ей Вы можете управлять в разделе Моя подписка.')
                break
        else:
            await message.answer(f'Вы успешно оформили подписку до {db.add_user_to_subscription(message.chat.id, message.chat.username)}')


# кнопка купоны
@router.message(F.text.lower() == 'купоны')
async def button_coupons(message: Message):
    if message.chat.id != operators_chat:
        await message.answer(f'Купоны обычного пользователя:\n'
                             f'1)Купон 2% скидка на всё: {db.add_coupon(message.chat.id, message.chat.username)}')
        for row in db.get_user_with_subscription():
            if message.chat.id in row:
                await message.answer('Купоны обладателя подписки:\n'
                                     '1) скидка 5% на все позиции\n'
                                     '2) 3 купона на бесплатные сезонные напитки\n'
                                     '3) 4 купона на позиции со скидкой от 10 до 30%\n')
                break


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
        await message.answer('Заполни анкету и мы свяжемся с тобой: https://www.xleb.ru/job#form')


# кнопка работа у нас → пекарь-повар
@router.message(F.text.lower() == 'пекарь-повар')
async def button_baker_cook(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Заполни анкету и мы свяжемся с тобой: https://www.xleb.ru/job#form')


# кнопка работа у нас → продавец-кассир
@router.message(F.text.lower() == 'продавец-кассир')
async def button_seller_cashier(message: Message):
    if message.chat.id != operators_chat:
        await message.answer('Заполни анкету и мы свяжемся с тобой: https://www.xleb.ru/job#form')
