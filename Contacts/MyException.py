'''
Created on Nov 23, 2017

@author: Sebi
'''
class MyExeption(Exception):
    def __init__(self,msg,obj,*args):
        self.__msg=msg
        self.__obj=obj
        
    super(MyExeption,self).__init__(msg,obj,*args))
    
    