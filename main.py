import argparse
import logging

from file_organizer.organizer import organize_folder


def main():
    parser = argparse.ArgumentParser(
        description="Organize files into folders based on their file type."
    )

    parser.add_argument(
        "folder",
        help="Path to the folder you want to organize"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving files"
    )

    args = parser.parse_args()

    try:
        organize_folder(
            args.folder,
            dry_run=args.dry_run
        )

        if args.dry_run:
            print("\nDry run completed. No files were moved.")
        else:
            print("\nFiles organized successfully!")

    except (FileNotFoundError, NotADirectoryError) as error:
        logging.error(error)
        print(f"Error: {error}")


if __name__ == "__main__":
    main()