import unittest

from flatlandSpaceStations import flatlandSpaceStations

class TestFlatlandSpaceStations(unittest.TestCase):
    def test_1(self):
        self.assertEqual(flatlandSpaceStations(20, [13,1,11,10,6]), 6)
    def test_2(self):
        self.assertEqual(flatlandSpaceStations(6,[0,1,2,4,3,5]), 0)
    def test_3(self):
        self.assertEqual(flatlandSpaceStations(5,[0,4]), 2)

if __name__ == '__main__':
    unittest.main()