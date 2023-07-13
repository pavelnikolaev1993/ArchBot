from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_num: KeyboardButton = KeyboardButton(text='Поиск по шифру')
button_name: KeyboardButton = KeyboardButton(text='Поиск по наименованию')

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
search_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с параметром width=2
search_kb_builder.row(button_num, button_name, width=2)

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
search_kb = search_kb_builder.as_markup(
                                one_time_keyboard=True,
                                resize_keyboard=True)
# Создаем объекты инлайн-кнопок
arch_button: InlineKeyboardButton = InlineKeyboardButton(
    text='Показать тома в архиве',
    callback_data='Запрос на тома в архиве')

# Создаем объект инлайн-клавиатуры
in_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[arch_button]])