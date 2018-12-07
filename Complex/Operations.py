'''
Created on Nov 23, 2017

@author: Sebi
'''
from ComplexNumber import *
from Validator import *
class Operations():
    def __init__(self):
        self.__val=Validator()
    
    def conjugat(self,nrC):
        self.__val.validareComplex(nrC)
        return ComplexNumber(nrC.getReal(),nrC.getImg())
    
    def reprCart(self,nrC):
        self.__val.validareComplex(nrC)
        return "Real:"+str(nrC.getReal())+"\nImag:"+str(nrC.getImg())+"\n"
        
    def reprGeom(self,nrC):
        self.__val.validareComplex(nrC)
        real=nrC.getReal()
        img=nrC.getImg()
        return "Raza: "+str(abs(complex(real,img)))+"\nUnghiul:"+str(phase(complex(real,img)))+"\n"
        
    def putere(self,nrC,p):
        self.__val.validareComplex(nrC)
        c=ComplexNumber(nrC.getReal(),nrC.getImg())
        c2=c
        for i in range(0,p-1):
            c2=self.multyplyBy(c2, c)
        return str(c2)
        
    def radical(self,nrC):
        self.__val.validareComplex(nrC)
        real=nrC.getReal()
        img=nrC.getImg()
        return str(sqrt(real+img*1j))
    
    def exp(self,nrC):
        self.__val.validareComplex(nrC)
        real=nrC.getReal()
        img=nrC.getImg()
        rez=exp(real+img*1j)
        return str(complex(round(rez.real,2),round(rez.imag,2))+"\n")
        
    def conj(self,nrC):
        self.__val.validareComplex(nrC)
        c=ComplexNumber(nrC.getReal(),-nrC.getImg())
        return (c)
        
    def multyplyByReal(self,nrC,x):
        self.__val.validareComplex(nrC)
        return ComplexNumber(nrC.getReal()*x,nrC.getImg()*x)
    
    def multyplyByImg(self,nrC,x):
        self.__val.validareComplex(nrC)
        return ComplexNumber((-1)*nrC.getImg()*x,nrC.getReal()*x)
        
    def add(self,comp1,comp2):
        self.__val.validareComplex(comp1)
        self.__val.validareComplex(comp2)
        return ComplexNumber(comp1.getReal()+comp2.getReal(),comp1.getImg()+comp2.getImg())
        
    def multyplyBy(self,comp1,comp2):
        self.__val.validareComplex(comp1)
        self.__val.validareComplex(comp2)
        real=comp1.getReal()
        img=comp2.getImg()
        real2=comp2.getReal()
        img2=comp2.getImg()
        real3=real*real2+(-1)*img*img2
        img3=real*img2+real2*img
        return ComplexNumber(real3,img3)
        
    def matrixRepr(self,nrC):
        self.__val.validareComplex(nrC)
        return str(nrC.getReal())+" "+str(-nrC.getImg())+"\n"+str(nrC.getReal())+" "+str(nrC.getImg()+"\n")    
    
