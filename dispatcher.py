from aiogram import Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import config
import random
import agents
import logging

logging.basicConfig(level=logging.INFO)

dp = Dispatcher(config.BOT)

@dp.message_handler()
async def echo(message: Message):
    all_peak = []
    for i in range(3):
        peak = random.choice(list(agents.AGENTS[random.choice(list(agents.AGENTS.keys()))]))
        all_peak.append(peak)
    for j in range(len(all_peak)):
        if all_peak.count(j) > 1:
            peak = random.choice(list(agents.AGENTS[random.choice(list(agents.AGENTS.keys()))]))
            all_peak[j] = peak
    peak_finally = ' '.join(all_peak)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)
    key_button = KeyboardButton('Карты')
    keyboard.add(key_button)
    
    match(message.text):
        case '/start':
            await message.answer('Привет, нажми на кнопку "Карты" и выбери карту', reply_markup=keyboard)
        case 'Карты':
            keyboard_map = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=3)

            key_ascent = KeyboardButton('Ascent')
            keyboard_map.add(key_ascent)
            
            key_bind = KeyboardButton('Bind')
            keyboard_map.add(key_bind)

            key_haven = KeyboardButton('Haven')
            keyboard_map.add(key_haven)
            
            key_split = KeyboardButton('Split')
            keyboard_map.add(key_split)
            
            key_lotus = KeyboardButton('Lotus')
            keyboard_map.add(key_lotus)
            
            key_sunset = KeyboardButton('Sunset')
            keyboard_map.add(key_sunset)

            await message.answer('Карты', reply_markup=keyboard_map)

        
        case 'Ascent':
            picture = open('maps\ASCENT.png', 'rb')
            await message.answer_photo(picture, caption=f'Peak: {message.text}\n{peak_finally}')
            # await message.answer(f'Peak: {message.text}\n{all_peak}')

        case 'Bind':
            picture = open('maps/BIND.png', 'rb')
            await message.answer_photo(picture, caption=f'Peak: {message.text}\n{peak_finally}')

            # await message.answer(f'Peak: {message.text}\n{all_peak}')
        
        case 'Haven':
            picture = open('maps\HAVEN.png', 'rb')
            await message.answer_photo(picture, caption=f'Peak: {message.text}\n{peak_finally}')
            # await message.answer(f'Peak: {message.text}\n{all_peak}')
        
        case 'Split':
            picture = open('maps\SPLIT.png', 'rb')
            await message.answer_photo(picture, caption=f'Peak: {message.text}\n{peak_finally}')
            # await message.answer(f'Peak: {message.text}\n{all_peak}')
        
        case 'Lotus':
            picture = open('maps\LOTUS.png', 'rb')
            await message.answer_photo(picture, caption=f'Peak: {message.text}\n{peak_finally}')
            # await message.answer(f'Peak: {message.text}\n{all_peak}')
        
        case 'Sunset':
            picture = open('maps\SUNSET.png', 'rb')
            await message.answer_photo(picture, caption=f'Peak: {message.text}\n{peak_finally}')
            # await message.answer(f'Peak: {message.text}\n{all_peak}')