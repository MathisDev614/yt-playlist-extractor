import argparse
from pathlib import Path

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Outil CLI pour extraire les métadonnées et audios d'une playlist YouTube."
    )
    
    parser.add_argument(
        "url",
        type=str,
        help="L'URL de la playlist ou de la vidéo YouTube"
    )
    
    parser.add_argument(
        "-f", "--format",
        choices=["json", "csv"],
        default="json",
        help="Format de sortie pour les métadonnées (défaut: json)"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("output/playlist_meta"),
        help="Chemin de base du fichier de sortie (sans extension)"
    )
    
    parser.add_argument(
        "--download-audio",
        action="store_true",
        help="Télécharge et convertit également les pistes en MP3"
    )

    return parser.parse_args()