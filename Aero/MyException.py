'''
Created on Dec 13, 2017

@author: Sebi
'''
from builtins import str
class MyException(Exception):

    def __init__(self,msg,obj=None,*args):
        self.__msg=msg
        self.__obj=obj
        
    def __str__(self):
        return "Error:"+str(self.__msg)+" Object:"+str(self.__obj)
    pass
        