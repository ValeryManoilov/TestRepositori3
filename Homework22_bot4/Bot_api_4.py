from Config_4 import Config
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = Bot(Config.BOT_TOKEN)
dp = Dispatcher(token)

@dp.message_handler(commands='start')
async def eho(message: types.Message):
    await token.send_message(message.from_user.id, f'Добрый день, {message.from_user.username}')


@dp.message_handler(commands='help')
async def eho(message: types.Message):
    await token.send_message(message.from_user.id, f'Добрый день, {message.from_user.username}')

if __name__ == "__main__":
    executor.start_polling(dp)

# Ссылка на бота
# https://t.me/Valeras_eho_bot