import unittest
import sys
import os

# Ajouter le dossier Exercice1 au chemin Python
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, "../Exercice1"))
sys.path.append(parent_dir)

from conversion import dollars_to_dirhams, meters_to_kilometers

class TestConversion(unittest.TestCase):

    def test_dollars_to_dirhams(self):
        self.assertEqual(dollars_to_dirhams(1), 10)
        self.assertEqual(dollars_to_dirhams(100), 1000.0)
        self.assertEqual(dollars_to_dirhams(0), 0.0)
        self.assertAlmostEqual(dollars_to_dirhams(25.5), 255.0)

    def test_meters_to_kilometers(self):
        self.assertEqual(meters_to_kilometers(1000), 1.0)
        self.assertEqual(meters_to_kilometers(5000), 5.0)
        self.assertEqual(meters_to_kilometers(0), 0.0)
        self.assertAlmostEqual(meters_to_kilometers(1234), 1.234)

if __name__ == "__main__":
    unittest.main()
