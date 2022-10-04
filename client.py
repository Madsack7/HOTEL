from faulthandler import disable
from logging.handlers import RotatingFileHandler
from sre_parse import State
from tkinter import *
from tkinter import messagebox
from tkinter import ttk,Entry
import customtkinter
import pymysql
import mysql.connector

def callback(event):
    ligne_id = tableAfficher.selection()[0]
    selection=tableAfficher.set(ligne_id)
    if selection:
        txtnom.delete(0, END)
        txtprenom.delete(0, END)
        txttelephone.delete(0, END)
        txtnom.insert(0,selection['2'])
        txtprenom.insert(0,selection['3'])
        txttelephone.insert(0,selection['1'])
       
        print(selection)
    else:
        print('nnnn')


def Ajouter():
   nom=txtnom.get()
   prenom=txtprenom.get()
   telephone=txttelephone.get()
   if(nom=="" or prenom=="" or telephone==""):
       messagebox.showinfo("Echec","Tous les  champs sont requis")
  
   else:
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hotel")
    meconnect=mysqldb.cursor()
    sql="insert into client (telephone,nom, prenom)values(%s,%s,%s)"
    val=(telephone,nom,prenom)
    meconnect.execute(sql,val)
    mysqldb.commit()
    lastid = meconnect.lastrowid
   # tableAfficher.delete(*tableAfficher.get_children())
    messagebox.showinfo("info","enregistrer avec succes")
    tableAfficher.delete(*tableAfficher.get_children())
    txtnom.delete(0,END)
    txtprenom.delete(0,END)
    txttelephone.delete(0,END)
    mysqldb.rollback()
    mysqldb.close()
    afficher()

def modifier():
    nom= txtnom.get()
    prenom = txtprenom.get()
    telephone = txttelephone.get()
    if(nom=="" or prenom=="" or telephone==""):
       messagebox.showinfo("Echec","Tous les  champs sont requis")
    else:
     mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="hotel")
     mycursor = mysqldb.cursor()
     sql = "Update  client set nom=%s,prenom=%s where telephone=%s"
     val = (nom,prenom,telephone)
     mycursor.execute(sql, val)
     mysqldb.commit()
     lastid = mycursor.lastrowid
     messagebox.showinfo("information", "modifier avec succes")
     tableAfficher.delete(*tableAfficher.get_children())
     txtnom.delete(0, END)
     txtprenom.delete(0, END)
     txttelephone.delete(0, END)
     mysqldb.rollback()
     mysqldb.close()
     afficher()

def supprimer():
     if(txttelephone.get()==""):
       messagebox.showinfo("Echec"," le  champs est requis")
     else:
        
        telephone= str(txttelephone.get())
        print(telephone)
        mysqldb = pymysql.connect(host="localhost", user="root", password="", database="hotel")
        meconnect = mysqldb.cursor()
        sql = 'delete from client where telephone=%s'
        
        meconnect.execute(sql, telephone)
        mysqldb.commit()
        lastid = meconnect.lastrowid
        messagebox.showinfo("info", "supprimer avec succès")
        tableAfficher.delete(*tableAfficher.get_children())
        txtnom.delete(0, END)
        txtprenom.delete(0, END)
        txttelephone.delete(0, END)
        mysqldb.rollback()
        mysqldb.close()
        afficher()

def rechercher():
    
    conn=mysql.connector.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')
    cur=conn.cursor()
    cur.execute("select telephone,nom,prenom from client where "+str(type_rechercher.get())+" LIKE '%"+str(txtrechercher.get())+"%' ;")
    tableAfficher.delete(*tableAfficher.get_children())
    output=cur.fetchall()
    print(output,type_rechercher.get())
    for i in output:
        tableAfficher.insert('',END,values=i)
    conn.close()


root = Tk()
root.title("Aw KA HOTEL")
root.geometry("1000x650")
root.attributes("-toolwindow",1)

root.resizable(False, False)
# root.resizable(False, False)
root.configure(background='#4B4745')

def dashboard():
    root.destroy()
   
b4 = Button(master=root,text='<-',font=("Arial",16),background='#FFFFFF',width=5,command=dashboard)
b4.place(x=0, y=30)

lbltitre = customtkinter.CTkLabel(master=root, text="BIENVENUE SUR LA PAGE DE GESTION DES CLIENTS",
                                  text_font=("sans serif", 20), height=30, width=40, border=1, corner_radius=20,
                                  bg_color="#FCFAFA", )
lbltitre.place(x=0, y=0, width=1000)

lblnom = Label(root, text="Nom", font=("sans serif", 14), background='#60554F', foreground='#FCFFFF')
lblnom.place(x=10, y=130, width=60)
txtnom=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtnom.place(x=200,y=130,width=160)


lblprenom = Label(root, text="Prénom", font=("sans serif", 14), background='#60554F', foreground='#FCFFFF')
lblprenom.place(x=10, y=190, width=80)
txtprenom=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtprenom.place(x=200,y=190,width=160)

lbltelephone = Label(root, text="Téléphone", font=("sans serif", 14), background='#60554F', foreground='#FCFFFF')
lbltelephone.place(x=10, y=250, width=90)
txttelephone=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txttelephone.place(x=200,y=250,width=160)

buttrechercher= customtkinter.CTkButton(master=root,text="Rechercher",command=rechercher,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttrechercher.place(x=230,y=510,width=110)

v8=StringVar()
type_rechercher=customtkinter.CTkComboBox(master=root,values=("telephone","nom", "prenom"),variable=v8,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
type_rechercher.place(x=10,y=450,width=160)


v9=StringVar()
txtrechercher=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtrechercher.place(x=200,y=450,width=160)

#txtrechercher=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
#txtrechercher.place(x=160,y=510,width=160)

buttEnregistrer= customtkinter.CTkButton(master=root,text="Enregistrer",command=Ajouter,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttEnregistrer.place(x=10,y=560,width=100)


buttmodifier= customtkinter.CTkButton(master=root,text="Modifier",command=modifier,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttmodifier.place(x=120,y=560,width=100)


buttonsupp= customtkinter.CTkButton(master=root,text="Supprimer",command=supprimer,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttonsupp.place(x=230,y=560,width=100)


tableAfficher = ttk.Treeview(root, columns=(1, 2, 3), height=10, show="headings")
tableAfficher.place(x=400, y=130, width=600, height=600)
style = ttk.Style(root)
style.configure("Treeview",background="#D9D9D9")
# Entete
tableAfficher.heading(1, text="Téléphone")
tableAfficher.heading(2, text="Nom")
tableAfficher.heading(3, text="Prénom") 
# definir les dimentions des colonnes
tableAfficher.column(1, width=10)
tableAfficher.column(2, width=40)
tableAfficher.column(3, width=40)

"""liste = ["a","b","c"]
tableAfficher.insert('',1,values=liste)
root.state('zoomed')
mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hotel ")
meconnect=mysqldb.cursor()
meconnect.execute("select * from client")
for row in meconnect:
    tableAfficher.insert('',END,values=row)."""

tableAfficher.bind("<Double-Button>",callback)
#afficher
def afficher():
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hotel")
    meconnect=mysqldb.cursor()
    meconnect.execute("select * from client;")
    a=meconnect.fetchall()
    print(a)
    for row in a:
        tableAfficher.insert('',END,values=row)
        mysqldb.close()
        
afficher()
root.mainloop()