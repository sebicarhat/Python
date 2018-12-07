'''
Created on Dec 23, 2017

@author: Sebi
'''
from Book import *
class RepositoryBooks():
    def __init__(self):
        self.__booklist=[Book(123,"titlu","autor","edit",1231,32131,32131,21)]
        
    def addBook(self,b):
        self.__booklist.append(b)
        
    def removeBook(self,b):
        self.__booklist.remove(b)
        
    def updateBook(self,old,new):
        index=self.__booklist.index(old)
        self.__booklist[index]=new
    
    def getAllBooks(self):
        return self.__booklist[:]
    
    