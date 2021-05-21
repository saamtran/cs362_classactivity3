import unittest
import SAMUEL_TRAN_HW1

class testCaseLeapYear(unittest.TestCase):
    def test_SAMUEL_TRAN_HW1(self):
        self.assertEqual(SAMUEL_TRAN_HW1.mainFunction(2020), True)
    

class testCaseLeapYear2(unittest.TestCase):
    def test_SAMUEL_TRAN_HW1(self):
        self.assertEqual(SAMUEL_TRAN_HW1.mainFunction(-250), False)

class TestCaseLeapYear3(unittest.TestCase):
    def test_SAMUEL_TRAN_HW1(self):
        self.assertEqual(SAMUEL_TRAN_HW1.mainFunction(2000), True)
    
class TestCaseLeapYear4(unittest.TestCase):
    def test_SAMUEL_TRAN_HW1(self):
        self.assertEqual(SAMUEL_TRAN_HW1.mainFunction(0), False)

if __name__ == '__main__':
    unittest.main()