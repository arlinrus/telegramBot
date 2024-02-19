from aiogram import Bot,Dispatcher,types
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove,ContentType, InlineKeyboardButton, InlineKeyboardMarkup,InputFile,InputMediaPhoto
from aiogram import executor
import logging
import asyncio
from random import randrange
from colorcet import kb
import os
from aiogram.types.input_file import InputFile
from aiogram.dispatcher.filters import Text
import cv2

logging.basicConfig(level = logging.INFO)
bot = Bot(token = TOKIENAPI)
dp = Dispatcher(bot)

FORMATTED_TEXT = '''
Зачем нужен этот бот?
'''
FORMATTED_TEXT2 = '''
Чем занимаемся фирма Kedrovv?
...
Почему именно кедр?
...
Что выбрать : баня-бочка или обычная баня?
...
Кедр правда лечит?
...
'''
FORMATTED_TEXT3 ='''
/help - нажмите, чтобы узнать больше информации о банях или связаться для более подробной информации
/description - нажмите, чтобы узнать более подробную информацию о нашей компании
/questions - нажмите, чтобы узнать ответы на часто задаваемые вопросы
'''

#КЛАВА
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('/help')).insert(KeyboardButton('/description')).insert(KeyboardButton('/questions'))

ikb1 = InlineKeyboardMarkup(row_width=1)
ikb2=InlineKeyboardButton(text = 'Instagram📷', callback_data='social_inst' , url = 'https://www.instagram.com/kedrovv__?igsh=NnVkc3hzN3JpZjA4')
ikb3=InlineKeyboardButton(text = 'Telegram📍', callback_data='social_tg', url = 'https://t.me/kedrovv_bath')
ikb1.insert(ikb2)
ikb1.insert(ikb3)

kp = InlineKeyboardMarkup(row_width=3)
kp1 = InlineKeyboardButton(text = 'Окта',  callback_data= 'ban_okta')
kp2 = InlineKeyboardButton(text = 'Овальная',callback_data='ban_oval' )
kp3 = InlineKeyboardButton(text = 'Круглая' ,callback_data= 'ban_round')
kp.add(kp1).add(kp2)
kp.insert(kp3)

#Инлайн клавиатура для кнопок просмотра размера бани окты
okta_inline = InlineKeyboardMarkup(row_width=2)
oval1 = InlineKeyboardButton(text = '4 метра',  callback_data= '4metr')
oval2 = InlineKeyboardButton(text = '4,5 метра  перед',  callback_data= '4,5metr1')
oval3 = InlineKeyboardButton(text = '4,5 метра бок',  callback_data= '4,5metr2')
oval4 = InlineKeyboardButton(text = '5 метров перед',  callback_data= '5metr1')
oval5 = InlineKeyboardButton(text = '5 метров бок',  callback_data= '5metr2')
oval6 = InlineKeyboardButton(text = '6 метров перед',  callback_data= '6metr1')
oval7 = InlineKeyboardButton(text = '6 метров бок',  callback_data= '6metr2')
okta_inline.insert(oval1)
okta_inline.insert(oval2).insert(oval3)
okta_inline.insert(oval4).insert(oval5)
okta_inline.insert(oval6).insert(oval7)

#Инлайн клавиатура для кнопок просмотра размера бани овал
oval_inline = InlineKeyboardMarkup(row_width=2, resize_keyboard=True )
oval1=InlineKeyboardButton(text = '4 метра бок',  callback_data= '4oval1')
oval2=InlineKeyboardButton(text = '4 метра перед',  callback_data= '4oval2')
oval3=InlineKeyboardButton(text = '4x4 метра',  callback_data= '4x4oval')
oval4=InlineKeyboardButton(text = '4x5 метра',  callback_data= '4x5oval')
oval_inline.insert(oval1).insert(oval2)
oval_inline.insert(oval3).insert(oval4)


#Инлайн клавиатура для кнопок просмотра размера бани круглая
round_inline = InlineKeyboardMarkup(row_width=3, resize_keyboard=True )
round1=InlineKeyboardButton(text='3 метра', callback_data='3round')
round2=InlineKeyboardButton(text='4 метра', callback_data='4round')
round3=InlineKeyboardButton(text='4,5 метров', callback_data='4x5round')
round4=InlineKeyboardButton(text='5 метров', callback_data='6round')
round5=InlineKeyboardButton(text='6 метров', callback_data='7round')
round_inline.insert(round1).insert(round2)
round_inline.insert(round3).insert(round4)
round_inline.insert(round5)

ikb = InlineKeyboardMarkup(row_width=1)
ib1 = InlineKeyboardButton("Узнать цену📌", callback_data='like')
ib2 = InlineKeyboardButton("Заказать баню📌", callback_data='dislike')
ib3 = InlineKeyboardButton("Проконсультироваться📌",url = 'https://t.me/iamarlinrus')
ib4 = InlineKeyboardButton("Социальные сети📌",callback_data='cosmed')
ib5 = InlineKeyboardButton("Поделиться", switch_inline_query='<-- бани из алтайского кедра')
ikb.insert(ib1)
ikb.insert(ib2)
ikb.insert(ib3)
ikb.insert(ib4)
ikb.insert(ib5)



async def on_startup(_):
    print('Ready!')


#START AND HELP
@dp.message_handler(commands = ['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id,
                           text = FORMATTED_TEXT3 ,
                           reply_markup= kb)
    await message.delete()

@dp.message_handler(commands = ['description'])
async def cmd_start(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id,
                           text = FORMATTED_TEXT )
    await message.delete()

@dp.message_handler(commands = ['help'])
async def cmd_sm(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id,
                           text='Добро пожаловать в главное меню',
                           reply_markup = ikb )

@dp.message_handler(commands = ['questions'])
async def cmd_sm(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id,
                           text=FORMATTED_TEXT2)
@dp.callback_query_handler(text = 'like')
async def cmd_know(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id )
    await bot.send_message(call.from_user.id,text= 'Выберите форму бани, которую хотите использовать: ' ,reply_markup=kp)

@dp.callback_query_handler(text='dislike')
async def cmd_order(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id,text = 'Звоните по номеру: 89819542507', reply_markup= ib2)

@dp.callback_query_handler(text='cosmed')
async def cmd_order(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id,text = 'Мы есть в социальных сетях >>> Подписывайтесь, чтобы получать больше актуальной информации и быть в курсе всех новостей!', reply_markup= ikb1)

@dp.callback_query_handler(text_contains='social_')
async def cmd_social(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    if call.data == "social_inst":
        await bot.send_message(call.from_user.id,  call.message.message_id)
    if call.data == "social_inst":
        await bot.send_message(call.from_user.id,  call.message.message_id)

@dp.callback_query_handler(text_contains='ban_')
async def cmd_bani(call: types.CallbackQuery):
    if call.data == 'ban_okta':
        await bot.send_message(call.from_user.id,text ='Выберите: ', reply_markup=okta_inline)
    if call.data == 'ban_oval':
        await bot.send_message(call.from_user.id, text ='Выберите: ', reply_markup=oval_inline)
    if call.data == 'ban_round':
        await bot.send_message(call.from_user.id, text ='Выберите: ',reply_markup=round_inline )


#Определяем для бани окты фотографии к каждому метражу
@dp.callback_query_handler(text_contains = 'metr')
async def cmd_metr(call: types.CallbackQuery):
    # await bot.delete_message(call.from_user.id, call.message.message_id)
    if call.data == '4metr':
        photo_path = 'okta-banya-bochka-4_5-metra-s-kozyrkom-v.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
    if call.data == '4,5metr1':
        photo_path = 'OKTA 4,5m_st_2.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
    if call.data == '4,5metr2':
        photo_path = 'OKTA_4_5_b_2.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
    if call.data == '5metr1':
        photo_path = 'okta-banya-bochka-5_5-metrov-s-kozyrkom-.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
    if call.data == '5metr2':
        photo_path = 'okta-banya-bochka-5-metrov-so-vhodom-sbo.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
    if call.data == '6metr1':
        photo_path = 'OKTA_6m_vr_2.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
    if call.data == '6metr2':
        photo_path = 'okta-banya-bochka-6-metrov-so-vhodom-sbo.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)

#Определяем для овальной бани фотографии к каждому метражу
@dp.callback_query_handler(text_contains = 'oval')
async def cmd_oval(call: types.CallbackQuery):
    # await bot.delete_message(call.from_user.id, call.message.message_id)
    if call.data == '4oval1':
        photo_path1 = 'oval4pered.jpg'
        with open(photo_path1, 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
    if call.data == '4oval2':
        photo_path1 = 'oval4metr.jpg'
        with open(photo_path1, 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
    if call.data == '4x4oval':
        photo_path1 = 'oval4x4.jpg'
        with open(photo_path1, 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
    if call.data == '4x5oval':
        photo_path1 = 'oval4x5.jpg'
        with open(photo_path1, 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)

#Определяем для круглой бани фотографии к каждому метражу
@dp.callback_query_handler(text_contains = 'round')
async def cmd_round(call: types.CallbackQuery):
    # await bot.delete_message(call.from_user.id, call.message.message_id)
    if call.data == '3round':
        photo_path = 'round3.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
    if call.data == '4round':
        photo_path = 'round4.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
    if call.data == '4x5round':
        photo_path = 'round4x5.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
    if call.data == '6round':
        photo_path = 'round5.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)
    if call.data == '7round':
        photo_path = 'round6.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(call.from_user.id, photo)



if __name__ == '__main__' :
    executor.start_polling(dp, skip_updates = True, on_startup = on_startup )
