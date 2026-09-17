import json
from pathlib import Path


CONFIG_FILE = Path(__file__).parent.parent / "config" / "categories.json"


def load_categories() -> dict:
    """Load file categories from the JSON configuration file."""

    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


FILE_CATEGORIES = load_categories()