'''
Created on Jan 2, 2018

@author: Sebi
'''
import sqlite3
import time
import datetime
from Validator import *

class Repository():
    def __init__(self):
        self.conn=sqlite3.connect('database.db')
        self.c=self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS borrowed(nrinv TEXT, cnp TEXT, zian REAL)')
        self.__v=Validator()
    
    def imprumuta(self,nrinv,cnp):
        unix=time.time()
        day=int(datetime.datetime.fromtimestamp(unix).strftime('%j'))
        '''self.c.execute("SELECT nrex FROM books WHERE nrinv > '"+nrinv+"' ")
        self.conn.commit
        row=self.c.fetchall()[0]
        self.__v.validateNrEx(row[0])'''
        self.c.execute("INSERT INTO borrowed (nrinv, cnp, zian) VALUES(?, ?, ?)",
                  (nrinv,cnp, day))
        self.conn.commit()
        self.c.execute("UPDATE books SET nrex=nrex-1 WHERE nrinv='"+nrinv+"'")
        self.conn.commit()
        
    def returneaza(self,nrinv,cnp):
        self.c.execute("DELETE FROM borrowed WHERE nrinv = '"+nrinv+"'")
        self.conn.commit()
        self.c.execute("UPDATE books SET nrex=nrex+1 WHERE nrinv='"+nrinv+"'")
        self.conn.commit()
    

    def cartiimprumutate(self):
        l=[]
        list=[]
        '''self.c.execute("SELECT * FROM borrowed")
        for row in self.c.fetchall():
            l.append(row[0])
            l.append(row[1])
        for i in range(0, len(l),2):'''
        self.c.execute("SELECT books.titlu, books.autor, readers.nume, readers.prenume, readers.cnp FROM borrowed LEFT JOIN readers ON readers.cnp=borrowed.cnp LEFT JOIN books ON borrowed.nrinv=books.nrinv")
        #list.append(self.c.fetchall())
        return self.c.fetchall()
        '''for i in range(0 ,len(l), 2):
            #self.c.execute("SELECT titlu, autor FROM books WHERE nrinv='"+l[i+1]+"' UNION SELECT nume, prenume FROM readers WHERE cnp='"+l[i]+"'")
            #list.append(self.c.fetchall())
            list.append(l[i],l[i+1])
        return l'''
   
    def restante(self):
        unix=time.time()
        day=int(datetime.datetime.fromtimestamp(unix).strftime('%j'))
        self.c.execute("SELECT books.titlu, books.autor, readers.nume, readers.prenume, readers.cnp FROM borrowed LEFT JOIN readers ON readers.cnp=borrowed.cnp LEFT JOIN books ON borrowed.nrinv=books.nrinv WHERE borrowed.zian<'"+str(day)+"'")
        return self.c.fetchall()
    