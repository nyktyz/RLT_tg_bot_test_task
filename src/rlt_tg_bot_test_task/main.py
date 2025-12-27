import asyncio

from rlt_tg_bot_test_task.tg import bot, dp
from rlt_tg_bot_test_task.database import populate_tables
from rlt_tg_bot_test_task.lp import SQLAgent


async def main():
    # populate_tables()
    dp["sql_agent"] = SQLAgent()
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())

