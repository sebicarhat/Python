'''
Created on Nov 16, 2017

@author: Sebi
'''
class Contact():
    
    def __init__(self,name,nr):
        self.__name=name
        self.__nr=nr
        
    def setName(self,nr):
        self.__name=name
    
    def setNr(self,nr):
        self.__nr=nr
        
    def getName():
        return self.__name
    
    def getNumber():
        return self.__nr
    
    def __eq__(self,object):
        return self.getName()==object.getName()
    
    def __str__(self):
        print(str(repr.getName()))
        
        