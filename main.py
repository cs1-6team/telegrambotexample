from aiogram import Bot, Dispatcher
from aiogram.filters.command import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import logging
import sys
import os


bot = Bot(token=os.environ['BOT_TOKEN'])
dp = Dispatcher()


keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Button 1", callback_data="nimadur"), InlineKeyboardButton(text="Button 2", callback_data="nimadur"), InlineKeyboardButton(text="Button 3", callback_data="nimadur")],
    [InlineKeyboardButton(text="Button 4", callback_data="nimadur"), InlineKeyboardButton(text="Button 5", callback_data="nimadur"), InlineKeyboardButton(text="Button 6", callback_data="nimadur")],
    [InlineKeyboardButton(text="Button 7", callback_data="nimadur"), InlineKeyboardButton(text="Button 8", callback_data="nimadur"), InlineKeyboardButton(text="Button 9", callback_data="nimadur")],
    [InlineKeyboardButton(text="Button +", callback_data="nimadur"), InlineKeyboardButton(text="Button 0", callback_data="nimadur"), InlineKeyboardButton(text="Button #", callback_data="nimadur")],
])


@dp.message(CommandStart())
async def welcome_handler(message: Message):
    await message.answer("Assalomu alaykum!")


@dp.message(Command("menu"))
async def menu_handler(message: Message):
    await message.answer("Mana siz uchun menu\n\n\n/start\n/menu", reply_markup=keyboard)


async def main():
    await asyncio.to_thread(logging.basicConfig, level=logging.DEBUG, stream=sys.stdout)
    await dp.start_polling(bot)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
