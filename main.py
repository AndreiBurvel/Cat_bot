from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import requests

api_url = 'https://api.thecatapi.com/v1/images/search'

with open('token.txt', 'r') as f:
    BOT_TOKEN=f.read()

bot=Bot(token=BOT_TOKEN)
dp=Dispatcher()

@dp.message(Command(commands=['start']))
async def process_start_command(message:Message):
    await message.answer('Привет! Я бот котеек! Напиши мне что-нибудь и я вышлю котейку тебе в ответ!')

@dp.message(Command(commands=['help']))
async def process_help_command(message:Message):
    await message.answer('В любой непонятной ситуации я шлю котейку:)')

@dp.message()
async def process_any_command(message:Message):
    response=requests.get(api_url)
    if response.status_code==200:
        photo=response.json()[0]['url']
    await bot.send_photo(chat_id=message.chat.id, photo=photo)

if __name__ == '__main__':
    dp.run_polling(bot)