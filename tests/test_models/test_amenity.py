import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_name(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

if __name__ == "__main__":
    unittest.main()