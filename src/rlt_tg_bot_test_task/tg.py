import typing

from aiogram import Bot, Dispatcher, types, BaseMiddleware

from rlt_tg_bot_test_task.config import settings
from rlt_tg_bot_test_task.lp import SQLAgent

bot = Bot(token=settings.tg_bot_settings.api_token)
dp = Dispatcher()



# class SQLAgentMiddelware(BaseMiddleware):


#     def __init__(self, sql_agent: SQLAgent):
#         self.sql_agent = sql_agent


#     async def __call__(
#         self, 
#         handler: typing.Callable[
#             [
#                 types.TelegramObject,
#                 dict[str, typing.Any],
#                 typing.Awaitable[typing.Any]
#             ], 
#         ], 
#         event: types.Message,
#         data: dict[str, typing.Any]
#     ):

#         data["sql_agent"] = self.sql_agent
#         await handler(event, data)



@dp.message()
async def echo_handler(message: types.Message, sql_agent: SQLAgent):

    content = message.text
    if content is None:
        await message.answer("failed to retreive message text") 
        return
    if not content:
        await message.answer("message is empty") 
        return

    sql_agent.user_prompt = content
    answer = await sql_agent.query_db()
    await message.answer(answer)
        


# @dp.message()
# async def echo_handler(message: types.Message):

#     try: 
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.answer("Nice try!")





