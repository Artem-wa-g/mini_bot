import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6584575989:AAGifcX4Uj2gWKy_NJJ4ArnoN_dNIBMwtMg", parse_mode="HTML")
# Диспетчер
dp = Dispatcher()


async def keyb():
    kb = [
        [
            types.KeyboardButton(text="Отзывы")
        ],
        [
            types.KeyboardButton(text="📲 Профиль")
        ],
        [
            types.KeyboardButton(text="📙 Заказы"),
            types.KeyboardButton(text="Примеры")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    return keyboard


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = await keyb()

    await message.answer(
        text="<b>Привет</b>, <i>Дорогой путник!</i> "
             "Ты наткнулся на нашу группу по дизайну, где тебе сделают недорого"
             "Короче тут какой-то текст.....",
        reply_markup=keyboard
    )


@dp.message(F.text == 'Отзывы')
async def reviews(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="что-то")
        ],
        [
            types.KeyboardButton(text="что-то")
        ],
        [
            types.KeyboardButton(text="Назад")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer(
        text='💻 Отзывы',
        reply_markup=keyboard
    )


@dp.message(F.text == '📲 Профиль')
async def profile(message: types.Message):
    await message.answer(text='📲 Профиль')


@dp.message(F.text == '📙 Заказы')
async def orders(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Кнопка для примера",
        callback_data="check")
    )
    builder.add(types.InlineKeyboardButton(
        text="Еще какаято",
        callback_data="rrerrre")
    )
    builder.add(types.InlineKeyboardButton(
        text="А это кнопка ссылка",
        url="https://www.youtube.com/")
    )
    builder.adjust(1)
    await message.answer(
        text="📙 Заказы тут может быть любой текст",
        reply_markup=builder.as_markup()
    )



@dp.message(F.text == 'Назад')
async def profile(message: types.Message):
    keyboard = await keyb()

    await message.answer(
        text="Назад",
        reply_markup=keyboard
    )


@dp.message(F.data == 'check')
async def check(message: types.Message):

    await message.answer(
        text="вывод этой кнопки check"
    )


@dp.message(F.data == 'rrerrre')
async def rrerrre(message: types.Message):

    await message.answer(
        text="вывод этой кнопки"
    )




@dp.message(F.text == 'Примеры')
async def profile(message: types.Message, bot: Bot):


    await bot.send_photo(
        chat_id=message.from_user.id,
        caption="Примеры всех работ доступны по ссылке <a href=\"https://www.youtube.com/\">Ссылка на тексте</a>",
        photo='https://s1.1zoom.ru/big3/114/349146-admin.jpg'
    )


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
