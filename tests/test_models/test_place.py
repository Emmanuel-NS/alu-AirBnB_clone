import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_name(self):
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

if __name__ == "__main__":
    unittest.main()