from ComplexNumber import *
from builtins import str
import json as js

class Repository():
    def __init__(self):
        pass

    def read(self):
        try:
            f=open("date.js","r")
            data=js.load(f)
            f.close()
            return data
        except IOError as e1:
            print(str(e1))
        except ValueError as e2:
            print(str(e2))
            
    def write(self,data):
        try:
            f=open("date.js","w")
            js.dump(data,f)
            f.close()
        except IOError as e1:
            print(str(e1))
        except ValueError as e2:
            print(str(e2))
            
    def writeRez(self,s):
        data=str(self.read())
        data+=s+"\n"
        self.write(data)
        
        
    def viewData(self):
        print(str(self.read()))
    
            