import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_text(self):
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")

if __name__ == "__main__":
    unittest.main()