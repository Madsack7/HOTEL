import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk,Entry
import  customtkinter
import mysql.connector
import pymysql
from future.builtins import disabled
from tkcalendar import DateEntry


def callback(event):
    ligne_id = tableAfficher.selection()[0]
    selection=tableAfficher.set(ligne_id)
    if selection:
        txtnom.delete(0, END)
        txtprenom.delete(0, END)
        txttelephone.delete(0, END)
        txtsalaire.delete(0, END)
        
        txtnom.insert(0,selection['1'])
        txtprenom.insert(0,selection['2'])
        txttelephone.insert(0,selection['3'])
        txtsalaire.insert(0,selection['4'])
        v7.set(selection['5'])
       
        print(selection)
    else:
        print('nnnn')

def Ajouter():
   nom=txtnom.get()
   prenom=txtprenom.get()
   telephone=txttelephone.get()
   salaire=txtsalaire.get()
   date_embauche=txtdate_embauche.get()
   if(nom=="" or prenom=="" or telephone=="" or salaire=="" or date_embauche==""):
       messagebox.showinfo("Echec","Tous les  champs sont requis")
   else:
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hotel")
    meconnect=mysqldb.cursor()
    sql="insert into employe(nom, prenom, telephone,salaire,date_embauche)values(%s,%s,%s,%s,%s)"
    val=(nom,prenom,telephone,salaire,date_embauche)
    meconnect.execute(sql,val)
    mysqldb.commit()
    lastid = meconnect.lastrowid
    messagebox.showinfo("info","enregistrer avec succes")
    tableAfficher.delete(*tableAfficher.get_children())
    txtnom.delete(0,END)
    txtprenom.delete(0,END)
    txttelephone.delete(0,END)
    txtsalaire.delete(0,END)
    txtdate_embauche.delete(0,END)
    mysqldb.rollback()
    mysqldb.close()
    afficher()
def modifier():
    nom=txtnom.get()
    prenom=txtprenom.get()
    telephone = txttelephone.get()
    salaire=txtsalaire.get()
    date_embauche=txtdate_embauche.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="hotel")
    mycursor = mysqldb.cursor()
    sql = "Update  employe set nom=%s,prenom=%s,salaire=%s,date_embauche=%s where telephone=%s"
    val = (nom, prenom, salaire,date_embauche,telephone)
    mycursor.execute(sql, val)
    mysqldb.commit()
    lastid = mycursor.lastrowid
    messagebox.showinfo("information", "modifier avec succes")
    tableAfficher.delete(*tableAfficher.get_children())

    txtnom.delete(0, END)
    txtprenom.delete(0, END)
    txttelephone.delete(0, END)
    txtsalaire.delete(0,END)
    txtdate_embauche.delete(0,END)
    mysqldb.rollback()
    mysqldb.close()
    afficher()
def supprimer():
        telephone= txttelephone.get()
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="hotel")
        meconnect = mysqldb.cursor()
        sql = 'delete from employe where telephone=%s'
        val = (telephone,)
        meconnect.execute(sql, val)
        mysqldb.commit()
        lastid = meconnect.lastrowid
        messagebox.showinfo("info", "supprimer avec succès")
        tableAfficher.delete(*tableAfficher.get_children())
        txtnom.delete(0, END)
        txtprenom.delete(0, END)
        txttelephone.delete(0, END)
        txtsalaire.delete(0, END)
        txtdate_embauche.delete(0, END)
        mysqldb.rollback()
        mysqldb.close()
        afficher()
def rechercher():
    
    conn=pymysql.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')
    cur=conn.cursor()
    cur.execute("select nom,prenom,telephone,salaire,date_embauche from employe where "+str(type_rechercher.get())+" LIKE '%"+str(txtrechercher.get())+"%' ;")
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
root.configure(background='#4B4745')

def dashboard():
    root.destroy()
   
b4 = Button(master=root,text='<-',font=("Arial",16),background='#FFFFFF',width=5,command=dashboard)
b4.place(x=0, y=30)

lbltitre = customtkinter.CTkLabel(master=root,text="BIENVENUE SUR LA PAGE DE GESTION DES EMPLOYES",text_font=("sans serif",20),height=30,fg_color="white",width=40,border=1,corner_radius=20,bg_color="#D9D9D9")
lbltitre.place(x=0, y=0, width=1000)

lblnom = Label(root, text="Nom", font=("sans serif", 14), background='#60554F', foreground='#D9D9D9')
lblnom.place(x=10, y=130, width=80)
txtnom=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtnom.place(x=180,y=130,width=160)
lblprenom = Label(root, text="Prenom", font=("sans serif", 14), background='#60554F', foreground='#D9D9D9')
lblprenom.place(x=10, y=190, width=80)
txtprenom=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtprenom.place(x=180,y=190,width=160)

lblnumero = Label(root, text="Téléphone", font=("sans serif", 14), background='#60554F', foreground='#D9D9D9')
lblnumero.place(x=10, y=250, width=120)
txttelephone=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txttelephone.place(x=180,y=250,width=160)

lblsalaire = Label(root, text="Salaire", font=("sans serif", 14), background='#60554F', foreground='#D9D9D9')
lblsalaire.place(x=10, y=310, width=80)
txtsalaire=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtsalaire.place(x=180,y=310,width=160)

lbldate = Label(root, text="Date d'embauche", font=("sans serif", 14), background='#60554F', foreground='#D9D9D9')
lbldate.place(x=10, y=370, width=160)
v7=StringVar()
txtdate_embauche=DateEntry (master=root,height=30,width=30,textvariable=v7,font=("Inter",15),border_width=1,corner_radius=20,date_pattern="yy/mm/dd",fg_color="#FFFFFF")
txtdate_embauche.grid(row=1,column=1,padx=15)
txtdate_embauche.pack(padx=22)
txtdate_embauche.place(x=180,y=370,width=160)

buttrechercher= customtkinter.CTkButton(master=root,text="Rechercher",command=rechercher,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttrechercher.place(x=220,y=510,width=110)

v8=StringVar()
type_rechercher=customtkinter.CTkComboBox(master=root,values=("nom","prenom","salaire","date_embauche","telephone"),variable=v8,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
type_rechercher.place(x=10,y=450,width=160)


v9=StringVar()
txtrechercher=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtrechercher.place(x=180,y=450,width=160)
#txtrechercher=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
#txtrechercher.place(x=180,y=450,width=160)

buttEnregistrer= customtkinter.CTkButton(master=root,text="Enregistrer",command=Ajouter,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttEnregistrer.place(x=10,y=560,width=100)


buttmodifier= customtkinter.CTkButton(master=root,text="Modifier",command=modifier,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttmodifier.place(x=115,y=560,width=100)


buttonsupp= customtkinter.CTkButton(master=root,text="Supprimer",command=supprimer,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttonsupp.place(x=220,y=560,width=100)

tableAfficher = ttk.Treeview(root, columns=(1, 2, 3, 4, 5), height=10, show="headings")
tableAfficher.place(x=400, y=130, width=600, height=600)
style = ttk.Style(root)
style.configure("Treeview",background="#D9D9D9")
# Entete
tableAfficher.heading(1, text="Nom")
tableAfficher.heading(2, text="Prenom")
tableAfficher.heading(3, text="téléphone")
tableAfficher.heading(4, text="salaire")
tableAfficher.heading(5, text="Date_embauche")
# definir les dimentions des colonnes
tableAfficher.column(1, width=10)
tableAfficher.column(2, width=40)
tableAfficher.column(3, width=40)
tableAfficher.column(4, width=40)
tableAfficher.column(5, width=40)


tableAfficher.bind("<Double-Button>",callback)
def afficher():
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hotel")
    meconnect=mysqldb.cursor()
    meconnect.execute("select * from employe")
    a=meconnect.fetchall()
    print(a)
    for row in a:
        tableAfficher.insert('',END,values=row)
        mysqldb.close()
afficher()
root.mainloop()