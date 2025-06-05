import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_name(self):
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

if __name__ == "__main__":
    unittest.main()