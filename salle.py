from tkinter import *
from tkinter import messagebox
from tkinter import ttk, Entry
import customtkinter
from subprocess import call
import mysql.connector
from future.builtins import disabled


# from PIL import ImageTk, Image

def reservation():
    root.destroy()
    call(["python", "Reservation salle.py"])

def callback(event):
    ligne_id = tableAfficher.selection()[0]
    selection=tableAfficher.set(ligne_id)
    if selection:
        txtnum_salle.delete(0, END)
       
        txtnum_salle.insert(0,selection['1'])
        txtcategorie_salle.set(selection['2'])
       
        print(selection)
    else:
        print('nnnn')



def Ajouter():
    num_salle = txtnum_salle.get()
    categorie_salle = txtcategorie_salle.get()
    if (categorie_salle == ""):
        messagebox.showinfo("Echec", "Tous les  champs sont requis")
    else:
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="hotel")
        meconnect = mysqldb.cursor()
        sql = "insert into salle(categorie_salle)values(%s)"
        val = (categorie_salle,)
        meconnect.execute(sql, val)
        mysqldb.commit()
        lastid = meconnect.lastrowid
        messagebox.showinfo("info", "enregistrer avec succes")
        tableAfficher.delete(*tableAfficher.get_children())
        txtnum_salle.delete(0, END)
        mysqldb.rollback()
        afficher()
        mysqldb.close()


def modifier():
    num_salle = int(txtnum_salle.get())
    categorie_salle = txtcategorie_salle.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="hotel")
    mycursor = mysqldb.cursor()
    sql = "Update  salle set categorie_salle=%s where num_salle=%s"
    val = (categorie_salle, num_salle)
    mycursor.execute(sql, val)
    mysqldb.commit()
    lastid = mycursor.lastrowid
    messagebox.showinfo("information", "modifier avec succes")
    tableAfficher.delete(*tableAfficher.get_children())
    txtnum_salle.delete(0, END)
    mysqldb.rollback()
    afficher()
    mysqldb.close()


def supprimer():
    num_salle = int(txtnum_salle.get())
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="hotel")
    meconnect = mysqldb.cursor()
    sql = 'delete from salle where num_salle=%s'
    val = (num_salle,)
    meconnect.execute(sql, val)
    mysqldb.commit()
    lastid = meconnect.lastrowid
    messagebox.showinfo("info", "supprimer avec succès")
    tableAfficher.delete(*tableAfficher.get_children())
    txtnum_salle.delete(0, END)
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
    cur.execute("select num_salle,categorie_salle from salle where "+str(type_rechercher.get())+" LIKE '%"+str(txtrechercher.get())+"%' ;")
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

lbltitre = customtkinter.CTkLabel(master=root, text="Bienvenue sur la page de gestion des salles",
                                  text_font=("sans serif", 20), height=30, width=40, border=1, 
                                  fg_color="#FFFFFF", )
lbltitre.place(x=0, y=0, width=1000)

lblnom = Label(root, text="Num_Salle", font=("sans serif", 14), background='#60554F', foreground='#D9D9D9')
lblnom.place(x=10, y=150, width=150)
txtnum_salle = customtkinter.CTkEntry(master=root, height=30, width=40, border_width=1, corner_radius=20,
                                      fg_color="#FFFFFF")
txtnum_salle.place(x=200, y=150, width=160)
lblprenom = Label(root, text="Cathegorie_Salle", font=("sans serif", 14), background='#60554F', foreground='#D9D9D9')
lblprenom.place(x=5, y=270, width=200)
txtcategorie_salle = customtkinter.CTkComboBox(master=root,values=("salle de reunion","salle des fetes"), border_width=1, corner_radius=20,fg_color="#FFFFFF")
txtcategorie_salle.place(x=200, y=270, width=160)

buttrechercher = customtkinter.CTkButton(master=root, text="Rechercher", height=30, width=40, border_width=1,command=rechercher,corner_radius=20, fg_color="#FFFFFF")
buttrechercher.place(x=220, y=500, width=110)

v8=StringVar()
type_rechercher=customtkinter.CTkComboBox(master=root,values=("num_salle","categorie_salle"),variable=v8,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
type_rechercher.place(x=10,y=450,width=160)


v9=StringVar()
txtrechercher=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtrechercher.place(x=200,y=450,width=160)


def reservation_salle():
    call(["python", "Reservation_salle.py"])

buttmoreservation = customtkinter.CTkButton(master=root, text="Reservation", height=30, width=40, border_width=1,
                                       corner_radius=20, fg_color="#FFFFFF",command=reservation_salle)
buttmoreservation.place(x=10, y=350, width=150)


     


buttEnregistrer = customtkinter.CTkButton(master=root, text="Enregistrer", command=Ajouter, height=30, width=40,
                                          border_width=1, corner_radius=20, fg_color="#FFFFFF")
buttEnregistrer.place(x=10, y=560, width=100)

buttmodifier = customtkinter.CTkButton(master=root, text="Modifier", command=modifier, height=30, width=40,
                                       border_width=1, corner_radius=20, fg_color="#FFFFFF")
buttmodifier.place(x=115, y=560, width=100)

buttonsupp = customtkinter.CTkButton(master=root, text="Supprimer", command=supprimer, height=30, width=40,
                                     border_width=1, corner_radius=20, fg_color="#FFFFFF")
buttonsupp.place(x=220, y=560, width=100)

tableAfficher = ttk.Treeview(root, columns=(1, 2), height=10, show="headings")
tableAfficher.place(x=400, y=130, width=600, height=600)
style = ttk.Style(root)
style.configure("Treeview", background="#D9D9D9")
# Entete
tableAfficher.heading(1, text="Num_Salle")
tableAfficher.heading(2, text="Categorie")

# definir les dimentions des colonnes
tableAfficher.column(1, width=100)
tableAfficher.column(2, width=100)
tableAfficher.bind("<Double-Button>",callback)


def afficher():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="hotel")
    meconnect = mysqldb.cursor()
    meconnect.execute("select * from salle")
    a = meconnect.fetchall()
    print(a)
    for row in a:
        tableAfficher.insert('', END, values=row)
        mysqldb.close()


afficher()

root.mainloop()