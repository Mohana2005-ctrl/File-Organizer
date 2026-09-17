from pathlib import Path
import shutil
import logging

from .config import FILE_CATEGORIES
logging.basicConfig(
    filename="logs/organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_category(file_path: Path) -> str:
    """Return the category for a file based on its extension."""

    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_path(destination: Path) -> Path:
    """Return a unique destination path if a filename already exists."""

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = f"{destination.stem}_{counter}{destination.suffix}"
        new_path = destination.parent / new_name

        if not new_path.exists():
            return new_path

        counter += 1


def organize_file(
    file_path: Path,
    target_folder: Path,
    dry_run: bool = False
) -> Path:
    """Move a file into its category folder."""

    category = get_category(file_path)

    category_folder = target_folder / category

    destination = category_folder / file_path.name
    destination = get_unique_path(destination)

    if dry_run:
        logging.info(
            f"[DRY RUN] Would move {file_path.name} "
            f"-> {category}/{destination.name}"
    )

        print(
            f"[DRY RUN] {file_path.name} "
            f"-> {category}/{destination.name}"
    )

    else:
        category_folder.mkdir(exist_ok=True)

        shutil.move(str(file_path), str(destination))

        logging.info(
            f"Moved {file_path.name} "
            f"-> {category}/{destination.name}"
    )

        print(
            f"Moved: {file_path.name} "
            f"-> {category}/{destination.name}"
    )


def organize_folder(folder_path: str, dry_run: bool = False) -> None:
    """Organize all files inside the specified folder."""

    folder = Path(folder_path)
    logging.info(f"Started organizing folder: {folder}")

    if not folder.exists():
        raise FileNotFoundError(f"Folder does not exist: {folder}")

    if not folder.is_dir():
        raise NotADirectoryError(f"Not a directory: {folder}")

    for file_path in folder.iterdir():

        if not file_path.is_file():
            continue

        organize_file(
            file_path,
            folder,
            dry_run=dry_run
        )