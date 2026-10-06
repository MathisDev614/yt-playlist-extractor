from typing import List
import yt_dlp
from .models import VideoMetadata

class PlaylistExtractor:
    def __init__(self, download_audio: bool = False, output_dir: str = "downloads"):
        self.download_audio = download_audio
        self.output_dir = output_dir

    def _get_ydl_opts(self) -> dict:
        opts = {
            'extract_flat': not self.download_audio,  # True = rapide, extrait seulement les métadonnées
            'quiet': True,
            'no_warnings': True,
        }
        if self.download_audio:
            opts.update({
                'format': 'bestaudio/best',
                'outtmpl': f'{self.output_dir}/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        return opts

    def extract(self, playlist_url: str) -> List[VideoMetadata]:
        videos: List[VideoMetadata] = []
        
        with yt_dlp.YoutubeDL(self._get_ydl_opts()) as ydl:
            # extract_flat permet de récupérer les infos de la playlist sans tout télécharger d'un coup
            info = ydl.extract_info(playlist_url, download=self.download_audio)
            
            if 'entries' not in info:
                # Lien vidéo unique plutôt que playlist
                entries = [info]
            else:
                entries = info['entries']

            for entry in entries:
                if not entry:
                    continue
                videos.append(VideoMetadata(
                    id=entry.get('id', ''),
                    title=entry.get('title', 'Sans titre'),
                    duration_seconds=entry.get('duration'),
                    channel=entry.get('uploader', 'Inconnu'),
                    url=entry.get('url') or f"https://www.youtube.com/watch?v={entry.get('id')}",
                    thumbnail_url=entry.get('thumbnail')
                ))

        return videos