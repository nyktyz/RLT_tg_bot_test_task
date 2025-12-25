import asyncio

from rlt_tg_bot_test_task.tg import bot, dp
from rlt_tg_bot_test_task.database import populate_tables 


async def main():
    populate_tables()
    # await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())

