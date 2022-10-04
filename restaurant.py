from faulthandler import disable
from tkinter import *
from tkinter import messagebox
from tkinter import ttk,Entry
import  customtkinter
import mysql.connector
import tkcalendar
from tkcalendar import DateEntry

def callback(event):
    ligne_id = tableAfficher.selection()[0]
    selection=tableAfficher.set(ligne_id)
    if selection:
        txtid.delete(0, END)
        txtprix.delete(0, END)

        txttype.set(selection['2'])
        txtid.insert(0,selection['1'])
        txtprix.insert(0,selection['3'])
        v7.set(selection['4'])
       
        print(selection)
    else:
        print('nnnn')

def Ajouter():
   #id=lblid.get()
   type_nourriture=txttype.get()
   prix=txtprix.get()
   date_achat=txtdate.get()
   if(type_nourriture=="" or prix=="" or date_achat==""):
       messagebox.showinfo("Echec", "Tous les  champs sont requis")
   else:
       mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hotel")
       meconnect=mysqldb.cursor()
       sql="insert into restaurant (type_nourriture,prix,date_achat)values(%s,%s,%s)"
       val=(type_nourriture,prix,date_achat)
       meconnect.execute(sql,val)
       mysqldb.commit()
       lastid = meconnect.lastrowid
       messagebox.showinfo("info","enregistrer avec succes")
       tableAfficher.delete(*tableAfficher.get_children())
       #txtid.delete(0,END)
      # txttype.delete(0,END)
       #txtprix.delete(0,END)
       #txtdate.delete(0,END)
      # mysqldb.rollback()
       mysqldb.close()
       afficher()

def modifier():
    id = int(txtid.get())
    type_nourriture = txttype.get()
    prix = txtprix.get()
    date_achat=txtdate.get()
    if (type_nourriture == "" or prix == "" or date_achat == ""):
        messagebox.showinfo("Echec", "Tous les  champs sont requis")
    else:
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="hotel")
        mycursor = mysqldb.cursor()
        sql = "Update  restaurant set type_nourriture=%s,prix=%s,date_achat=%s  where id=%s"
        val = (type_nourriture,prix,date_achat,id)
        mycursor.execute(sql, val)
        mysqldb .commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "modifier avec succes")
        tableAfficher.delete(*tableAfficher.get_children())
       # txttype.delete(0, END)
       # txtprix.delete(0, END)
       # txtdate.delete(0, END)
        mysqldb.rollback()
        mysqldb.close()
        afficher()
def supprimer():
        id= int(txtid.get())
        if (txtid.get() == ""):
            messagebox.showinfo("Echec", " le  champs est requis")
        else:
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="hotel")
            meconnect = mysqldb.cursor()
            sql = 'delete from restaurant where id=%s'
            val = (id,)
            meconnect.execute(sql, val)
            mysqldb.commit()
            lastid = meconnect.lastrowid
            messagebox.showinfo("info", "supprimer avec succès")
            tableAfficher.delete(*tableAfficher.get_children())
            #txtid.delete(0, END)
           # txttype.delete(0, END)
            #txtprix.delete(0, END)
            #txtdate.delete(0,END)
            mysqldb.rollback()
            mysqldb.close()
            afficher()



"""def rechercher():
    id = txtid.get()
    if (txtid.get() == ""):
        messagebox.showinfo("search status", "Le champ id ne doit pas être vide")
        # desactiver le boutton rechercher quand le champ id est rempli
        if txtid != 0:
            rechercher.configure(State=disable)
    else:
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="pas6190sfst", database="HÔTEL")
        cursor = mysqldb.cursor()
        cursor.execute("select type_nourriture,prix,date_achat from restaurant where id = '" + str(txtid.get()) + "' ;")
        rows = cursor.fetchall()
        print(rows)
        mysqldb.commit()
        for row in rows:
            txttype.insert(0, row[1])
            txtprix.insert(0, row[2])
            txtdate.insert(0, row[3])
            # txttelephone.insert(0, row[2])
            afficher()
            mysqldb.close()"""
def rechercher():
    
    conn=mysql.connector.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')
    cur=conn.cursor()
    cur.execute("select id,type_nourriture,prix,date_achat from restaurant where "+str(type_rechercher.get())+" LIKE '%"+str(txtrechercher.get())+"%' ;")
    tableAfficher.delete(*tableAfficher.get_children())
    output=cur.fetchall()
    print(output,type_rechercher.get())
    for i in output:
        tableAfficher.insert('',END,values=i)
    conn.close()

root = Tk()
root.title("Aw KA HOTEL")
root.geometry("1000x650")
root.resizable(False, False)
root.attributes("-toolwindow",1)
root.configure(background='#4B4745')

def dashboard():
    root.destroy()
   
b4 = Button(master=root,text='<-',font=("Arial",16),background='#FFFFFF',width=5,command=dashboard)
b4.place(x=0, y=30)

lbltitre = customtkinter.CTkLabel(master=root,text="BIENVENU SUR LA PAGE DE GESTION DE RESTAURANT",text_font=('Arial',20),height=40,width=100,border=1,corner_radius=20,bg_color="white",)
lbltitre.place(x=0, y=0, width=1000)

lblid = Label(root, text="Id", font=("sans serif", 14), background='#60554F', foreground='#FFFFFF')
lblid.place(x=10, y=130, width=80)
txtid=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtid.place(x=200,y=130,width=160)
lbltype = Label(root, text="Type_Nourriture", font=("sans serif", 14), background='#60554F', foreground='#FFFFFF')
lbltype.place(x=0, y=200, width=220)

v2=StringVar()
txttype=customtkinter.CTkComboBox(master=root,height=30,width=40,values=("Pizza","Vin_rouge","hamburger","patê arachide","Salade"),variable=v2, corner_radius=20,fg_color="#FFFFFF")
txttype.place(x=200,y=196,width=160)

lblprix = Label(root, text="Prix_Nourriture", font=("sans serif", 14), background='#60554F', foreground='#FFFFFF')
lblprix.place(x=0, y=270, width=220)
txtprix=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtprix.place(x=200,y=266,width=160)

lbldate = Label(root, text="Date_achat", font=("sans serif", 14), background='#60554F', foreground='#FFFFFF')
lbldate.place(x=0, y=335, width=190)
v7=StringVar()
txtdate= DateEntry(master=root,height=30,width=40,textvariable=v7,font=("Inter",15),border_width=1,corner_radius=20,fg_color="#FFFFFF",date_pattern="dd/mm/yy")
txtdate.place(x=200,y=336,width=160)


buttrechercher= customtkinter.CTkButton(master=root,text="Rechercher",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF",command=rechercher)
buttrechercher.place(x=230,y=510,width=110)

v8=StringVar()
type_rechercher=customtkinter.CTkComboBox(master=root,values=("type_nourriture","prix","id","date_achat"),variable=v8,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
type_rechercher.place(x=10,y=450,width=160)


v9=StringVar()
txtrechercher=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtrechercher.place(x=200,y=450,width=160)

#txtrechercher=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
#txtrechercher.place(x=200,y=420,width=160)

buttEnregistrer= customtkinter.CTkButton(master=root,text="Enregistrer",command=Ajouter,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttEnregistrer.place(x=10,y=560,width=100)


buttmodifier= customtkinter.CTkButton(master=root,text="Modifier",command=modifier,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttmodifier.place(x=115,y=560,width=100)


buttonsupp= customtkinter.CTkButton(master=root,text="Supprimer",command=supprimer,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttonsupp.place(x=230,y=560,width=100)

tableAfficher = ttk.Treeview(root, columns=(1, 2, 3,4), height=10, show="headings")
tableAfficher.place(x=400, y=130, width=600, height=600)
style = ttk.Style(root)
style.configure("Treeview",background="#D9D9D9")
# Entete
tableAfficher.heading(1, text="Id")
tableAfficher.heading(2, text="Type_Nourriture")
tableAfficher.heading(3, text="Prix_Nourriture")
tableAfficher.heading(4, text="date_achat")


# definir les dimentions des colonnes
tableAfficher.column(1, width=10)
tableAfficher.column(2, width=40)
tableAfficher.column(3, width=40)

"""liste = ["a","b","c"]
tableAfficher.insert('',1,values=liste)

mysqldb=mysql.connector.connect(host="localhost",user="root",password="pas6190sfst",database="HÔTEL")
meconnect=mysqldb.cursor()
meconnect.execute("select * from restaurant")
for row in meconnect:
    tableAfficher.insert('',END,values=row)"""
tableAfficher.bind("<Double-Button>",callback)
def afficher():
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hotel")
    meconnect=mysqldb.cursor()
    meconnect.execute("select * from restaurant;")
    a=meconnect.fetchall()
    print(a)
    for row in a:
        tableAfficher.insert('',END,values=row)
        mysqldb.close()
afficher()
root.mainloop()