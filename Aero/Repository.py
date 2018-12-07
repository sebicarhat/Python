'''
Created on Nov 27, 2017

@author: Sebi
'''
from Aeroplane import *
from Passenger import *

class Repository():
    def __init__(self):
        l1=[Passenger("Prenume1","Nume1","abcd"),Passenger("Prenume2","Nume2","abce"),Passenger("Prenume2","Nume2","abce")]
        l2=[Passenger("Prenume2","Nume4","abcd"),Passenger("Arenume3","Nume3","abdf")]
        A1=Aeroplane("A1",1,"Company",100,"Dest",l1)
        A2=Aeroplane("A2",2,"Company2",200,"Dest",l2)
        A3=Aeroplane("A3",3,"Company",200,"Dest",l1)
        self.__aeroplanes=[A1,A2]
        self.__passengers=[]
    
    def addPassenger(self,passenger):
        self.__passengers.append(passenger)
        
    def removePassenger(self,passenger):
        self.__passengers.remove(passenger)
    
    def updatePassenger(self,oldpassenger,newpassenger):
        index=self.__passengers.index(oldpassenger)
        self.__passengers[index]=newpassenger
    
    def getPassengerList(self):
        return self.__passengers[:]
    
        
    def addAero(self,aero):
        self.__aeroplanes.append(aero)
        
    def removeAero(self,aero):
        self.__aeroplanes.remove(aero)
    
    def updateAero(self,oldaero,newaero):
        index=self.__aeroplanes.index(oldaero)
        self.__aeroplanes[index]=newaero
    
    def getAllAeroplanes(self):
        return self.__aeroplanes[:]
    
    def getAllAeroplanesRec(self,l,i):
        if(i==len(self.__aeroplanes)):
            return l
        else:
            l.append(self.__aeroplanes[i])
            return self.getAllAeroplanesRec(l, i+1)
    
    
                    
                