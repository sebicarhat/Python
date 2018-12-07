'''
Created on Nov 16, 2017

@author: Sebi
'''
from numpy.lib.type_check import real, imag
from cmath import *
from numpy.ma.core import arctan
class ComplexNumber():
    
    def __init__(self,real=0,imag=0):
        self.__real=real
        self.__imag=imag
    
    def setReal(self, real):
        self.__real=real
    
    def setImag(self,imag):
        self.__imag=imag
    
    def getReal(self):
        return self.__real
    
    def getImg(self):
        return self.__imag
    
    def __repr__(self):
        real=self.__real
        img=self.__imag
        if(img>=0):
            return( str(real)+" + "+str(img)+"i")
        else:
            return( str(real)+" "+str(img)+"i")
        
    
    
    