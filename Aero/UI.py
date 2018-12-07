'''
Created on Nov 28, 2017

@author: Sebi
'''
from Controller import *
from Passenger import *
from Repository import *
from Aeroplane import *
from MyException import *
from back import *

class UI():
    def __init__(self):
        self.__ctrl=Controller()
        self.__repo=Repository()
        
    def readNr(self):
        return int(input("n="))
    
    def readChar(self):
        return input("c=")
    
    def readPassenger(self):
        fname=input("Prenume")
        lname=input("Nume:")
        series=input("Serie:")
        p=Passenger(fname,lname,series)
        return p
        
    def readAeroplane(self):
        name=input("Nume avion:")
        nr=int(input("Nr avion:"))
        c=input("Company:")
        nrseats=int(input("Nr locuri:"))
        dest=input("Destinatie:")
        a=Aeroplane(name,nr,c,nrseats,dest,[])
        return a
    
    def mesaj(self):
        print(
            """Alege
1 pentru adaugare pasager
2 pentru adaugare avion
3
4
5
6
7
8
9
10""")
    def run(self):
        try:
            stop=False
            while(stop==False):
                self.mesaj()
                opt=int(input("Alege o optiune:"))
                if opt==1:
                    aero=self.readAeroplane()
                    self.__ctrl.addAero(aero)
                    print("Adaugat cu succes")
                if opt==2:
                    passenger=self.readPassenger()
                    self.__ctrl.addPassenger(passenger)
                    print("Adaugat cu succes")
                if opt==3:
                    p=int(input("nr:"))
                    print(self.__ctrl.Condition(1, p))
                if opt==4:
                    p=input("Litera:")
                    print(self.__ctrl.Condition(2, p))
                if opt==5:
                    print(self.__ctrl.Condition(3))
                if opt==6:
                    print(self.__ctrl.Condition(4))
                if opt==7:
                    p=input("Sirul de caractere:")
                    q=int(input("nr avion:"))
                    print(self.__ctrl.Condition(5, p,q))
                if opt==8:
                    p=input("Nume:")
                    print(self.__ctrl.Condition(6, p))    
                if opt==9:
                    nr=int(input("Nr avion"))
                    k=int(input("k="))
                    self.__ctrl.kPasageri(k, nr)
                    #Back(3,k,[1,2,3],1)
                if opt==10:
                    k=int(input("k="))
                    self.__ctrl.kAvioane(k)
                if opt==0:
                    stop=True
                
        except MyException as ex:
            print(ex)
            
    

        
UI().run()