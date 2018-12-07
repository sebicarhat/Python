'''
Created on Jan 2, 2018

@author: Sebi
'''
from Book import *
import sqlite3

class RepositoryBooksDB():
    def __init__(self):
        self.conn=sqlite3.connect('database.db')
        self.c=self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS books(nrinv INT, titlu TEXT, autor TEXT, editura TEXT, anap TEXT, codbare TEXT, isbn TEXT,nrex INT)')  
    
    def addBook(self,book):
        nrinv=book.getNrInv()
        titlu=book.getTitlu()
        autor=book.getAutor()
        editura=book.getEditura()
        anap=book.getAnAparitie()
        codbare=book.getCodBare()
        isbn=book.getISBN()
        nrex=book.getNrEx()
        
        self.c.execute("INSERT INTO books (nrinv, titlu, autor, editura, anap, codbare, isbn, nrex) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                  (nrinv,titlu,autor,editura,anap,codbare,isbn,nrex))
        self.conn.commit()
        self.c.close()
        self.conn.close()
    
    def getAllBooks(self):
        self.c.execute("SELECT * FROM books")
        return self.c.fetchall()
    
    def getBooks(self,crt,s):
        if(crt=="Titlu"):
            self.c.execute("SELECT * FROM books WHERE titlu like '"+s+"'")
        
        if(crt=="Autor"):
            self.c.execute("SELECT * FROM books WHERE autor like '"+s+"'")
        if(crt=="Editura"):
            self.c.execute("SELECT * FROM books WHERE editura like '"+s+"'")
        return self.c.fetchall()
    