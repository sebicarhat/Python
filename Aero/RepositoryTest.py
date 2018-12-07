'''
Created on Dec 13, 2017

@author: Sebi
'''
import unittest

from Repository import *
from Aeroplane import *
from Passenger import *

class Test(unittest.TestCase):


    def testAddAero(self):
        repo=Repository()
        a=Aeroplane("Nume1",1,"Company",250,"Dest",[])
        repo.addAero(a)
        assert repo.getAllAeroplanes()[0]==a
        assert len(repo.getAllAeroplanes())==1
        pass
    
    def testAddPassenger(self):
        repo=Repository()
        p=Passenger("Prenume1","Nume1","abv")
        repo.addPassenger(p)
        assert repo.getPassengerList()[0]==p
        assert len(repo.getPassengerList())==1
        pass
    
    def testUpdatePassenger(self):
        repo=Repository()
        p1=Passenger("Prenume1","Nume1","abv")
        repo.addPassenger(p1)
        p2=Passenger("Prenume1","Nume1","abc")
        repo.updatePassenger(p1, p2)
        assert repo.getPassengerList()[0]==p2
        
    def testUpdateAero(self):
        repo=Repository()
        a=Aeroplane("Nume1",1,"Company",250,"Dest",[])
        repo.addAero(a)
        a2=Aeroplane("Nume1",1,"Company",250,"Dest",[Passenger("Prenume1","Nume1","abc")])
        repo.updateAero(a, a2)
        assert repo.getAllAeroplanes()[0]==a2
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()