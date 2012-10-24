'''
Created on Oct 17, 2012

@author: rosshe
'''

class FizzBuzz(object):
    
    def __init__(self):
        self.rules = [self.GetAnswerforFizzRule , self.GetAnswerforBuzzRule]
        
    def GetAnswerforBuzzRule(self, number):
        answer = "" 
        if number %5 == 0:
            answer = 'Buzz'
        return answer
    
    def GetAnswerforFizzRule(self, number): 
        answer = "" 
        if number %3 == 0:
            answer = 'Fizz'
        return answer
    
    def getanswer(self,numbers):
        list_to_return = []
        answer = None
        
        for number in numbers:
            answer = ""
            for rule in self.rules:
                answer += rule(number)
            if answer == "":
                answer = number              
                
            list_to_return.append(answer)
            
            
        return list_to_return
        
        
        

