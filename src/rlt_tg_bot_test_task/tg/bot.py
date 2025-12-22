from aiogram import Bot, Dispatcher, types 

from rlt_tg_bot_test_task.config import settings

bot = Bot(token=settings.api_token)
dp = Dispatcher()


@dp.message()
async def echo_handler(message: types.Message):

    try: 
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")






