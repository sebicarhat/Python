'''
Created on Nov 16, 2017

@author: Sebi
'''
from Repository import *
import Repository

class Controller():
    
    def __init__(self):
        self.__repo=Repository()
        
    def addContact(self,contact):
        self.__repo.addContact(contact)
        
    def removeContact(self,contact):
        self.__repo.removeContact(contact)
        
    def updateContact(self,oldContact,newContact):
        self.__repo.updateContact(newContact,oldContact)
        
    def searchContact(self,nr):
        for con in self._repo.getAllContacts():
            if(nr==con.getNumber()):
                return con
            
    def groupByPrefix(self):
        dict={}
        for con in self.__repo.getAllContacts():
            pref=con.getNumber()[:3]
            values=dict.get(prefix,[])
            values.append(con)
            dict[prefix]=values
        return dict
    
                