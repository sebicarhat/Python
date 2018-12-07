'''
Created on Jan 2, 2018

@author: Sebi
'''
from Reader import *
import sqlite3
from unicodedata import numeric

class RepositoryReadersDB():
    def __init__(self):
        self.conn=sqlite3.connect('database.db')
        self.c=self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS readers(nume TEXT, prenume TEXT, cnp TEXT, serieci TEXT, nrci TEXT, adresa TEXT, tel TEXT)')
    
    def addReader(self,r):
        nume=r.getNume()
        prenume=r.getPrenume()
        cnp=r.getCnp()
        serie=r.getSerieCI()
        nr=r.getNrCI()
        adresa=r.getAdresa()
        tel=r.getTel()
        
        self.c.execute("INSERT INTO readers (nume, prenume, cnp, serieci, nrci, adresa, tel) VALUES(?, ?, ?, ?, ?, ?, ?)",
              (nume,prenume,cnp,serie,nr,adresa,tel))
        self.conn.commit()
        self.c.close()
        self.conn.close()

    def getAllReaders(self):
        self.c.execute("SELECT * FROM readers")
        return self.c.fetchall()
    
    def getReaders(self,crt,s):
        if(crt=="Nume"):
            self.c.execute("SELECT * FROM readers WHERE nume like '"+s+"' OR prenume like '"+s+"'")
        if(crt=="CNP"):
            self.c.execute("SELECT * FROM readers WHERE cnp like '"+s+"'")
        if(crt=="Telefon"):
            self.c.execute("SELECT * FROM readers WHERE tel like '"+s+"'")
        return self.c.fetchall()
 
    