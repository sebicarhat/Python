'''
Created on Nov 27, 2017

@author: Sebi
'''
class Passenger():
    def __init__(self,fname,lname,series):
        self.__fname=fname
        self.__lname=lname
        self.__series=series
        
    def getFName(self):
        return self.__fname
    
    def getLName(self):
        return self.__lname
    
    def getSeries(self):
        return self.__series
    
    def setFName(self,name):
        self.__fname=name
        
    def setLName(self,name):
        self.__lname=name
    
    def setSeries(self,series):
        self.__series=series
        
    def __str__(self):
        return str(self.__fname)+","+str(self.__lname)+","+str(self.getSeries())
    
    def __repr__(self):
        return str(self.__fname)+","+str(self.__lname)+","+str(self.getSeries())
        