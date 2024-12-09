from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api = "8132492198:AAFBixtKxq98jNmHdlwEJlxX2XysdZfRWSk"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard = True)
button1 = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Рассчитать')
kb.row(button1, button2)

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.\n'
                         'Могу вычислить Вашу норму суточного потребления килокалорий. \n'
                         'Нажмите на кнопку "Рассчитать".', reply_markup = kb)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    male = State()


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст: \n'
                         '(полных лет)')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост(см): \n'
                         '(Если число не целое, введите его в формате "170.35" \n'
                         'разделив точкой без пробелов)')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес: \n'
                         '(Если число не целое, введите его в формате "50.255" \n'
                         'разделив точкой без пробелов)')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_male(message, state):
    await state.update_data(weight=message.text)
    await message.answer('Введите свой пол: \n'
                         'Просто напишите "М" или "Ж" в верхнем регистре')
    await UserState.male.set()

@dp.message_handler(state=UserState.male)
async def send_calories(message, state):
    await state.update_data(male=message.text)
    data = await state.get_data()
    age = float(data['age'])
    weight = float(data['weight'])
    growth = float(data['growth'])
    male = str(data['male'])
    if male == 'Ж':
        calories = 10 * weight + 6.25 * growth - 5 * age - 161
        await message.answer(f'Ваша норма калорий в сутки составляет: {calories} Ккал \n'
                             f'Напишите /start, если хотите начать заново')
    elif male == 'М':
        calories = 10 * weight + 6.25 * growth - 5 * age + 5
        await message.answer(f'Ваша норма калорий в сутки составляет: {calories} Ккал \n'
                             f'Нажмите "Рассчитать", если хотите начать заново')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)