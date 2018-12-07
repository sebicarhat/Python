'''
Created on Dec 6, 2017

@author: Sebi
'''
from Repo import *
class Controller():
    '''
    classdocs
    '''
    def __init__(self,list):
        self.__repo=Repo(list)
        
        
    def filter(self,x):
        l=[]
        s=0
        for ap in self.__repo.getBlocList():
            if(ap.getSuma()>x):
                l.append(ap)
                s+=ap.getSuma()
        return l,s
    
    
    
    '''
        Constructor
        '''
        