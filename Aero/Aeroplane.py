'''
Created on Nov 27, 2017

@author: Sebi
'''

class Aeroplane():
    '''
    classdocs
    '''

    def __init__(self, name, nr, company, nrseats, dest, passengerlist):
        self.__name=name
        self.__nr=nr
        self.__company=company
        self.__nrseats=nrseats
        self.__dest=dest
        self.__passengerlist=passengerlist
    
    def getName(self):
        return self.__name
    
    def getNr(self):
        return self.__nr
    
    def getCompany(self):
        return self.__company
    
    def getNrSeats(self):
        return self.__nrseats

    def getDest(self):
        return self.__dest
    
    def getPassengerList(self):
        return self.__passengerlist
    
    def setName(self,name):
        self.__name=name
        
    def setNr(self,nr):
        self.__nr=nr
        
    def setCompany(self,company):
        self.__company=company
        
    def setNrSeats(self,nrseats):
        self.__nrseats=nrseats
        
    def setDest(self,dest):
        self.__dest=dest
    
    def setPassengerList(self,passengerlist):
        self.__passengerlist=passengerlist
        
    def __str__(self):
        return self.__name
        
    def __repr__(self):
        return self.__name
    
        