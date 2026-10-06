import sys
from ytp_extractor.cli import parse_arguments
from ytp_extractor.extractor import PlaylistExtractor
from ytp_extractor.exporter import DataExporter

def main():
    args = parse_arguments()
    print(f"[*] Analyse de l'URL : {args.url}")

    try:
        extractor = PlaylistExtractor(download_audio=args.download_audio)
        videos = extractor.extract(args.url)
        print(f"[+] {len(videos)} vidéo(s) trouvée(s).")

        out_file = args.output.with_suffix(f".{args.format}")
        if args.format == "json":
            DataExporter.to_json(videos, out_file)
        else:
            DataExporter.to_csv(videos, out_file)

        print(f"[+] Métadonnées exportées avec succès dans : {out_file}")

    except Exception as e:
        print(f"[!] Erreur lors de l'exécution : {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()