'''
Created on Dec 23, 2017

@author: Sebi
'''
from RepositoryBooks import *
from RepositoryReaders import *
from RepositoryBooksDB import *
from RepositoryReadersDB import *
from Repository import *
from Validator import *

class Controller():
    def __init__(self):
        self.__repob=RepositoryBooksDB()
        self.__repor=RepositoryReadersDB()
        self.__repo=Repository()
        self.__val=Validator()
        
    def addBook(self,b):
        self.__val.validateBook(b)
        self.__repob.addBook(b)
        
    def addReader(self,r):
        self.__val.validateReader(r)
        self.__repor.addReader(r)
    
    def readersList(self):
        return self.__repor.getAllReaders()
    
    def booksList(self):
        return self.__repob.getAllBooks()
    
    def bookSearch(self,crt,c):
        l=[]
        if(crt=="Titlu"):
            for book in self.__repob.getAllBooks():
                if(book.getTitlu()==c):
                    l.append(book)
        return l
        
    def bookSearchv2(self,crt,c):
        return self.__repob.getBooks(crt, c)
    
    def readerSearchv2(self,crt,c):
        return self.__repor.getReaders(crt, c)
    
    def borrowBook(self,nrinv,cnp):
        self.__val.validateNr(nrinv)
        self.__val.validateNr(cnp)
        self.__repo.imprumuta(nrinv, cnp)
        
    def returnBook(self,nrinv,cnp):
        self.__val.validateNr(nrinv)
        self.__val.validateNr(cnp)
        self.__repo.returneaza(nrinv,cnp)
        
    def borrowedBooks(self):
        return self.__repo.cartiimprumutate()
    
    def restante(self):
        return self.__repo.restante()
    
    