import csv
import json
from pathlib import Path
from typing import List
from .models import VideoMetadata

class DataExporter:
    @staticmethod
    def to_json(videos: List[VideoMetadata], output_path: Path) -> None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        data = [video.to_dict() for video in videos]
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def to_csv(videos: List[VideoMetadata], output_path: Path) -> None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        if not videos:
            return
        
        fieldnames = ["id", "title", "duration_seconds", "channel", "url", "thumbnail_url"]
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for video in videos:
                writer.writerow(video.to_dict())