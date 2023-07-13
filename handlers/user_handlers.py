from aiogram import Router, F
from aiogram.filters import Command, CommandStart, callback_data, Filter, StateFilter
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import LEXICON_RU
import pandas as pd
from keyboards import search_kb, in_keyboard
from aiogram.filters import Text
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import State, StatesGroup

router: Router = Router()

pd.read_excel(io='Arch.xlsx', engine='openpyxl')
df = pd.concat(pd.read_excel(r'C:\Users\НиколаевПА\PycharmProjects\ProjectsBot\Projects.xlsx', engine='openpyxl',
                             sheet_name=None), ignore_index=True)
af = pd.concat(pd.read_excel(r'C:\Users\НиколаевПА\PycharmProjects\ProjectsBot\Arch.xlsx', engine='openpyxl',
                             sheet_name=None), ignore_index=True)
pd.options.display.max_colwidth = 400

h = []

class FSMFillForm(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодейтсвия с пользователем
    fill_start = State()        # Состояние ожидания ввода имени
    fill_number = State()         # Состояние ожидания ввода возраста
    fill_name = State()      # Состояние ожидания выбора пола


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=search_kb)
    await state.set_state(FSMFillForm.fill_start)

# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=search_kb)

# поиск по шифру
@router.message(Text(text='Поиск по шифру'), StateFilter(FSMFillForm.fill_start))
async def num_search_process(message:Message, state: FSMContext):
    await message.answer(text='Введите шифр')
    await state.set_state(FSMFillForm.fill_number)


    @router.message(StateFilter(FSMFillForm.fill_number))
    async def num_process(message: Message):
        n = message.text
        num = df[(df['Шифр объекта'].str.contains(n, na=False))]
        for i in range(num.shape[0]):
            row = num[['Наименование', 'Шифр объекта', 'Наличие в архиве']].iloc[i]
            row = row.to_dict()
            number = row.setdefault('Шифр объекта')
            builder = InlineKeyboardBuilder()
            builder.add(InlineKeyboardButton(text='Поиск в архиве', callback_data=number))
            h.append(number)
            if row['Наличие в архиве'] == 'Да':
                await message.answer(f'Наименование: {row["Наименование"]}\n'
                        f'Шифр: {row["Шифр объекта"]}\n'
                        f'Наличие в архиве: {row["Наличие в архиве"]}', reply_markup=builder.as_markup())
            else:
                await message.answer(f'Наименование: {row["Наименование"]}\n'
                                     f'Шифр: {row["Шифр объекта"]}\n'
                                     f'Наличие в архиве: {row["Наличие в архиве"]}')

        @router.callback_query(F.data.in_(h), StateFilter(FSMFillForm.fill_number))
        async def process_edit_press(callback: CallbackQuery):
            ar_num = af[(af['Шифр объекта'].str.contains(callback.data, na=False))]
            ar_col = ar_num.iloc[:, 3].to_list()
            await callback.message.edit_text(
                text="\n".join(ar_col),
                reply_markup=callback.message.reply_markup)
            await callback.answer()

#Поиск по наименованию
@router.message(Text(text='Поиск по наименованию'), StateFilter(FSMFillForm.fill_start))
async def name_search_process(message:Message, state: FSMContext):
    await message.answer(text='Введите наименование объекта')
    await state.set_state(FSMFillForm.fill_name)

    @router.message(StateFilter(FSMFillForm.fill_name))
    async def num_process(message: Message):
        n = message.text
        num = df[(df['Наименование'].str.contains(n, na=False))]
        for i in range(num.shape[0]):
            row = num[['Наименование', 'Шифр объекта', 'Наличие в архиве']].iloc[i]
            row = row.to_dict()
            number = row.setdefault('Шифр объекта')
            builder = InlineKeyboardBuilder()
            builder.add(InlineKeyboardButton(text='Поиск в архиве', callback_data=number))
            h.append(number)
            if row['Наличие в архиве'] == 'Да':
                await message.answer(f'Наименование: {row["Наименование"]}\n'
                                     f'Шифр: {row["Шифр объекта"]}\n'
                                     f'Наличие в архиве: {row["Наличие в архиве"]}', reply_markup=builder.as_markup())
            else:
                await message.answer(f'Наименование: {row["Наименование"]}\n'
                                     f'Шифр: {row["Шифр объекта"]}\n'
                                     f'Наличие в архиве: {row["Наличие в архиве"]}')

        @router.callback_query(F.data.in_(h), StateFilter(FSMFillForm.fill_name))
        async def process_edit_press(callback: CallbackQuery):
            ar_num = af[(af['Шифр объекта'].str.contains(callback.data, na=False))]
            ar_col = ar_num.iloc[:, 3].to_list()
            await callback.message.edit_text(
                text="\n".join(ar_col),
                reply_markup=callback.message.reply_markup)
            await callback.answer()






