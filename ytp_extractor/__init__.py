"""ytp_extractor - Module d'extraction de métadonnées et d'audios YouTube."""

from .models import VideoMetadata
from .extractor import PlaylistExtractor
from .exporter import DataExporter

__all__ = ["VideoMetadata", "PlaylistExtractor", "DataExporter"]
__version__ = "0.1.0"