'''
Created on Oct 24, 2012

@author: rosshe
'''

class FizzRule(object):
    
    def getAnswer(self, number):
        answer = "" 
        if number %3 == 0:
            answer = 'Fizz'
        return answer
