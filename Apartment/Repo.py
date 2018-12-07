'''
Created on Dec 6, 2017

@author: Sebi
'''
from Apartament import *
import Apartament

class Repo():
    '''
    classdocs
    '''
    def __init__(self,list):
        self.__bloc=list
 
    def getBlocList(self):
        return self.__bloc[:]
    
        '''
        Constructor
        '''
        