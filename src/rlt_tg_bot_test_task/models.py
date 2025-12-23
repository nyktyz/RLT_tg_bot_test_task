from uuid import UUID
import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import(
    Mapped,
    mapped_column,
    relationship,
)

from rlt_tg_bot_test_task.database import Base


class Videos(Base):

    __tablename__ = "videos"

    id: Mapped[UUID] = mapped_column(
        index=True, primary_key=True, unique=True
    )
    views_count: Mapped[int] = mapped_column()
    video_created_at: Mapped[datetime.datetime] = mapped_column()
    likes_count: Mapped[int] = mapped_column()
    reports_count: Mapped[int] = mapped_column()
    comments_count: Mapped[int] = mapped_column()
    creator_id: Mapped[UUID] = mapped_column()
    created_at: Mapped[datetime.datetime] = mapped_column()
    updated_at: Mapped[datetime.datetime] = mapped_column()

    video_snapshots: Mapped[list["VideoSnapshots"]] = relationship(back_populates="video")


class VideoSnapshots(Base):
    __tablename__ = "video_snapshots"
    
    id: Mapped[UUID] = mapped_column(
        index=True, primary_key=True, unique=True
    )
    video_id: Mapped[UUID] = mapped_column(
        ForeignKey("videos.id"), index=True
    )
    views_count: Mapped[int] = mapped_column()
    likes_count: Mapped[int] = mapped_column()
    reports_count: Mapped[int] = mapped_column()
    comments_count: Mapped[int] = mapped_column()
    delta_views_count: Mapped[int] = mapped_column()
    delta_likes_count: Mapped[int] = mapped_column()
    delta_reports_count: Mapped[int] = mapped_column()
    delta_comments_count: Mapped[int] = mapped_column()
    created_at: Mapped[datetime.datetime] = mapped_column()
    updated_at: Mapped[datetime.datetime] = mapped_column()

    video: Mapped["Videos"] = relationship(back_populates="video_snapshots")
    