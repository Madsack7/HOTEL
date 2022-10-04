
from email import message
from faulthandler import disable
from tkinter import*
from tkinter import messagebox
from unicodedata import category

from PIL import ImageTk, Image
from tkinter import ttk,Entry
import  customtkinter
from subprocess import call
import pymysql


def callback(event):
    ligne_id = tableAfficher.selection()[0]
    selection=tableAfficher.set(ligne_id)
    if selection:
        txtnum_chambre.delete(0, END)
       

        txtcategorie.set(selection['2'])
        txtnum_chambre.insert(0,selection['1'])
       
        print(selection)
    else:
        print('nnnn')

def Ajouter():
   categorie=txtcategorie.get()
   if( categorie==""):
      messagebox.showinfo("Echec","Tous les  champs sont requis")
  
   else:
    mysqldb= pymysql.connect(host="localhost",user="root",password="",database="hotel")
    meconnect=mysqldb.cursor()
    sql="insert into chambre (categorie) values(%s);"
    val=str(categorie)
    meconnect.execute(sql,val)
    mysqldb.commit()
    lastid = meconnect.lastrowid
   # tableAfficher.delete(*tableAfficher.get_children())
    messagebox.showinfo("info","enregistrer avec succes")
    tableAfficher.delete(*tableAfficher.get_children())
    #txtcategorie.delete(0,END)
    mysqldb.rollback()
    mysqldb.close()
    afficher()

   
def modifier():
    cat=txtcategorie.get()
    num_chambre=int(txtnum_chambre.get())
    if(num_chambre=="" ):
       messagebox.showinfo("Echec","Tous les  champs sont requis")
    else:
     mysqldb = pymysql.connect(host="localhost", user="root", password="", database="hotel")
     mycursor = mysqldb.cursor()
     sql = "Update  chambre set categorie=%s where num_chambre=%s"
     val = (cat,num_chambre)
     mycursor.execute(sql, val)
     mysqldb.commit()
     lastid = mycursor.lastrowid
     messagebox.showinfo("information", "modifier avec succes")
     tableAfficher.delete(*tableAfficher.get_children())
     #txtcategorie.delete(0, END)
     txtnum_chambre.delete(0,END)
    
     mysqldb.close()
     afficher()


def supprimer():
     if(txtnum_chambre.get()==""):
       messagebox.showinfo("Echec"," le  champs est requis")
     else:
        num_chambre= int(txtnum_chambre.get())
        mysqldb = pymysql.connect(host="localhost", user="root", password="", database="hotel")
        meconnect = mysqldb.cursor()
        sql = 'delete from chambre where num_chambre=%s'
        
        meconnect.execute(sql, num_chambre)
        mysqldb.commit()
        lastid = meconnect.lastrowid
        messagebox.showinfo("info", "supprimer avec succès")
        tableAfficher.delete(*tableAfficher.get_children())
        txtnum_chambre.delete(0, END)
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
    cur.execute("select num_chambre,categorie from chambre where "+str(type_rechercher.get())+" LIKE '%"+str(txtrechercher.get())+"%' ;")
    tableAfficher.delete(*tableAfficher.get_children())
    output=cur.fetchall()
    print(output,type_rechercher.get())
    for i in output:
        tableAfficher.insert('',END,values=i)
    conn.close()

fenetre=Tk()
fenetre.title("AW KA HOTEL")
fenetre.resizable(False, False)
fenetre.attributes("-toolwindow",1)
fenetre.geometry("1000x650")
fenetre.config(background='#4B4745')

lbltitre = customtkinter.CTkLabel(master=fenetre,text="BIENVENUE SUR LA PAGE DE GESTION DES CHAMBRES",text_font=('Arial',20),height=40,width=100,border=1,corner_radius=20,bg_color="white",)
lbltitre.place(x=0, y=0, width=1000)

lblnum_chambre = Label(fenetre, text="Num_Chambre", font=("sans serif", 14),background='#5C4D4D', foreground='#FFFFFF')
lblnum_chambre.place(x=10, y=200, width=150)


txtnum_chambre=customtkinter.CTkEntry(master=fenetre,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtnum_chambre.place(x=230,y=200,width=160)


lblcategorie = Label(fenetre, text="Cathegorie_Chambre", font=("sans serif", 14), background='#5C4D4D', foreground='#FFFFFF')
lblcategorie.place(x=5, y=300, width=200)

v4=StringVar()
txtcategorie=customtkinter.CTkComboBox(master=fenetre,values=("chambre simple","chambre dortoir","chambre double"),variable=v4,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtcategorie.place(x=230,y=300,width=160)

buttrechercher= customtkinter.CTkButton(master=fenetre,text="Rechercher",command=rechercher,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF",)
buttrechercher.place(x=260,y=510,width=110)

v8=StringVar()
type_rechercher=customtkinter.CTkComboBox(master=fenetre,values=("num_chambre","categorie"),variable=v8,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
type_rechercher.place(x=10,y=450,width=160)


v9=StringVar()
txtrechercher=customtkinter.CTkEntry(master=fenetre,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtrechercher.place(x=230,y=450,width=160)

"""texteRechercher=customtkinter.CTkEntry(master=fenetre,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
texteRechercher.place(x=160,y=510,width=160)"""

def salle():
    call(["python", "Reservation_chambre.py"])

buttReserver= customtkinter.CTkButton(master=fenetre,text="Réservation",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF",command=salle)
buttReserver.place(x=10,y=360,width=110)

buttEnregistrer= customtkinter.CTkButton(master=fenetre,text="Enregistrer",command=Ajouter,height=30,width=50,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttEnregistrer.place(x=10,y=560,width=100)


buttmodifier= customtkinter.CTkButton(master=fenetre,text="Modifier",height=30,command=modifier,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttmodifier.place(x=130,y=560,width=110)


buttonsupp= customtkinter.CTkButton(master=fenetre,text="Supprimer",command=supprimer,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttonsupp.place(x=260,y=560,width=110)

def dashboard():
    fenetre.destroy()
                
b4 = Button(text='<-',font=("Arial",16),background='#FFFFFF',width=5,command=dashboard)
b4.place(x=0, y=40)


tableAfficher = ttk.Treeview(fenetre, columns=(1, 2), height=10, show="headings")
tableAfficher.place(x=400, y=130, width=600, height=600)
style = ttk.Style(fenetre)
style.configure("Treeview",background="#D9D9D9")
# Entete
tableAfficher.heading(1, text="NumChambre")
tableAfficher.heading(2, text="Catégorie")

# definir les dimentions des colonnes
tableAfficher.column(1, width=10)
tableAfficher.column(2, width=40)

tableAfficher.bind("<Double-Button>",callback)

def afficher():
    mysqldb=pymysql.connect(host="localhost",user="root",password="",database="hotel")
    meconnect=mysqldb.cursor()
    meconnect.execute("select * from chambre;")
    a=meconnect.fetchall()
    print(a)
    for row in a:
        tableAfficher.insert('',END,values=row)
        #mysqldb.close()


afficher()




fenetre.mainloop()
