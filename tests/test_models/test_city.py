import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_name(self):
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

if __name__ == "__main__":
    unittest.main()