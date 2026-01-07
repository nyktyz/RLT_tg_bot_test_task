from langchain.agents import create_agent
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI

from rlt_tg_bot_test_task.config import settings


class SQLAgent:

    def __init__(self):
        self.db = SQLDatabase.from_uri(
            settings.database_settings.database_url
        )
        self.llm = ChatOpenAI(
            model_name=settings.llm_settings.model_name,
            api_key=settings.llm_settings.openrouter_api_token,
            # base_url=settings.llm_settings.base_url
        )
        self.toolkit = SQLDatabaseToolkit(
            db=self.db,
            llm=self.llm
        )
        self.top_k = settings.llm_settings.top_k
        self._system_prompt = ""
        self._user_prompt = ""
        res = self.llm.invoke("как у тебя дела?")
        from pprint import pprint
        pprint(res)
        # self.agent = create_agent(
        #     self.llm,
        #     self.toolkit,
        #     system_prompt=self.system_prompt
        # )

        exit()


    @property
    def system_prompt(self):
        return f"""ты - продвинутый аналитик данных свободно владеющий языком sql. 
        напиши запрос на языке sql к таблице users, который находит ползователя по его id. 
        В своем ответе предоставь только сам запрос, никаких коммеентариев или пояснений давать не нужно. 
        Также не пиши символы ``` в начале и в конце запроса

        Вы — агент, предназначенный для взаимодействия с базой данных SQL.
        Получив на вход вопрос, создайте синтаксически корректный запрос на {self.db.dialect},
        затем просмотрите результаты запроса и верните ответ. Если пользователь не указывает конкретное количество примеров, которые он хочет получить, всегда ограничивайте свой запрос максимум {self.top_k} результатами.

        Вы можете упорядочить результаты по соответствующему столбцу, чтобы вернуть наиболее интересные
        примеры в базе данных. Никогда не запрашивайте все столбцы из конкретной таблицы,
        запрашивайте только соответствующие столбцы, исходя из вопроса.

        Вы ОБЯЗАТЕЛЬНО должны дважды проверить свой запрос перед его выполнением. Если вы получили ошибку во время выполнения запроса, перепишите запрос и попробуйте снова.

        НЕ используйте никаких операторов DML (INSERT, UPDATE, DELETE, DROP и т. д.) в базе данных.

        Для начала ВСЕГДА просматривайте таблицы в базе данных, чтобы увидеть, что вы можете запросить. НЕ пропускайте этот шаг.

        Затем следует запросить схему наиболее релевантных таблиц.
        """


    @system_prompt.setter
    def system_prompt(self, value):
        print("it is forbidden to change the system prompt")


    @property
    def user_prompt(self):
        return self._user_prompt


    @user_prompt.setter
    def user_prompt(self, value: str):
        self._user_prompt = value


    async def query_db(self):
        await self.agent.ainvoke(self._user_prompt)














