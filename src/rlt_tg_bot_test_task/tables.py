# from sqlalchemy import BigInteger, Column, Index, MetaData, Table, Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship 


from rlt_tg_bot_test_task.database import Base



class Videos(Base):
    __tablename__ = "videos"    
    Column('', BigInteger),
    Column('id', Text),
    Column('video_created_at', Text),
    Column('views_count', BigInteger),
    Column('likes_count', BigInteger),
    Column('reports_count', BigInteger),
    Column('comments_count', BigInteger),
    Column('creator_id', Text),
    Column('created_at', Text),
    Column('updated_at', Text),
    Index('ix_videos_index', 'index')



class VideoSnapshots(Base):
    __tablename__ = "video_snapshots"
    Column('index', BigInteger),
    Column('id', Text),
    Column('video_id', Text),
    Column('views_count', BigInteger),
    Column('likes_count', BigInteger),
    Column('reports_count', BigInteger),
    Column('comments_count', BigInteger),
    Column('delta_views_count', BigInteger),
    Column('delta_likes_count', BigInteger),
    Column('delta_reports_count', BigInteger),
    Column('delta_comments_count', BigInteger),
    Column('created_at', Text),
    Column('updated_at', Text),
    Index('ix_video_snapshots_index', 'index')