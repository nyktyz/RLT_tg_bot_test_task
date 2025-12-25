from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL




class TGBotSettings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    api_token: str  


class LLMSettings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    model_name: str
    base_url: str
    openrouter_api_token: str  


class DatabaseSettings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env", 
        extra="ignore",
        env_prefix="postgres_"
    )

    driver: str
    user: str
    pw: str
    host: str
    port: int
    db: str
    # query: str

    @computed_field
    @property
    def database_url(self) -> URL:
        return URL(
            self.driver,
            username=self.user,
            password=self.pw,
            host=self.host,
            port=self.port,
            database=self.db,
            query={}
        )



class Settings(BaseSettings):

    database_settings: DatabaseSettings = DatabaseSettings()
    tg_bot_settings: TGBotSettings = TGBotSettings()
    llm_settings: LLMSettings = LLMSettings()


settings = Settings()
print(settings.database_settings.database_url)