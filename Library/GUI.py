'''
Created on Dec 23, 2017

@author: Sebi
'''
from Book import *
from Reader import *
from Controller import *
from Validator import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image

controller=Controller()
rb=RepositoryBooks()
rr=RepositoryReaders()

text1=tk.Text
text2=tk.Text
text3=tk.Text
text4=tk.Text
text5=tk.Text
text6=tk.Text
text7=tk.Text
text8=tk.Text

text21=tk.Text
text22=tk.Text
text23=tk.Text
text24=tk.Text
text25=tk.Text
text26=tk.Text
text27=tk.Text

def MainWindow(root):
    load=Image.open("image.jpg")
    render = ImageTk.PhotoImage(load)
    img=tk.Label(root,image=render)
    img.image=render
    img.pack(side="top", fill="y", expand=True, padx=5, pady=5)
    
    button1=tk.Button(root,text="Adauga carte",command= lambda: addBookWindow(root))
    #button1.grid(row=0,column=1)
    #button1.config(width=50)
    button1.pack(side="top", fill="both", expand=True, padx=5, pady=5)
            
    button2=tk.Button(root,text="Lista carti",command= lambda: viewBookList(root))
    #button2.grid(row=1,column=1)
    #button2.config(width=50)
    button2.pack(side="top", fill="both", expand=True, padx=5, pady=5)
        
    button3=tk.Button(root,text="Cautare carte",command= lambda: searchBook(root))
    #button3.grid(row=2,column=1)
    #button3.config(width=50)    
    button3.pack(side="top", fill="both", expand=True, padx=5, pady=5)
        
    button4=tk.Button(root,text="Adauga cititor",command= lambda: addReaderWindow(root))
    #button4.grid(row=0,column=3)
    #button4.config(width=50)
    button4.pack(side="top", fill="both", expand=True, padx=5, pady=5)
            
    button5=tk.Button(root,text="Lista cititori",command= lambda: viewReaderList(root))
    #button5.grid(row=1,column=3)
    #button5.config(width=50)
    button5.pack(side="top", fill="both", expand=True, padx=5, pady=5)
            
    button6=tk.Button(root,text="Cauta cititor",command= lambda: searchReader(root))
    #button6.grid(row=2,column=3)
    #button6.config(width=50)
    button6.pack(side="top", fill="both", expand=True, padx=5, pady=5)
        
    button7=tk.Button(root,text="Imprumuta carte",command= lambda: borrowWindow(root))
    #button7.grid(row=3,column=1)
    #button7.config(width=50)
    button7.pack(side="top", fill="both", expand=True, padx=5, pady=5)
            
    button8=tk.Button(root,text="Returneaza carte",command= lambda: returnWindow(root))
    #button8.grid(row=4,column=1)
    #button8.config(width=50)
    button8.pack(side="top", fill="both", expand=True, padx=5, pady=5)
            
    button9=tk.Button(root,text="Carti imprumutate",command= lambda: viewBorrowedBooks(root))
    #button9.grid(row=3,column=3)
    #button9.config(width=50)
    button9.pack(side="top", fill="both", expand=True, padx=5, pady=5)
            
    button10=tk.Button(root,text="Restante",command= lambda: restante(root))
    #button10.grid(row=4,column=3)
    #button10.config(width=50)
    button10.pack(side="top", fill="both", expand=True, padx=5, pady=5)
      
      
def addReaderWindow(root):
    t=tk.Toplevel(root)
    t.wm_title("Adauga cititor")
    
    label21=tk.Label(t,text="Nume:",width=5)
    label21.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    global text21
    text21=tk.Text(t,width=40,height=1)
    text21.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
    label22=tk.Label(t,text="Prenume:",width=5)
    label22.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    global text22
    text22=tk.Text(t,width=40,height=1)
    text22.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
    label23=tk.Label(t,text="CNP:",width=5)
    label23.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    global text23
    text23=tk.Text(t,width=40,height=1)
    text23.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
    label24=tk.Label(t,text="SerieCI:",width=5)
    label24.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    global text24
    text24=tk.Text(t,width=40,height=1)
    text24.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
    label25=tk.Label(t,text="Nr CI:",width=5)
    label25.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    global text25
    text25=tk.Text(t,width=40,height=1)
    text25.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
    label26=tk.Label(t,text="Adresa:",width=5)
    label26.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    global text26
    text26=tk.Text(t,width=40,height=1)
    text26.pack(side="top", fill="both", expand=True, padx=5, pady=5)
     
    label27=tk.Label(t,text="Tel:",width=5)
    label27.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    global text27
    text27=tk.Text(t,width=40,height=1)
    text27.pack(side="top", fill="both", expand=True, padx=5, pady=5)   
    
    adaugabutton=tk.Button(t,text="Adauga",command= lambda: adaugacititor())
    adaugabutton.pack(side="top", fill="both", expand=True, padx=5, pady=5)

def searchBook(root):
    t=tk.Toplevel(root)
    t.wm_title("Cautare carte")
    
    searchlabel=tk.Label(t,text="Cauta dupa:",width=5)
    searchlabel.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    cb=ttk.Combobox(t, state='readonly')
    cb.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    cb['values']=('Titlu','Autor','Editura')
    cb.current(0)
    text1=tk.Text(t,width=40,height=1,)
    text1.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    '''def cmd():
        listbox.delete(0,"end")
        listbox.insert("end",controller.bookSearchv2(str(cb.get()),str(text1.get("1.0","end"))))
    listbox=tk.Listbox(t)
    listbox.pack(side="top", fill="both", expand=True, padx=5, pady=5)'''
    
    tabel=ttk.Treeview(t,columns=('Nr inv','Titlu','Autor','Editura','An aparitie','Cod bare','ISBN','Nr ex'))
    tabel.heading('#0', text="Nr inv",anchor=tk.CENTER)
    tabel.heading('#1', text="Titlu",anchor=tk.CENTER)
    tabel.heading('#2', text="Autor",anchor=tk.CENTER)
    tabel.heading('#3', text="Editura",anchor=tk.CENTER)
    tabel.heading('#4', text="An aparitie",anchor=tk.CENTER)
    tabel.heading('#5', text="Cod bare",anchor=tk.CENTER)
    tabel.heading('#6', text="ISBN",anchor=tk.CENTER)
    tabel.heading('#7', text="Nr ex",anchor=tk.CENTER)
    tabel.column('#0', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#1', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#2', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#3', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#4', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#5', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#6', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#7', stretch=tk.YES, minwidth=50, width=100)
    tabel.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    def cmd():
        for row in tabel.get_children():
            tabel.delete(row)
        for row in controller.bookSearchv2(str(cb.get()),str(text1.get("1.0","end"))):
            tabel.insert('','end',text=(row[0]),values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
                     
    searchbookbutton=tk.Button(t,text="Cauta",command= lambda: cmd())
    searchbookbutton.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    

def searchReader(root):
    t=tk.Toplevel(root)
    t.wm_title("Cautare cititor")
    
    searchlabel=tk.Label(t,text="Cauta dupa:",width=5)
    searchlabel.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    cb=ttk.Combobox(t, state='readonly')
    cb.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    cb['values']=('Nume','CNP','Telefon')
    cb.current(0)
    text1=tk.Text(t,width=40,height=1,)
    text1.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    '''listbox=tk.Listbox(t)
    listbox.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    def cmd():
        listbox.delete(0, "end")
        listbox.insert("end",controller.readerSearchv2(str(cb.get()),str(text1.get("1.0","end"))))'''
    
    tabel=ttk.Treeview(t,columns=('Nume','Prenume','CNP','SerieCI','NrCI','Adresa','Tel'))
    tabel.heading('#0', text="Nume",anchor=tk.CENTER)
    tabel.heading('#1', text="Prenume",anchor=tk.CENTER)
    tabel.heading('#2', text="CNP",anchor=tk.CENTER)
    tabel.heading('#3', text="SerieCI",anchor=tk.CENTER)
    tabel.heading('#4', text="NrCI",anchor=tk.CENTER)
    tabel.heading('#5', text="Adresa",anchor=tk.CENTER)
    tabel.heading('#6', text="Tel",anchor=tk.CENTER)
    tabel.column('#0', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#1', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#2', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#3', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#4', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#5', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#6', stretch=tk.YES, minwidth=50, width=100)
    tabel.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    def cmd():
        for row in tabel.get_children():
            tabel.delete(row)
        for row in controller.readerSearchv2(str(cb.get()),str(text1.get("1.0","end"))):
            tabel.insert('','end',text=(row[0]),values=(row[1],row[2],row[3],row[4],row[5],row[6]))
    searchreaderbutton=tk.Button(t,text="Cauta",command= lambda: cmd())
    searchreaderbutton.pack(side="top", fill="both", expand=True, padx=5, pady=5)


def viewBookList(root):
    t=tk.Toplevel(root)
    t.wm_title("Vizualizare carti") 
    #listbox=tk.Listbox(t)
    #listbox.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    tabel=ttk.Treeview(t,columns=('Nr inv','Titlu','Autor','Editura','An aparitie','Cod bare','ISBN','Nr ex'))
    tabel.heading('#0', text="Nr inv",anchor=tk.CENTER)
    tabel.heading('#1', text="Titlu",anchor=tk.CENTER)
    tabel.heading('#2', text="Autor",anchor=tk.CENTER)
    tabel.heading('#3', text="Editura",anchor=tk.CENTER)
    tabel.heading('#4', text="An aparitie",anchor=tk.CENTER)
    tabel.heading('#5', text="Cod bare",anchor=tk.CENTER)
    tabel.heading('#6', text="ISBN",anchor=tk.CENTER)
    tabel.heading('#7', text="Nr ex",anchor=tk.CENTER)
    tabel.column('#0', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#1', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#2', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#3', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#4', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#5', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#6', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#7', stretch=tk.YES, minwidth=50, width=100)
    tabel.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    i=-1
    for row in controller.booksList():
        tabel.insert('','end',text=str(row[0]),values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
    
    
def viewReaderList(root):
    t=tk.Toplevel(root)
    t.wm_title("Vizualizare cititori") 
    '''listbox=tk.Listbox(t)
    listbox.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    listbox.insert("end",controller.readersList())'''
    
    tabel=ttk.Treeview(t,columns=('Nume','Prenume','CNP','SerieCI','NrCI','Adresa','Tel'))
    tabel.heading('#0', text="Nume",anchor=tk.CENTER)
    tabel.heading('#1', text="Prenume",anchor=tk.CENTER)
    tabel.heading('#2', text="CNP",anchor=tk.CENTER)
    tabel.heading('#3', text="Serie CI",anchor=tk.CENTER)
    tabel.heading('#4', text="Nr CI",anchor=tk.CENTER)
    tabel.heading('#5', text="Adresa",anchor=tk.CENTER)
    tabel.heading('#6', text="Tel",anchor=tk.CENTER)
    tabel.column('#0', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#1', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#2', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#3', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#4', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#5', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#6', stretch=tk.YES, minwidth=50, width=100)
    tabel.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    for row in controller.readersList():
        tabel.insert('','end',text=str(row[0]),values=(row[1],row[2],row[3],row[4],row[5],row[6]))
    
 
def viewBorrowedBooks(root):
    t=tk.Toplevel(root)
    t.wm_title("Carti imprumutate") 
    '''listbox=tk.Listbox(t)
    listbox.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    listbox.insert("end",controller.borrowedBooks())'''
    tabel=ttk.Treeview(t,columns=('Titlu','Autor','Nume','Prenume','CNP'))
    tabel.heading('#0', text="Titlu",anchor=tk.CENTER)
    tabel.heading('#1', text="Nume",anchor=tk.CENTER)
    tabel.heading('#2', text="Prenume",anchor=tk.CENTER)
    tabel.heading('#3', text="Autor",anchor=tk.CENTER)
    tabel.heading('#4', text="CNP",anchor=tk.CENTER)
    tabel.column('#1', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#2', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#3', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#4', stretch=tk.YES, minwidth=50, width=100)
    tabel.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    for row in controller.borrowedBooks():
        tabel.insert('','end',text=str(row[0]),values=(row[1],row[2],row[3],row[4]))

def borrowWindow(root):
    def borrow():
        try:
            controller.borrowBook(text1.get("1.0","end"), text2.get("1.0","end"))
        except MyException as ex:
            tk.messagebox.showinfo(message=str(ex))
    
    t=tk.Toplevel(root)
    #t.wm_title("Adauga carte #%s" % counter)
    t.wm_title("Imprumuta" )
    #l=tk.Label(t, text="This is window #%s" % counter)
    #l.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
    label1=tk.Label(t,text="Nr inv:",width=5)
    label1.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    text1=tk.Text(t,width=40,height=1)
    text1.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
    label2=tk.Label(t,text="CNP:",width=5)
    label2.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    text2=tk.Text(t,width=40,height=1)
    text2.pack(side="top", fill="both", expand=True, padx=5, pady=5) 
    
    imprumutabutton=tk.Button(t,text="Imprumuta",command= lambda: borrow())
    imprumutabutton.pack(side="top", fill="both", expand=True, padx=5, pady=5)

def returnWindow(root):
    def ret():
        try:
            controller.returnBook(text1.get("1.0","end"), text2.get("1.0","end"))
        except MyException as ex:
            tk.messagebox.showinfo(message=str(ex))
    t=tk.Toplevel(root)
    #t.wm_title("Adauga carte #%s" % counter)
    t.wm_title("Returneaza" )
    #l=tk.Label(t, text="This is window #%s" % counter)
    #l.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
    label1=tk.Label(t,text="Nr inv:",width=5)
    label1.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    text1=tk.Text(t,width=40,height=1)
    text1.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
    label2=tk.Label(t,text="CNP:",width=5)
    label2.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    text2=tk.Text(t,width=40,height=1)
    text2.pack(side="top", fill="both", expand=True, padx=5, pady=5) 
    
    returneazabutton=tk.Button(t,text="Returneaza",command= lambda: ret())
    returneazabutton.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
def restante(root):
    t=tk.Toplevel(root)
    t.wm_title("Restante") 
    '''listbox=tk.Listbox(t)
    listbox.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    listbox.insert("end",controller.restante())'''
    
    tabel=ttk.Treeview(t,columns=('Titlu','Autor','Nume','Prenume','CNP'))
    tabel.heading('#0', text="Titlu",anchor=tk.CENTER)
    tabel.heading('#1', text="Nume",anchor=tk.CENTER)
    tabel.heading('#2', text="Prenume",anchor=tk.CENTER)
    tabel.heading('#3', text="Autor",anchor=tk.CENTER)
    tabel.heading('#4', text="CNP",anchor=tk.CENTER)
    tabel.column('#1', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#2', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#3', stretch=tk.YES, minwidth=50, width=100)
    tabel.column('#4', stretch=tk.YES, minwidth=50, width=100)
    tabel.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    for row in controller.restante():
        tabel.insert('','end',text=str(row[0]),values=(row[1],row[2],row[3],row[4]))
    
def addBookWindow(root):
    t=tk.Toplevel(root)
    #t.wm_title("Adauga carte #%s" % counter)
    t.wm_title("Adauga carte" )
    #l=tk.Label(t, text="This is window #%s" % counter)
    #l.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
    label1=tk.Label(t,text="Nr inv:",width=5)
    label1.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    global text1
    text1=tk.Text(t,width=40,height=1)
    text1.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
    label2=tk.Label(t,text="Titlu:",width=5)
    label2.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    global text2
    text2=tk.Text(t,width=40,height=1)
    text2.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
    label3=tk.Label(t,text="Autor:",width=5)
    label3.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    global text3
    text3=tk.Text(t,width=40,height=1)
    text3.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
    label4=tk.Label(t,text="Editura:",width=5)
    label4.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    global text4
    text4=tk.Text(t,width=40,height=1)
    text4.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
    label5=tk.Label(t,text="An aparitie:",width=5)
    label5.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    global text5
    text5=tk.Text(t,width=40,height=1)
    text5.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
    label6=tk.Label(t,text="Cod de bare:",width=5)
    label6.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    global text6
    text6=tk.Text(t,width=40,height=1)
    text6.pack(side="top", fill="both", expand=True, padx=5, pady=5)
     
    label7=tk.Label(t,text="ISBN:",width=5)
    label7.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    global text7
    text7=tk.Text(t,width=40,height=1)
    text7.pack(side="top", fill="both", expand=True, padx=5, pady=5)    
    
    label8=tk.Label(t,text="Nr exemplare:",width=5)
    label8.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    global text8
    text8=tk.Text(t,width=40,height=1)
    text8.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
    adaugabutton=tk.Button(t,text="Adauga",command= lambda: adaugacarte())
    adaugabutton.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    
def adaugacarte():
    try:
        nrinv=text1.get("1.0","end")
        titlu=text2.get("1.0","end")
        autor=text3.get("1.0","end")
        editura=text4.get("1.0","end")
        anap=text5.get("1.0","end")
        codbare=text6.get("1.0","end")
        isbn=text7.get("1.0","end")
        nrex=text8.get("1.0","end")
        c=Book(nrinv,titlu,autor,editura,anap,codbare,isbn,nrex)
        controller.addBook(c)
        tk.messagebox.showinfo(message="Cartea a fost adaugata cu succes")
    except MyException as ex:
        tk.messagebox.showerror(message=str(ex))

    
def adaugacititor():
    try:
        nume=text21.get("1.0","end")
        prenume=text22.get("1.0","end")
        cnp=text23.get("1.0","end")
        serieci=text24.get("1.0","end")
        nrci=text25.get("1.0","end")
        adresa=text26.get("1.0","end")
        tel=text27.get("1.0","end")
        c=Reader(nume,prenume,cnp,serieci,nrci,adresa,tel)
        Controller().addReader(c)
        tk.messagebox.showinfo(message="Cititorul a fost adaugat cu succes")
    except MyException as ex:
        tk.messagebox.showerror(message=str(ex))
    
def main():
    root = tk.Tk()
    root.title("Library")
    root.geometry=("960x540")
    main=MainWindow(root)
    root.mainloop()

main()