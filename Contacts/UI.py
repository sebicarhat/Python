'''
Created on Nov 16, 2017

@author: Sebi
'''
from Controller import *
import Contact
from email.mime import application

class UI():
    
    def __init__(self):
        self.__ctrl=Controller()
    
    def printMenu(self):
        print("""1.Adauga
        2.Sterge
        3.Update
        4.Group
        5.Cauta
        6.Exit""")
    
    def readContact():
        nume=int(input("Nume:"))
        nr=int(input("Numar:"))
        c=Contact(nume,nr)
        return c
    
    def run(self):
        stop=False
        while(stop==False):
            self.printMenu()
            opt=int(input("Enter an option:"))
            if(opt==1):
                con=self.readContact()
                self.__ctrl.addContact(con)
            if(opt==2):
                con=self.readContact()
                self.__ctrl.removeContact(con)
            if(opt==3):
                oldContact=self.readContact()
                newContact=self.readContact()
                self.__ctrl.updateContact(newContact, oldContact)
            if(opt==4):
                print(self.__ctrl.groupByPrefix())
            if(opt==5):
                con=self.readContact()
                print(self.__ctrl.searchContact(con))
            if(opt==6):
                stop=True
                
UI().run()
        