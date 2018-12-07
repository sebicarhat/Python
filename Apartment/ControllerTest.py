'''
Created on Dec 6, 2017

@author: Sebi
'''
import unittest
from Controller import *
from Apartament import *

class Test(unittest.TestCase):


    def testFilter(self):
        l=[Apartament(1, "Nume1", 100),Apartament(2, "Nume2", 200)]
        assert Controller(l).filter(100)[1]==300
        assert Controller(l).filter(100)[1]==200


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFilter']
    unittest.main()