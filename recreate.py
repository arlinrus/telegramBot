from aiogram.types import ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardRemove,KeyboardButton
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from asposecells.api import Workbook
import jpype
import json
import csv

API_TOKEN ='7058282410:AAGMkIh2dt2Q5wyPsPIB5hRrXVr5fZR3msQ'
bot = Bot(token= '7058282410:AAGMkIh2dt2Q5wyPsPIB5hRrXVr5fZR3msQ')
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

#Buttons
kb = ReplyKeyboardMarkup(resize_keyboard=True)
# kb1 = InlineKeyboardButton(text = 'Bot description 📌')
kb.add(KeyboardButton('/help'))

NEW_TEXT = '''
/start - начать сначала
'''
async def on_startup(_):
    print('Ready!')
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id,
                           text = NEW_TEXT ,
                           reply_markup= kb)
    await message.delete()
    # if not message.document:
    #     await message.answer("Please, send a CSV file to convert.")
    #     return
@dp.message_handler(commands=['help'])
async def cmd_start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                            text=NEW_TEXT)
    await message.delete()


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def cmd_convert(message: types.Message):
    file_id = message.document.file_id
    file_path = await bot.get_file(file_id)
    file_url = file_path.file_path
    file = await bot.download_file(file_url)

    with open(file, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        json_data = json.dumps([row for row in csv_reader], indent=2)

    await message.answer(json_data)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)





    # Получаем информацию о файле
    # file = await bot.get_file(file_id=message.document.file_id)
    # file_url = f'https://api.telegram.org/file/bot{API_TOKEN}/{file.file_path}'
    #
    # Читаем CSV файл и конвертируем его в JSON
    # csv_data = []
    # with open(file_url, mode='r') as csv_file:
    #     csv_reader = csv.DictReader(csv_file)
    #     for row in csv_reader:
    #         csv_data.append(row)
    #
    # json_data = json.dumps(csv_data, indent=4)
    #
    # Отправляем конвертированный JSON файл обратно пользователю
    # await message.answer_document(types.InputFile(bio=json_data, filename='converted.json'))

