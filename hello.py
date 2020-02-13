# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 20:35:53 2020

@author: azucker
"""

class sampleclass: 
    count = 0     # class attribute 
  
    def increase(self): 
        sampleclass.count += 1
  
# Calling increase() on an object 
s1 = sampleclass() 
s1.increase()         
print (s1.count) 
  
# Calling increase on one more 
# object 
s2 = sampleclass() 
s2.increase() 
print (s2.count) 
  
print sampleclass.count 