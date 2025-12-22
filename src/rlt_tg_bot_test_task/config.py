from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    api_token: str = Field()

settings = Settings()
