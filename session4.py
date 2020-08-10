#!/usr/bin/env python
# coding: utf-8
# In[70]:
import random
from operator import and_ as and_operator
from operator import or_ as or_operator
import math
from decimal import Decimal
# In[168]:
class Qualean():
    def __init__(self, x):
        if(x not in [0,1,-1,1.0,-1.0]):
            raise ValueError ('Number should be in  [0,1,-1,1.0,-1.0]')
            #print("Error")
        self.mask = Decimal(random.uniform(-1,1))
        self.num = round(x*self.mask,10)  
    def __eq__(self, value):
        if isinstance(value, Qualean):
            return self.num == value.num
        return self.num == Decimal(value)
    def __float__(self):        
        return float(self.num)
    def __add__(self, value):
        if isinstance(value, Qualean):
            return self.num + value.num
        return self.num + Decimal(value)
    def __mul__(self, value):
        if isinstance(value, Qualean):
            return self.num * value.num
        return self.num * Decimal(value)
    def __ge__(self,y):
        return self.num >= Decimal(y*random.uniform(-1,1))
    def __gt__(self,y):        
        return self.num > Decimal(y*random.uniform(-1,1))        
    def __invert__(self):
        self.num *= -1
        self.__invertsign__()   
    def __invertsign__(self):   
        return self.num        
    def __le__(self, value):
        if isinstance(value, Qualean):
            return self.num <= value.num
        return self.num <= Decimal(value)
    def __lt__(self, value):
        if isinstance(value, Qualean):
            return self.num < value.num
        return self.num < Decimal(value)
    def __bool__(self): 
        return False if self.num == 0 else True
    def __sqrt__(self):
        return self.num.sqrt()    
    def __str__(self):        
        return str(self.num)
    def qualean(self):
        return self.num 
    def __repr__(self):
        return f"{self.num}"        
    def __or__(self , y):        
        return self.num if self.num != 0 else y*random.uniform(-1,1) if y*random.uniform(-1,1) != 0 else False    
    def __and__(self, value):
        if not isinstance(value, Qualean):
            return False
        if self.num == 0 or value.num == 0:
            return False
        return True