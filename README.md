# File Organizer

A Python-based command-line tool that automatically organizes files into categorized folders based on their file extensions.

## Features

- Automatically categorizes files by extension
- Supports configurable file categories using JSON
- Handles duplicate filenames safely
- Dry-run mode to preview changes without moving files
- Logging of file organization activities
- Input validation and error handling
- Unit tests using Python's built-in `unittest` framework

## Project Structure

```text
File Organizer/
├── config/
│   └── categories.json
├── file_organizer/
│   ├── config.py
│   ├── organizer.py
├── tests/
│   └── test_organizer.py
├── logs/
├── main.py
├── requirements.txt
└── README.md