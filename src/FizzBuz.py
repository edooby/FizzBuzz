'''
Created on Oct 17, 2012

@author: rosshe
'''

class FizzBuzz(object):
    
    
    def GetAnswerforBuzzRule(self): 
        self.answer = 'Buzz'
        return self.answer
    
    def GetAnswerforFizzRule(self): 
        self.answer = 'Fizz'
        return self.answer
    
    def GetAnswerforFizzBuzzRule(self): 
        self.answer = 'FizzBuzz'
        return self.answer
    
    def getanswer(self,numbers):
        list_to_return = []
          
        for number in numbers:
            answer = None
            if number % 5 == 0:
                answer = self.GetAnswerforBuzzRule()
                
            if number % 3 == 0:
                answer = self.GetAnswerforFizzRule()
            
            if number % 5 == 0 and number % 3 == 0:
                answer = self.GetAnswerforFizzBuzzRule()
                
            if answer == None:
                answer = number              
                
            list_to_return.append(answer)
            
            
        return list_to_return
        
        
        

