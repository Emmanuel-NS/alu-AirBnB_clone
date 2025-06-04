#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_id_is_string(self):
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_created_at_is_datetime(self):
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)

    def test_save_updates_updated_at(self):
        bm = BaseModel()
        old_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(bm.updated_at, old_updated_at)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_to_dict_returns_dict(self):
        bm = BaseModel()
        bm.name = "My First Model"
        bm.my_number = 89
        d = bm.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "My First Model")
        self.assertEqual(d['my_number'], 89)
        self.assertIsInstance(d['created_at'], str)
        self.assertIsInstance(d['updated_at'], str)

    def test_str_method(self):
        bm = BaseModel()
        s = str(bm)
        self.assertIn("[BaseModel]", s)
        self.assertIn(bm.id, s)

if __name__ == '__main__':
    unittest.main()

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))