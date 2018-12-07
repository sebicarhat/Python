'''
Created on Dec 11, 2017

@author: Sebi
'''
from MyException import *
from Passenger import *
from Aeroplane import *


class Validator():
    
    def validateName(self,name):
        if(not isinstance(name, str)):
            raise MyException("Incorrect data type",name)
        pass
    
    def validateNr(self,n):
        if(not isinstance(n, int)):
            raise MyException("Incorrect data type",n)
        pass
    
    def validatePassenger(self,p):
        if(not isinstance(p, Passenger)):
            raise MyException("Incorrect object type",p)
        self.validateName(p.getLName())
        self.validateName(p.getFName())
        self.validateName(p.getSeries())
        pass
    
    def validateAero(self,a):
        if(not isinstance(a, Aeroplane)):
            raise MyException("Incorrect object type",p)
        self.validateName(a.getName())
        self.validateNr(a.getNr())
        self.validateName(a.getDest())
        
        pass
    
        