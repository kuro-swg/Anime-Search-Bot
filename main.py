import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from shikimori import search_anime

#переменные окружения из .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "Введите название Аниме, "
        "и я найду ссылку на него на Shikimori!",
        parse_mode="Markdown"
    )


@dp.message()
async def search_handler(message: types.Message):
    user_query = message.text.strip()
    
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    
    title, url = await search_anime(user_query)
    
    if url:
        text = f"🎬 **{title}**\n\n🔗 [Открыть на Shikimori]({url})"
        await message.answer(text, parse_mode="Markdown", disable_web_page_preview=False)
    else:
        await message.answer("К сожалению, ничего не найдено. Попробуйте уточнить запрос.")


async def main():
    print("🚀 Бот успешно запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())