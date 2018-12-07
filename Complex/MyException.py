'''
Created on Nov 23, 2017

@author: Sebi
'''
class MyExeption(Exception):
    def __init__(self,msg,obj,*args):
        self.__msg=msg
        self.__obj=obj
    
    def __str__(self):
        return "Error: "+str(self.__msg)+" Object: "+str(self.__obj)
    
    