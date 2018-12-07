'''
Created on Dec 17, 2017

@author: Sebi
'''

class Back():
    def __init__(self,nr,k,stiva,cond):
        self.__n=nr
        self.__k=k
        self.__st=[None]*100
        self.__l=stiva
        if(cond==1):
            self.__c=self.valid1
        if(cond==2):
            self.__c=self.valid2
        self.back(1)
        
    def valid1(self,p):
        for i in range(1,p):
            if(self.__st[i]==self.__st[p] or self.__l[self.__st[i]-1].getFName()==self.__l[self.__st[p]-1].getFName()):
                return False
        return True

    def valid2(self,p):
        for i in range(1,p):
            if(self.__st[i]==self.__st[p] or self.__l[self.__st[i]-1].getDest() != self.__l[self.__st[p]-1].getDest() or self.__l[self.__st[i]-1].getCompany()==self.__l[self.__st[p]-1].getCompany()):
                return False
        return True
    
    def afisare(self,p):
        for i in range(1,p+1):
            print(self.__l[self.__st[i]-1],end=' ')
        print ("\n")
        
    def back(self,p):
        for pval in range(1,self.__n+1):
            self.__st[p]=pval
            if(self.__c(p)):
                if(p==self.__k):
                    self.afisare(p)
                else:
                    self.back(p+1)
                