'''
Created on Dec 6, 2017

@author: Sebi
'''

class Apartament():

    def __init__(self,numar,numefamilie,sumaplata):
        self.__nr=numar
        self.__nume=numefamilie
        self.__suma=sumaplata
        
    def getNumar(self):
        return self.__nr
    
    def getNume(self):
        return self.__nume
    
    def getSuma(self):
        return self.__suma
    
    def setNumar(self,nr):
        self.__nr=nr
    
    def setNume(self,nume):
        self.__nume=nume
        
    def setSuma(self,suma):
        self.__suma=suma
        
    def __str__(self):
        return str(self.getNume())
    
    def __repr__(self):
        return str(self.getNume())
    
        '''
        Constructor
        '''
        