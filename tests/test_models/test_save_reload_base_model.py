#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def test_file_path(self):
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        storage = FileStorage()
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_all(self):
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        storage = FileStorage()
        bm = BaseModel()
        storage.new(bm)
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, storage.all())

    def test_save_and_reload(self):
        storage = FileStorage()
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        storage._FileStorage__objects = {}
        storage.reload()
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, storage.all())


if __name__ == "__main__":
    unittest.main()