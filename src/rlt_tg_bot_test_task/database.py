from sqlalchemy import create_engine, URL
from sqlalchemy.orm import DeclarativeBase 

from rlt_tg_bot_test_task.config import settings
from rlt_tg_bot_test_task.get_data_from_json import df_videos, df_video_snapshots



engine = create_engine(
    settings.database_settings.database_url
)
df_videos.to_sql("videos", con=engine, if_exists="replace")
df_video_snapshots.to_sql("video_snapshots", con=engine, if_exists="replace")


class Base(DeclarativeBase):
    pass




