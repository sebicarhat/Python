'''
Created on Nov 16, 2017

@author: Sebi
'''
import unittest
from Repository import *
import Contact

class Test(unittest.TestCase):


    def testAdd(self):
        repo=Repository()
        c=Contact("Nume","123")
        repo.addContact(c)
        assert repo.getAllContacts()[0]==c
        assert len(repo.getAllContacts())==1
        pass
    
    def testRemove(self):
        repo=Repository()
        c=Contact("Nume","123")
        repo.addContact(c)
        repo.removeContact(c)
        assert len(repo.getAllContacts())==0
        
    def testUpdate(self):
        repo = Repository()
        c=Contact("Nume1","123")
        repo.addContact(c)
        c2=Contact("Nume2","123")
        repo.updateContact(c2,c)
        assert repo.getAllContacts()[0]==c2

    def testGetAllContact(self):
        repo = Repository()
        c=Contact("Nume","123")
        repo.addContact(c)
        assert len(repo.getAllContacts())==1
        assert repo.getAllContacts()[0]==c
        
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()