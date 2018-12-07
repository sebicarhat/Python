'''
Created on Nov 16, 2017

@author: Sebi
'''
from Contact import import*

class Repository():
    
    def __init__(self):
        self.__contactList=[]
        
    def addContact(self,contact):
        self.__contactList.append(contact)
        
    def removeContact(self,contact):
        self.__contactList.remove(contact)
        
    def updateContact(self,oldContact,newContact):
        index=self.__contactList.index(oldContact)
        self.__contactList[index]=newContact
    
    def getAllContacts(self):
        return self.__contactList[:]
    
