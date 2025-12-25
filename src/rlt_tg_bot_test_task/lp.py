import os
from pathlib import Path


from langchain.agents import create_agent
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI

# from langchain_ollama import OllamaLLM



from rlt_tg_bot_test_task.config import settings






system_prompt = """ты - продвинутый аналитик данных свободно владеющий языком sql. 
напиши запрос на языке sql к таблице users, который находит ползователя по его id. 
В своем ответе предоставь только сам запрос, никаких коммеентариев или пояснений давать не нужно. 
Также не пиши символы ``` в начале и в конце запроса
"""




# class LLMLocal(BaseLanguageModel):
    
#     def generate_prompt(
#         self, prompts: list[PromptValue], stop: list[str] | None 
#     ):




class SQLAgent:

    def __init__(self):
        self.db = SQLDatabase.from_uri(
            settings.database_settings.database_url
        )
        self.llm = ChatOpenAI(
            model_name=settings.llm_settings.model_name,
            api_key=settings.llm_settings.openrouter_api_token,
            base_url=settings.llm_settings.base_url
        )
        self.toolkit = SQLDatabaseToolkit(
            db=self.db,
            llm=self.llm
        )


    def _format_system_prompt(self):
        ...



    async def _format_user_prompt(self):
        ...












