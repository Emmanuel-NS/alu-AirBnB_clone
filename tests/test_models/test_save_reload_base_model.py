#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.file_path = "file.json"
        # Remove file.json if it exists to start fresh
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

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

    def test_save_and_reload(self):
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        # Clear objects and reload
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()