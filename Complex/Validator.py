'''
Created on Nov 25, 2017

@author: Sebi
'''
from MyException import *
from ComplexNumber import *

class Validator():
    def validateNr(self,nr):
        if not isinstance(nr, float):
            raise MyExeption("Nu este numar real",nr)
        
    def validareInt(self,nr):
        if not isinstance(nr, int):
            raise MyExeption("Nu este numar intreg",nr)
        
    def validareComplex(self,comp):
        if not isinstance(comp, ComplexNumber):
            raise MyExeption("Nu este nr complex",comp)
        self.validateNr(comp.getReal())
        self.validateNr(comp.getImg())
        