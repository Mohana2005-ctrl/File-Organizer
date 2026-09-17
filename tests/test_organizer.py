import unittest
import tempfile
from pathlib import Path

from file_organizer.organizer import (
    get_category,
    get_unique_path,
    organize_file,
    organize_folder
    )


class TestFileOrganizer(unittest.TestCase):

    def test_image_category(self):
        file_path = Path("photo.jpg")

        result = get_category(file_path)

        self.assertEqual(result, "Images")
        
    def test_pdf_category(self):
        file_path = Path("report.pdf")

        result = get_category(file_path)

        self.assertEqual(result, "Documents")

    def test_unknown_category(self):
        file_path = Path("random.xyz")

        result = get_category(file_path)

        self.assertEqual(result, "Others")

    def test_unique_path(self):
        test_file = Path("test_file.txt")

        test_file.touch()

        result = get_unique_path(test_file)

        self.assertEqual(result, Path("test_file_1.txt"))

        test_file.unlink()
    
    def test_organize_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:

            folder = Path(temp_dir)

            test_file = folder / "photo.jpg"
            test_file.write_text("test image")

            organize_file(test_file, folder)

            expected_file = folder / "Images" / "photo.jpg"

            self.assertTrue(expected_file.exists())
            self.assertFalse(test_file.exists())

    def test_dry_run_does_not_move_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:

            folder = Path(temp_dir)

            test_file = folder / "photo.jpg"
            test_file.write_text("test image")

            organize_file(
                test_file,
                folder,
                dry_run=True
            )

            self.assertTrue(test_file.exists())

            expected_file = folder / "Images" / "photo.jpg"

            self.assertFalse(expected_file.exists())

    def test_invalid_folder(self):
        with self.assertRaises(FileNotFoundError):
            organize_folder("this_folder_does_not_exist")


if __name__ == "__main__":
    unittest.main()