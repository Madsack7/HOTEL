from cgitb import text
from logging import root
from tkinter import *
from tkinter import messagebox
from tkinter import ttk,Entry
import  customtkinter
import pymysql
from subprocess import call
root=Tk()


    
    

root.title("Aw KA HOTEL")
root.geometry("1000x650")
root.attributes("-toolwindow",1)
root.iconbitmap("image\icone_logo.ico")
root.resizable(False, False)
root.configure(background='#4B4745')

def dashboard():
    root.destroy()
    
b4 = Button(text='<-',font=("Arial",16),background='#FFFFFF',width=5,command=dashboard)
b4.place(x=0, y=30)

lbltitre = customtkinter.CTkLabel(master=root,text="Bienvenue sur la page de gestion des utilisateurs",text_font=("sans serif",20),height=30,fg_color="white",width=40,border=1,corner_radius=20,bg_color="#D9D9D9")
lbltitre.place(x=0, y=0, width=1280)

lblnom = Label(root, text="Nom", font=("sans serif", 14), background='#60554F', foreground='#FFFFFF')
lblnom.place(x=10, y=130, width=60)
v1=StringVar()
entre_nom=customtkinter.CTkEntry(master=root,textvariable=v1,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
entre_nom.place(x=180,y=130,width=160)

lblprenom = Label(root, text="Prénom", font=("sans serif", 14), background='#60554F', foreground='#FFFFFF')
lblprenom.place(x=10, y=190, width=80)
v2=StringVar()
entre_prenom=customtkinter.CTkEntry(master=root,textvariable=v2,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
entre_prenom.place(x=180,y=190,width=160)

lblnumero = Label(root, text="Téléphone", font=("sans serif", 14), background='#60554F', foreground='#FFFFFF')
lblnumero.place(x=10, y=250, width=80)
v3=StringVar()
entre_numero=customtkinter.CTkEntry(master=root,textvariable=v3,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
entre_numero.place(x=180,y=250,width=160)

lblrole = Label(root, text="Rôle", font=("sans serif", 14), background='#60554F', foreground='#FFFFFF')
lblrole.place(x=10, y=310, width=60)
v10=customtkinter.StringVar(value="Gérant")
entre_role=customtkinter.CTkComboBox(master=root,values=("Gérant","Responsable"),variable=v10,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
entre_role.place(x=180,y=310,width=160)

lblemail = Label(root, text="Email", font=("sans serif", 14), background='#60554F', foreground='#FFFFFF')
lblemail.place(x=10, y=370, width=80)
v5=StringVar()
entre_email=customtkinter.CTkEntry(master=root,textvariable=v5,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
entre_email.place(x=180,y=370,width=160)

lbldmdp = Label(root, text="Mot de passe", font=("sans serif", 14), background='#60554F', foreground='#FFFFFF')
lbldmdp.place(x=0, y=430, width=160)
v6=StringVar()
entre_motdepasse=customtkinter.CTkEntry(master=root,textvariable=v6,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
entre_motdepasse.place(x=180,y=430,width=160)

lblcon_mdp = Label(root, text="Confirmation", font=("sans serif", 14), background='#60554F', foreground='#FFFFFF')
lblcon_mdp.place(x=0, y=490, width=160)
v7=StringVar()
entre_confirmation=customtkinter.CTkEntry(master=root,textvariable=v7,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
entre_confirmation.place(x=180,y=490,width=160)

v8=customtkinter.StringVar(value="nom")
type_rechercher=customtkinter.CTkComboBox(master=root,values=("nom","prenom","telephone","role","email"),variable=v8,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
type_rechercher.place(x=10,y=570,width=160)


v9=StringVar()
txtrechercher=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtrechercher.place(x=180,y=570,width=160)

tableAfficher = ttk.Treeview(root, columns=(1, 2, 3, 4, 5), height=10, show="headings")
tableAfficher.place(x=400, y=130, width=900, height=600)
style = ttk.Style(root)
style.configure("Treeview",background="#D9D9D9")

#frame=customtkinter.CTkFrame(master=root,width=800,corner_radius=20,fg_color="#4B4745",border_color="#FFFFFF",border_width=2,height=400)


# Entete
tableAfficher.heading(1, text="nom")
tableAfficher.heading(2, text="Prenom")
tableAfficher.heading(3, text="numero")
tableAfficher.heading(4, text="role")
tableAfficher.heading(5, text="email")

# definir les dimentions des colonnes
tableAfficher.column(1, width=10)
tableAfficher.column(2, width=40)
tableAfficher.column(3, width=40)
tableAfficher.column(4, width=40)
tableAfficher.column(5, width=40)
#tableAfficher.selection_get()

def afficher():
    conn=pymysql.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')
    cur=conn.cursor()
    cur.execute("select nom,prenom,telephone,role,email from utilisateur;")
    tableAfficher.delete(*tableAfficher.get_children())
    output=cur.fetchall()
    for i in output:
        tableAfficher.insert('',END,values=i)
    conn.close()

def callback(event):
    ligne_id = tableAfficher.selection()[0]
    selection=tableAfficher.set(ligne_id)
    if selection:
        entre_nom.delete(0, END)
        entre_prenom.delete(0, END)
        entre_numero.delete(0, END)
        entre_email.delete(0,END)
       
        entre_nom.insert(0,selection['1'])
        entre_prenom.insert(0,selection['2'])
        entre_numero.insert(0,selection['3'])
        entre_role.set(selection['4'])
        entre_email.insert(0,selection['5'])
        print(selection)
    else:
        print('nnnn')
tableAfficher.bind("<Double-Button>",callback)

def enregistrer():
    try:
        if entre_nom.get()=="" or entre_prenom.get()=="" or entre_numero.get()=="" or entre_role.get()=="" or entre_email.get()=="" or entre_motdepasse.get()=="" or entre_confirmation.get()=="":
            messagebox.showinfo("Echec","Tous les champs sont réquis") 
        elif entre_motdepasse.get()!=entre_confirmation.get(): 
          messagebox.showinfo("Echec","Mot de passe incohérent")
        else:
         conn=pymysql.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')
         nom=entre_nom.get()
         prenom=entre_prenom.get()
         telephhone=entre_numero.get()
         role=entre_role.get()
         email=entre_email.get()
         mdp=entre_motdepasse.get()
         print(nom,prenom,telephhone,role,email,mdp)
         cur=conn.cursor()
         cur.execute("insert into utilisateur (nom,prenom,telephone,role,email,mot_de_passe) values (%s,%s,%s,%s,%s,%s);",(nom,entre_prenom.get(),entre_numero.get(),entre_role.get(),entre_email.get(),entre_motdepasse.get()))
         conn.commit()
         messagebox.showinfo("Success","Utilisateur enregistré")
         afficher()
    except Exception as e:
        messagebox.showwarning('Attention','Cet email ou numéro de téléphone éxiste')
        conn.rollback()
        conn.close()
        
def modifier():

    
    nom=str(entre_nom.get())
    prenom=str(entre_prenom.get())
    telephhone=str(entre_numero.get())
    role=str(entre_role.get())
    email=str(entre_email.get())
    
    try:
        conn=pymysql.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')
        
       
        cur=conn.cursor()
        cur.execute("update utilisateur set nom=%s,prenom=%s,role=%s,telephone=%s where email=%s;",(nom,prenom,role,telephhone,email))
        conn.commit()
        dernier=cur.lastrowid
        messagebox.showinfo("Success","Utilisateur modifié")
        afficher()
    except Exception as e:
        messagebox.showwarning("Attention","Ce numero de téléphone")
        conn.rollback()
        conn.close()

def supprimer():

    email=str(entre_email.get())
    if email=="":
        messagebox.showwarning("Attention","spécifier l'email s'il vous plaît")
    else:

         try:
            conn=pymysql.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')
              
            cur=conn.cursor()
            cur.execute("delete from utilisateur where email=%s;",email)
            conn.commit()
            dernier=cur.lastrowid
            messagebox.showinfo("Information","Utilisateur supprimé")
            afficher()
         except Exception as e:
             messagebox.showwarning("Attention","spécifier l'email s'il vous plaît")
             conn.rollback()
             conn.close()

def rechercher():
    
    conn=pymysql.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')
    cur=conn.cursor()
    cur.execute("select nom,prenom,telephone,role,email from utilisateur where "+str(type_rechercher.get())+" LIKE '%"+str(txtrechercher.get())+"%' ;")
    tableAfficher.delete(*tableAfficher.get_children())
    output=cur.fetchall()
    print(output,type_rechercher.get())
    for i in output:
        tableAfficher.insert('',END,values=i)
    conn.close()


buttEnregistrer= customtkinter.CTkButton(master=root,text="Enregistrer",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF",command=enregistrer)
buttEnregistrer.place(x=10,y=670,width=100)


buttmodifier= customtkinter.CTkButton(master=root,text="Modifier",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF",command=modifier)
buttmodifier.place(x=125,y=670,width=100)


buttonsupp= customtkinter.CTkButton(master=root,text="Supprimer",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF",command=supprimer)
buttonsupp.place(x=240,y=670,width=100)

buttrechercher= customtkinter.CTkButton(master=root,text="Rechercher",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF",command=rechercher)
buttrechercher.place(x=210,y=620,width=130)

buttrafficher= customtkinter.CTkButton(master=root,text="Afficher tous",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF",command=afficher)
buttrafficher.place(x=10,y=620,width=130)



        
afficher()

root.state('zoomed')
root.mainloop()