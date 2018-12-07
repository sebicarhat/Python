'''
Created on Dec 11, 2017

@author: Sebi
'''
import unittest
from Passenger import *

class Test(unittest.TestCase):


    def testPassenger(self):
        p=Passenger("Prenume","Nume",23)
        assert p.getFName()=="Prenume"
        assert p.getLName()=="Nume"
        assert p.getSeries()==23
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPassenger']
    unittest.main()