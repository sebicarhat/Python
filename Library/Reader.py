'''
Created on Dec 23, 2017

@author: Sebi
'''
class Reader():
    def __init__(self,nume,prenume,cnp,serieci,nrci,adresa,tel):
        self.__nume=nume
        self.__prenume=prenume
        self.__cnp=cnp
        self.__serieci=serieci
        self.__nrci=nrci
        self.__adresa=adresa
        self.__tel=tel
        
    def getNume(self):
        return self.__nume
    
    def getPrenume(self):
        return self.__prenume
    
    def getCnp(self):
        return self.__cnp
    
    def getSerieCI(self):
        return self.__serieci
    
    def getNrCI(self):
        return self.__nrci
    
    def getAdresa(self):
        return self.__adresa
    
    def getTel(self):
        return self.__tel
    
    def setNume(self,x):
        self.__nume=x 
        
    def setPrenume(self,x):
        self.__prenume=x 
        
    def setSerieCI(self,x):
        self.__serieci=x 
        
    def setNrCI(self,x):
        self.__nrci=x 
        
    def setAdresa(self,x):
        self.__adresa=x 
        
    def setTelefon(self,x):
        self.__tel=x 
        
    def __str__(self):
        return str(self.__nume)+" "+str(self.__prenume)
    
    def __repr__(self):
        return str(self.__nume)+" "+str(self.__prenume)