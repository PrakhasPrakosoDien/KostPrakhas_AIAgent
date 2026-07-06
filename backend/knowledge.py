import json
from pathlib import Path

def load_knowledge():
    base = Path(__file__).resolve().parent
    file_path = base / "data" / "kos_data.json"

    print("Current folder :", base)
    print("Looking for    :", file_path)
    print("Exists?        :", file_path.exists())

    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} tidak ditemukan")

    with file_path.open("r", encoding="utf-8") as f:
        return json.load(f)
