'''
Created on Oct 17, 2012

@author: rosshe
'''
import unittest
from FizzBuz import FizzBuzz


class TestFizzBuzz(unittest.TestCase):
    valuesForDefaultRule = [ ([1], [1]) , ([2], [2]) ]
    valuesForFizzRule = [ [3], [6]]
    valuesForBuzzRule = [[5], [10]]
    valuesForFizzBuzzRule = [[15], [30]]

    def setUp(self):
        self.fizzbuzz = FizzBuzz()
    
    def tearDown(self):
        pass

    def testGetAnswerfordefaultRules(self):
        for value in self.valuesForDefaultRule:
            input_value = value[0]
            expected_value = value[1]
            
            self.executeTestOfGetAnswer(expected_value, input_value)

    def testGetAnswerforFizz(self):
        expected_value = ['Fizz']

        for input_value in self.valuesForFizzRule:
            self.executeTestOfGetAnswer(expected_value, input_value)
    
    def testGetAnswerforBuzz(self):
        expected_value = ['Buzz']

        for input_value in self.valuesForBuzzRule:
            self.executeTestOfGetAnswer(expected_value, input_value)
    
    def testGetAnswerforFizzBuzz(self):
        expected_value= ['FizzBuzz']
        
        for input_value in self.valuesForFizzBuzzRule:
            self.executeTestOfGetAnswer(expected_value, input_value)
    
    def testGetAnswerwithMultiValues(self):
        input_value = [1,2,3]
        expected_value = [1,2,'Fizz']
        return self.executeTestOfGetAnswer(expected_value, input_value)
        
    def executeTestOfGetAnswer(self,expected_value, input_value):
        result =self.fizzbuzz.getanswer(input_value)
        return self.assertEquals(expected_value, result)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()