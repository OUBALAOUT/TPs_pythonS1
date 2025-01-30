import unittest
from conversion import dollars_to_dirhams,meters_to_kilometers
class Testmodule(unittest.TestCase):
    def test_function1(self):
        self.assertEqual(dollars_to_dirhams(300),3006.0)   
        self.assertEqual(meters_to_kilometers(500), 0.5)
if __name__=="__main__":
    unittest.main()