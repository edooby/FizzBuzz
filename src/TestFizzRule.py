import unittest
from FizzRule import FizzRule


class TestFizzRule(unittest.TestCase):
    valuesForFizzRule = [ 3, 6, 15]

    def setUp(self):
        self.fizzrule = FizzRule()
    
    def tearDown(self):
        self.fizzrule = None

    def testGetAnswer(self):
        expected_value = 'Fizz'
        for input_value in self.valuesForFizzRule:
            result = self.fizzrule.getAnswer(input_value)
            self.assertEquals(expected_value, result)
