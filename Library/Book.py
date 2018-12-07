'''
Created on Dec 22, 2017

@author: Sebi
'''
class Book():
    def __init__(self,nrinv,titlu,autor,editura,anap,codbare,isbn,nrex):
        self.__nrinv=nrinv
        self.__titlu=titlu
        self.__autor=autor
        self.__editura=editura
        self.__anap=anap
        self.__codbare=codbare
        self.__isbn=isbn
        self.__nrex=nrex
        
    def getNrInv(self):
        return self.__nrinv
    
    def getTitlu(self):
        return self.__titlu
    
    def getAutor(self):
        return self.__autor
    
    def getEditura(self):
        return self.__editura
    
    def getAnAparitie(self):
        return self.__anap
    
    def getCodBare(self):
        return self.__codbare
    
    def getISBN(self):
        return self.__isbn
    
    def getNrEx(self):
        return self.__nrex
    
    def setNrInv(self,x):
        self.__nrinv=x 
    
    def setTitlu(self,x):
        self.__titlu=x 
    
    def setAutor(self,x):
        self.__autor=x 
        
    def setEditura(self,x):
        self.__editura=x 
        
    def setAnAparitie(self,x):
        self.__anap=x 
        
    def setCodBare(self,x):
        self.__codbare=x 
        
    def setISBN(self,x):
        self.__isbn=x 
        
    def setNrEx(self,x):
        self.__nrex=x 
        
    def __str__(self):
        return str(self.__titlu)+", "+str(self.__autor)+" "+str(self.__editura)+", "+str(self.__anap)
    
    def __repr__(self):
        return str(self.__titlu)+", "+str(self.__autor)+" "+str(self.__editura)+", "+str(self.__anap)