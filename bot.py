import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

# Установка уровня логирования
logging.basicConfig(level=logging.INFO)

# Загрузка переменных окружения
load_dotenv()

# Инициализация бота и диспетчера
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я телеграмм бот.")

# Обработчик текстовых сообщений
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
