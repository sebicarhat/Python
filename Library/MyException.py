'''
Created on Jan 11, 2018

@author: Sebi
'''
'''
Created on Dec 13, 2017

@author: Sebi
'''
class MyException(Exception):

    def __init__(self,msg,obj=None,*args):
        self.__msg=msg
        self.__obj=obj
        
    def __str__(self):
        return "Error:"+str(self.__msg)+" Object: "+str(self.__obj)
    pass
        