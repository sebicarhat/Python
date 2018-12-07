'''
Created on Nov 16, 2017

@author: Sebi
'''
import unittest
from ComplexNumber import *

class Test(unittest.TestCase):


    def testNumber(self):
        c=ComplexNumber(3,123)
        assert c.getReal()==3
        assert c.getImg()==123
        c.setimag(44)
        assert c.getImg()==44
        c.setReal(2)
        assert c.getReal()==2
        assert c.getImg()=44
    pass

    def testReprtCart(self):
        c=ComplexNumber(2,3)
        assert c.reprCart()=="Raza:"+str(2)+"\nImag:"+str(3)
        
    
    def testConj(self):
        c=complexNumber(2,3)
        c2=c.conj()
        assert c2.getReal()==2
        assert c2.getImg()==-3
        c2=c2.conj()
        assert c2.getReal()==-2
        assert c2.getImg()==3
        assert c.getReal()==2
    
    def testMultiplyByReal(self):
        c=ComplexNumber(2,3)
        c2=c.multyplyByReal(2)
        assert c2.getReal()==4
        assert c2.getImg()==6
        c2=c.multyplyByReal(1)
        assert c2.getReal()==4
        assert c2.getImg()==6
        assert c.getReal()==2
    
    def testMultiplyByImg(self):
        c=ComplexNumber(3,4)
        c2=c.multyplyByImg(3)
        assert c2.getReal()==-12
        assert c2.getImg()==9
        c2=c.multyplyByImg(3)
        assert c2.getReal()==-12
        assert c2.getImg()==9
        assert c.getReal()==3
        
    def testMultiplyBy(self):
        c=ComplexNumber(3,4)
        c2=ComplexNumber(3,-2)
        c3=c.multyplyBy(c2)
        assert c3.getReal()==17
        assert c3.getImg()==6
        c2=ComplexNumber(1,1)
        c3=c.multyplyBy(c2)
        assert c.getReal()==3
        assert c.getImg()==4
        assert c.getReal()==3
    
    def testAdd(self):
        c=ComplexNumber(3,4)
        c2=ComplexNumber(1,2)
        c3=c.add(c2)
        assert c3.getReal()==4
        assert c3.getImg()==6
        c3=c.add(ComplexNumber(2,2))
        assert c3.getReal()==5
        assert c3.getImg()==6
        assert c.getReal()==3
    
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()