'''
Created on Dec 23, 2017

@author: Sebi
'''

class RepositoryReaders():
    def __init__(self):
        self.__readerslist=[]
        
    def addReader(self,r):
        self.__readerslist.append(r)
        
    def removeReader(self,r):
        self.__readerslist.remove(r)
        
    def updateReader(self,old,new):
        index=self.__readerslist.index(old)
        self.__readerslist[index]=new
    
    def getAllReaders(self):
        return self.__readerslist[:]