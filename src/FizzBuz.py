'''
Created on Oct 17, 2012

@author: rosshe
'''

class FizzBuz(object):
    def getanswer(self,numbers):
        
        list_to_return = []
        
        for number in numbers:
            answer = None
            
            if number % 5 == 0:
                answer = 'Buz'
                
            if number % 3 == 0:
                answer = 'Fizz'
                
            if answer == None:
                answer = number              
                
            list_to_return.append(answer)
            
            
        return list_to_return
        
        
        

