# tests/test_structure.py
import unittest
from plasterplan.structure import calculate_profiles

class TestStructure(unittest.TestCase):
    def test_calculate_profiles(self):
        self.assertEqual(calculate_profiles(10, 0.6), 17)
        self.assertEqual(calculate_profiles(5, 0.6), 9)

if __name__ == '__main__':
    unittest.main()
