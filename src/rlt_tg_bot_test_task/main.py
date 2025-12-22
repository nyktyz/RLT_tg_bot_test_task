import asyncio

from rlt_tg_bot_test_task.tg.bot import bot, dp


async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())

