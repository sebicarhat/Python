'''
Created on Nov 23, 2017

@author: Sebi
'''
from MyException import *
from Contact import *

class Validator():
    def validatePhoneNr(self,nr):
        if not isinstance(nr, str):
            raise MyExeption("Not string",nr)
        if(len(nr)<13):
            raise MyExeption("Not lungime",nr)
        if(number[0]!="+"):
            raise MyExeption("Incorrect",nr)
        cifre=number[1:]
        if(cifre.isdigit()==False)
            raise MyExeption("Is not digit",nr)
    
    def validateContact(self,contact):
        if not isinstance(contact, Contact):
            raise MyExeption("Not instance",contact)
        
        self.validatePhoneNr(contact.getNumber())
        name=contact.getName()
        if not isinstance(name, str):
            raise MyExeption("",name)
        if len(name<2):
            raise MyExeption("",name)
        
        