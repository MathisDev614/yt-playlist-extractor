# YouTube Playlist Extractor

Outil CLI en Python permettant d'extraire rapidement les métadonnées de playlists ou vidéos YouTube (titres, durées, chaînes, miniatures) aux formats JSON/CSV, avec option de téléchargement audio (MP3).

## Fonctionnalités

- Extraction rapide des métadonnées sans téléchargement vidéo lourd (`extract_flat`).
- Export structuré en **JSON** ou **CSV**.
- Option d'extraction et de conversion des pistes audio en **MP3** (192 kbps).
- Architecture modulaire et typée (`dataclasses`, séparation CLI / Service / Persistance).

## Prérequis

- Python 3.10+
- [FFmpeg](https://ffmpeg.org/) (nécessaire uniquement pour la conversion audio MP3)

## Installation

```bash
# Cloner le dépôt
git clone [https://github.com/](https://github.com/)<ton-user>/yt-playlist-extractor.git
cd yt-playlist-extractor

# Créer et activer l'environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Sur Windows : .venv\Scripts\Activate.ps1

# Installer les dépendances
pip install -r requirements.txt
```

## Utilisation

### 1. Extraire les métadonnées en JSON (défaut)
```bash
python main.py "[https://www.youtube.com/playlist?list=ID_PLAYLIST](https://www.youtube.com/playlist?list=ID_PLAYLIST)"
```
Le fichier est généré par défaut dans `output/playlist_meta.json`.

### 2. Exporter au format CSV avec chemin personnalisé
```bash
python main.py "[https://www.youtube.com/playlist?list=ID_PLAYLIST](https://www.youtube.com/playlist?list=ID_PLAYLIST)" -f csv -o export/ma_playlist
```

### 3. Extraire les métadonnées et télécharger les pistes audio en MP3
```bash
python main.py "[https://www.youtube.com/playlist?list=ID_PLAYLIST](https://www.youtube.com/playlist?list=ID_PLAYLIST)" --download-audio
```

## Structure du projet

```text
yt-playlist-extractor/
├── ytp_extractor/
│   ├── cli.py          # Analyse des arguments en ligne de commande
│   ├── models.py       # Dataclass VideoMetadata
│   ├── extractor.py    # Logique d'interaction avec yt-dlp
│   └── exporter.py     # Gestionnaires d'export (JSON, CSV)
├── main.py             # Point d'entrée de l'application
└── requirements.txt
```