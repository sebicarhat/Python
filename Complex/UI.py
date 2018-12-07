from Operations import *
from ComplexNumber import *
from Repository import *
from MyException import *
from Repository import *
class UI():
    def __init__(self):
        self.__comp=Operations()
        self.__nrC=ComplexNumber(3,4)
        self.__repo=Repository()
        
    def printMenu(self):
        print("""1.Reprezentarea carteziana
        2.Reprezentarea in coordonate polare
        3.Conjugatul unui nr complex
        4.Inmultire cu un nr real
        5.Inmultire cu un nr imag
        6.Adunarea a 2 nr
        7.Inmultirea a 2 nr
        8.Reprezentarea matriceala
        9.Ridicare la putere
        10.Radical
        11.Exponentiala
        12.Exit""")
    
    def readNr(self):
        real=float(input("Real:"))
        img=float(input("Img:"))
        c=ComplexNumber(real,img)
        return c
    
    def run(self):
        f=open("input.txt")
        line=f.readline()
        nrC=ComplexNumber(float(line[0]),float(line[2]))
        #nrC=ComplexNumber(3.0,4.0)
        stop=False
        while(stop==False):
            self.printMenu()
            opt=int(input("Enter an option:"))
            if(opt==1):
                try:
                    self.__repo.writeRez(self.__comp.reprCart(nrC))
                except MyExeption as e:
                    print(e)
            if(opt==2):
                try:
                    self.__repo.writeRez(self.__comp.reprGeom(nrC))
                except MyExeption as e:
                    print(e)
            if(opt==3):
                try:
                    self.__repo.writeRez(repr(self.__comp.conj(nrC)))
                except MyExeption as e:
                    print(e)
            if(opt==4):
                try:
                    x = int(input("x="))
                    self.__repo.writeRez(repr(self.__comp.multyplyByReal(nrC,x)))
                except MyExeption as e:
                    print(e)
            if(opt==5):
                try:
                    x=int(input("i="))
                    self.__repo.writeRez(repr(self.__comp.multyplyByImg(nrC,x)))
                except MyExeption as e:
                    print(e)
            if(opt==6):
                try:
                    c=self.readNr()
                    self.__repo.writeRez(repr(self.__comp.add(nrC,c)))
                except MyExeption as e:
                    print(e)
            if(opt==7):
                try:
                    c=self.readNr()
                    self.__repo.writeRez(repr(self.__comp.multyplyBy(nrC,c)))
                except MyExeption as e:
                    print(e)
            if(opt==8):
                try:
                    self.__repo.writeRez(self.__comp.matrixRepr(nrC))
                except MyExeption as e:
                    print(e)
            if(opt==9):
                try:
                    n= int(input("n="))
                    self.__repo.writeRez(self.__comp.putere(nrC,n))
                except MyExeption as e:
                    print(e)
            if(opt==10):
                try:
                    self.__repo.writeRez(self.__comp.radical(nrC))
                except MyExeption as e:
                    print(e)
            if(opt==11):
                try:
                    self.__repo.writeRez(self.__comp.exp(nrC))
                except MyExeption as e:
                    print(e)
            if(opt==12):
                stop=True
            if(opt==13):
                Repository().viewData()
                
UI().run()
        