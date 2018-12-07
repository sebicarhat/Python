'''
Created on Jan 11, 2018

@author: Sebi
'''
from MyException import *
from Book import *
from Reader import *
from tkinter import messagebox
import numpy
class Validator():
    
    def validateNrEx(self,n):
        #if(n<1):
         #   tk.messagebox.showerror("Eroare", "Nu mai sunt exemplare disponibile pentru aceasta carte")
         messagebox.showerror(message=str(n))
         
    def validateName(self,name):
        if(not isinstance(name, str)):
            raise MyException("Incorrect data type",name)
    
    def validateNr(self,n):
        def isanumber(a):
            try:
                float(str(a))
                bool_a = True
            except:
                bool_a = False
            return bool_a
        if(not isanumber(n)):
            raise MyException("Incorrect data type",n)
        pass
    
    def validateBook(self,b):
        if(not isinstance(b, Book)):
            raise MyException("Incorrect object type",p)
        self.validateNr(b.getNrInv())
        self.validateName(b.getTitlu())
        self.validateName(b.getAutor())
        self.validateName(b.getEditura())
        self.validateNr(b.getAnAparitie())
        self.validateNr(b.getCodBare())
        self.validateName(b.getISBN())
        self.validateNr(b.getNrEx())
        
    def validateReader(self,r):
        if(not isinstance(r,Reader)):
            raise MyException("Incorrect object type",p)
        self.validateName(r.getNume())
        self.validateName(r.getPrenume())
        self.validateNr(r.getCnp())
        self.validateName(r.getSerieCI())
        self.validateNr(r.getNrCI())
        self.validateName(r.getAdresa())
        self.validateNr(r.getTel())
        