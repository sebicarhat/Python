'''
Created on Nov 23, 2017

@author: Sebi
'''
from Repository import *
import Validator import *
from Contact import *

class Controller():
    
    def __init__(self,repo):
        self.__repo=repo
        self.__v=Validator()
        
    def addContact(self,contact):
        self.__v.validateContact(contact)
        self.__repo.addContact(contact)
        
    def removeContact(self,contact):
        self.__v.validateContact(contact)
        self.__repo.removeContact(contact)
        
    def updateContact(self,oldContact,newContact):
        self.__v.validateContact(contact)
        self.__repo.updateContact(newContact,oldContact)
        
    def searchContact(self,nr):
        self.__v.ValidatePhoneNr(nr)
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
    
                