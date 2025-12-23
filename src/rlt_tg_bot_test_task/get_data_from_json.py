import json
import functools
from pathlib import Path

import pandas as pd


def accumulate_all_snapshots(series_data):
    return functools.reduce(
        lambda x, y: x + y,
        series_data,
        []
    )


videos_json_path = Path(__file__).parents[2] / "videos.json"
js = json.loads(videos_json_path.read_text())
videos = js["videos"]


df_videos = pd.DataFrame(videos)
videos_snapshots = df_videos["snapshots"]
df_videos = df_videos.drop(columns=["snapshots"])

df_video_snapshots = pd.DataFrame(
    videos_snapshots.agg(accumulate_all_snapshots)
)
print(df_videos.info())
