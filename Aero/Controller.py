'''
Created on Dec 11, 2017

@author: Sebi
'''
from Repository import *
from Validator import *
from back import *

class Controller():
    
    def __init__(self):
        self.__repo=Repository()
        self.__v=Validator()
         
    def addPassenger(self,passenger):
        self.__v.validatePassenger(passenger)
        self.__repo.addPassenger(passenger)
        
    def removePassenger(self,passenger):
        self.__v.validatePassenger(passenger)
        self.__repo.removePassenger(passenger)

    def updatePassenger(self,old,new):
        self.__v.validatePassenger(old)
        self.__v.validatePassenger(new)
        self.__repo.updatePassenger(old, new)
    
    def addAero(self,aero):
        self.__v.validateAero(aero)
        self.__repo.addAero(aero)
        
    def removeAero(self,aero):
        self.__v.validateAero(aero)
        self.__repo.removeAero(aero)
        
    def updateAero(self,oldaero,newaero):
        self.__v.validateAero(oldaero)
        self.__v.validateAero(newaero)
        self.__repo.updateAero(oldaero, newaero)  
        
    def searchByNr(self,nr):
        for aero in self.__repo.getAllAeroplanes():
            if(aero.getNr()==nr):
                return aero
        return -1
        
    def getNrOfPassagers(self,aero,p):
        k=0
        for passenger in aero.getPassengerList():
            if(passenger.getFName()[:1]==p):
                k+=1
        return k
            
    def sortByNameCond(self,passenger1, passenger2,opt):
        return passenger1.getFName()>passenger2.getFName()
    
    def sortByNr(self,a1,a2,opt):
        return self.getNrOfPassagers(a1,opt)>self.getNrOfPassagers(a2,opt)
    
    def sortByConcat(self,a1,a2,opt):
        s1=str(len(a1.getPassengerList()))+str(a1.getName())
        s2=str(len(a2.getPassengerList()))+str(a2.getName())
        return s1>s2
    
    def sort(self,cond,list,opt=None):
        for i in range(0,len(list)-1):
            for j in range(i+1,len(list)):
                    if(cond(list[i],list[j],opt)):
                        list[i],list[j]=list[j],list[i]
       
    def groupBySeries(self,list):
        dict={}
        for el in list:
            pref=el.getSeries()[:3]
            values=dict.get(pref,[])
            values.append(el)
            dict[pref]=values
        return dict
    
    def search1Cond(self,aero,p):
        ok=False
        dict=self.groupBySeries(aero.getPassengerList())
        for v in dict.values():
            if len(v)>1:
                ok=True
        return ok
    
    def search2Cond(self,passenger,p):
        ok=False
        l1=len(passenger.getFName())
        l2=len(p)
        if(l1<l2):
            raise MyException("Lungimea numelui e mai mica decat a sirului")
        else:
            if passenger.getFName().find(p)!=-1:
                    ok=True
        return ok
    
    def search3Cond(self,aero,p):
        for passenger in aero.getPassengerList():
            if(passenger.getFName()==p):
                return True
        return False
        
    def search(self,cond,list,p=None,q=None):
        l=[]
        for el in list:
            if(cond(el,p)):
                l.append(el)
        return l          
           
    def Condition(self,cond,p=None,q=None):
        if cond==1:
            index=self.__repo.getAllAeroplanes().index(self.searchByNr(p))
            list=self.__repo.getAllAeroplanes()[index].getPassengerList()
            self.sort(self.sortByNameCond,list)   
        if cond==2:
            list=self.__repo.getAllAeroplanes()
            self.sort(self.sortByNr, list,p)
        if cond==3:
            list=self.__repo.getAllAeroplanes()
            self.sort(self.sortByConcat, list)
        if cond==4:
            list=self.__repo.getAllAeroplanes()
            l=self.search(self.search1Cond, list)
            list=l
        if cond==5:
            index=self.__repo.getAllAeroplanes().index(self.searchByNr(q))
            list=self.__repo.getAllAeroplanes()[index].getPassengerList() 
            list=self.search(self.search2Cond, list, p,q)  
        if cond==6:
            list=self.__repo.getAllAeroplanes()
            list=self.search(self.search3Cond, list,p) 
  
        return list
    
    def kPasageri(self,k,nr):
        index=self.__repo.getAllAeroplanes().index(self.searchByNr(nr))
        list=self.__repo.getAllAeroplanes()[index].getPassengerList() 
        Back(len(list),k,list,1)
    
    def kAvioane(self,k):
        list=self.__repo.getAllAeroplanes()
        Back(len(list),k,list,2)
    
    

    
