from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class VideoMetadata:
    id: str
    title: str
    duration_seconds: Optional[int]
    channel: str
    url: str
    thumbnail_url: Optional[str]

    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire pour l'export."""
        return asdict(self)