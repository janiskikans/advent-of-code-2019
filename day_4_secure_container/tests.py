import unittest
import day_4A
import day_4B

class TestDay4(unittest.TestCase):
    
    # Part A
    
    def test_has_same_two_adjecent_digits_should_be_false(self):
        result = day_4A.has_same_two_adjecent_digits(1023456)
        self.assertEqual(result, False)
        
    def test_has_same_two_adjecent_digits_should_be_true(self):
        result = day_4A.has_same_two_adjecent_digits(1223456)
        self.assertEqual(result, True)
        
    def test_has_all_increasing_digits_should_be_false(self):
        result = day_4A.has_all_increasing_digits(str(12341))
        self.assertEqual(result, False)
        
    def test_has_all_increasing_digits_should_be_true(self):
        result = day_4A.has_all_increasing_digits(str(112345))
        self.assertEqual(result, True)
        
    # Part B
        
    def test_B_has_same_two_adjecent_digits_should_be_false(self):
        result = day_4B.has_same_two_adjecent_digits(str(123444))
        self.assertEqual(result, False)
        
    def test_B_has_same_two_adjecent_digits_should_be_true(self):
        result = day_4B.has_same_two_adjecent_digits(str(111122))
        self.assertEqual(result, True)
        
    def test_B_has_all_increasing_digits_should_be_false(self):
        result = day_4B.has_all_increasing_digits(str(1234442))
        self.assertEqual(result, False)
        
    def test_B_has_all_increasing_digits_should_be_true(self):
        result = day_4B.has_all_increasing_digits(str(111122))
        self.assertEqual(result, True)