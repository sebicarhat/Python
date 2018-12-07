'''
Created on Dec 11, 2017

@author: Sebi
'''
import unittest
from Aeroplane import *
from Passenger import *
class Test(unittest.TestCase):


    def testAeropplane(self):
        obj=Aeroplane("Aeroplane",1,"Company",100,"Dest",[Passenger("Prenume1","Nume1",23),Passenger("Prenume2","Nume2",24)])
        assert obj.getName()=="Aeroplane"
        assert obj.getNr()==1
        assert obj.getCompany()=="Company"
        assert obj.getNrSeats()==100
        assert  obj.getDest()=="Dest"
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()