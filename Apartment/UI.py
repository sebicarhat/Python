'''
Created on Dec 6, 2017

@author: Sebi
'''
from Controller import *
from Apartament import *
class UI(object):
    '''
    classdocs
    '''


    def __init__(self):
        ''''l=[]
        ap1=Apartament(1, "Nume1", 100)
        ap2=Apartament(2, "Nume2", 200)
        l.append(ap1)
        l.append(ap2)'''
        self.__ctrl=Controller([Apartament(1, "Nume1", 100),Apartament(2, "Nume2", 200)])
    
        
        
    def run(self):
        x=int(input("val="))
        l=self.__ctrl.filter(x)[0]
        total=self.__ctrl.filter(x)[1]
        print(l)
        print(total)
        
        

UI().run()
    
      
        