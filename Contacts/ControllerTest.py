'''
Created on Nov 16, 2017

@author: Sebi
'''
from Controller import *
import unittest
import Contact
from pip._vendor.cachecontrol import controller

class Test(unittest.TestCase):
    
    def testSearchContact(self):
        c=Controller()
        con=Contact("Nume","123")
        c.addContact(con)
        found=Controller.searchContact("123")
        assert found==con
    
    def testGroupByPrefix(self):
        c=Controller()
        c.addContact("Nume1","1234")
        c.addContact("Nume","1235")
        c.addContact("Nume3","1224")
        assert len(c.groupByPrefix()["123"])==2
        assert len(c.groupByPrefix()["122"])==1
    
if __name__=="__main__":
    unittest.main()
    
        