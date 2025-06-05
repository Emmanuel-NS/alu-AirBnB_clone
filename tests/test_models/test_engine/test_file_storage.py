import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()
        self.file_path = "file.json"
        # Clean up file.json before each test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects.clear()

    def tearDown(self):
        """Clean up after test."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects.clear()

    def test_file_path(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        bm = BaseModel()
        self.storage.new(bm)
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        FileStorage._FileStorage__objects.clear()
        self.storage.reload()
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, self.storage.all())

    def test_base_model_save(self):
        bm = BaseModel()
        old_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(bm.updated_at, old_updated_at)

if __name__ == "__main__":
    unittest.main()