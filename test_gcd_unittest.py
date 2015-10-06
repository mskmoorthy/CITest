import unittest
from mygcd import gcd
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_1(self):
        self.assertEqual( gcd(0,0),-1)
 
    def test_2(self):
        self.assertEqual( gcd(23,46),23)

    def test_3(self):
        self.assertEqual(gcd(122,61),61)

    def test_4(self):
        self.assertEqual(gcd(222222222222200,11111110000000000012),4)

    def test_5(self):
        self.assertEqual(gcd(233,144),1)

    def test_6(self):
        self.assertEqual(gcd(23,0),-1)
        
if __name__ == '__main__':
    unittest.main()
