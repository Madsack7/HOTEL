from tkinter import *
from tkinter import messagebox
from tkinter import ttk,Entry
import  customtkinter
from tkcalendar import *
import pymysql
from subprocess import call

root = Tk()
root.title("Aw KA HOTEL")
root.geometry("1000x650")
root.iconbitmap("image\icone_logo.ico")
root.attributes("-toolwindow",1)
#root.resizable(False, False)
root.configure(background='#4B4745')

def listesalle():
    conn=pymysql.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')
    cur=conn.cursor()
    cur.execute("select num_salle,categorie_salle from salle;")
    l=[]
    output=cur.fetchall()
    for i in output:
        a=str(i[0])+" "+i[1]
        l.append(a)
    conn.close()
    return l

def listeclient():
    conn=pymysql.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')
    cur=conn.cursor()
    cur.execute("select nom,prenom,telephone from client;")
    l=[]
    output=cur.fetchall()
    for i in output:
        a=str(i[0])+" "+i[1]+" "+i[2]
        l.append(a)
    conn.close()
    return l



def callback(event):
    ligne_id = tableAfficher.selection()[0]
    selection=tableAfficher.set(ligne_id)
    if selection:
        conn1=pymysql.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')
               
        cur1=conn1.cursor()
        cur1.execute("select nom,prenom,telephone from client where telephone='"+selection['5']+"';")
        l1=[]
        output1=cur1.fetchall()
        for i in output1:
         a=str(i[0])+" "+i[1]+" "+i[2]
         l1.append(a)
         txtclient.set(a)
        conn1.close()
        
        conn=pymysql.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')
        cur=conn.cursor()
        cur.execute("select num_salle,categorie_salle from salle where num_salle="+selection['2']+";")
        l=[]
        output=cur.fetchall()
        for i in output:
          a=str(i[0])+" "+i[1]
          l.append(a)
          txtsalle.set(a)
        conn.close()

        date_.set(selection['6'])
        txtdprix.delete(0,END)
        txtdprix.insert(0,selection['7'])
        id_rec.insert(0,selection['1'])
        print(selection)
    else:
        print('nnnn')



lbltitre = customtkinter.CTkLabel(master=root,text="Bienvenue sur la page des reservations",text_font=("sans serif",20),height=30,fg_color="white",width=40,border=1,corner_radius=20,bg_color="#D9D9D9")
lbltitre.place(x=0, y=0, width=1280)

lblsalle = Label(root, text="Salle", font=("sans serif", 12), background='#60554F', foreground='#FFFFFF')
lblsalle.place(x=30, y=130, width=80)
txtsalle=customtkinter.CTkComboBox(master=root,height=30,values=listesalle(),width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtsalle.place(x=200,y=130,width=160)

lblclient = Label(root, text="Client", font=("sans serif", 12), background='#60554F', foreground='#FFFFFF')
lblclient.place(x=40, y=190, width=60)
txtclient=customtkinter.CTkComboBox(master=root,height=30,values=listeclient(),width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtclient.place(x=200,y=190,width=160)

lbldate = Label(root, text="Date_reservation", font=("sans serif", 12), background='#60554F', foreground='#FFFFFF')
lbldate.place(x=0, y=250, width=210)
#txtdate=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
#txtdate.place(x=200,y=250,width=160)
date_=StringVar()
date1=DateEntry(root,height=60,textvariable=date_,date_pattern='yyyy-MM-dd',width=40,border_width=1,font=("Inter",15),corner_radius=20,fg_color="#FFFFFF").place(x=200,y=250,width=160)

id_rec=Entry(root,width=100)

lblprix = Label(root, text="Prix", font=("sans serif", 12), background='#60554F', foreground='#FFFFFF')
lblprix.place(x=30, y=300, width=80)
txtdprix=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtdprix.place(x=200,y=300,width=160)

v8=customtkinter.StringVar(value="nom_client")
type_rechercher=customtkinter.CTkComboBox(master=root,values=("nom_client","prenom_client","telephone","date_reservation","prix"),variable=v8,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
type_rechercher.place(x=10,y=450,width=160)





listesalle()
listeclient()

def enregistrer():
    salle_=txtsalle.get().split(' ',-1)
    num_salle=int(salle_[0])
    client_=txtclient.get()
    info=client_.split(' ',-1)
    client_nom=info[0]
    client_prenom=info[1]
    client_telephone=info[2]
    date=date_.get()
    prix=txtdprix.get()
    print(num_salle,client_nom,client_prenom,client_telephone,date,prix)
    try:
        if prix=="":
            messagebox.showwarning("Attention","Veuillez donner le prix ")
        else:
         conn=pymysql.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')
         cur=conn.cursor()
         cur.execute("insert into reservation_salle (num_salle,nom_client,prenom_client,telephone,date_reservation,prix) values (%s,%s,%s,%s,%s,%s);",(num_salle,client_nom,client_prenom,client_telephone,date,prix))
         conn.commit()
         messagebox.showinfo("Success","Salle reservé")
         afficher()

    except Exception as e:
        messagebox.showerror("Echec","erreur")
        conn.rollback()
        conn.close()

def modifier():

    salle_=txtsalle.get().split(' ',-1)
    num_salle=int(salle_[0])
    client_=txtclient.get()
    info=client_.split(' ',-1)
    client_nom=info[0]
    client_prenom=info[1]
    client_telephone=info[2]
    date=date_.get()
    prix=txtdprix.get()
    
    id=int(id_rec.get())
    id_rec.delete(0,END)
    print(id)
    try:
        conn=pymysql.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')
        cur=conn.cursor()
        cur.execute("update reservation_salle set num_salle=%s, nom_client=%s,prenom_client=%s,telephone=%s,date_reservation=%s,prix=%s where id=%s;",(num_salle,client_nom,client_prenom,client_telephone,date,prix,id))
        conn.commit()
        dernier=cur.lastrowid
        messagebox.showinfo("Success","Réservation modifié") 
        afficher()
    except Exception as e:
        messagebox.showwarning("Attention","Ce numero de téléphone")
        conn.rollback()
        conn.close()   

def supprimer():

    
    if id_rec.get()=="":
        messagebox.showwarning("Attention","Veuillez selectionner un élément")
    else:
        id=int(id_rec.get())
        id_rec.delete(0,END)

        try:
            conn=pymysql.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')
              
            cur=conn.cursor()
            cur.execute("delete from reservation_salle where id=%s;",id)
            conn.commit()
            dernier=cur.lastrowid
            messagebox.showinfo("Information","Reservation supprimé")
            afficher()
        except Exception as e:
             messagebox.showwarning("Attention",e)
             conn.rollback()
             conn.close()

def rechercher():
    
    conn=pymysql.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')

    cur=conn.cursor()
    cur.execute("select id,num_salle,nom_client,prenom_client,telephone,date_reservation,prix from reservation_salle where "+str(type_rechercher.get())+" LIKE '%"+str(txtrechercher.get())+"%' ;")
    tableAfficher.delete(*tableAfficher.get_children())
    output=cur.fetchall()
    print(output,type_rechercher.get())
    for i in output:
        tableAfficher.insert('',END,values=i)
    conn.close()

buttrechercher= customtkinter.CTkButton(master=root,text="Rechercher",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF",command=rechercher)
buttrechercher.place(x=225,y=500,width=110)

txtrechercher=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtrechercher.place(x=200,y=450,width=160)

buttEnregistrer= customtkinter.CTkButton(master=root,text="Enregistrer",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF",command=enregistrer)
buttEnregistrer.place(x=10,y=560,width=100)


buttmodifier= customtkinter.CTkButton(master=root,text="Modifier",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF",command=modifier)
buttmodifier.place(x=115,y=560,width=100)

def salle():
    root.destroy()
    call(["python", "salle.py"])
     
b4 = Button(text='<-',font=("Arial",16),background='#FFFFFF',width=5,command=salle)
b4.place(x=0, y=30)


buttonsupp= customtkinter.CTkButton(master=root,text="Supprimer",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF",command=supprimer)
buttonsupp.place(x=220,y=560,width=100)

tableAfficher = ttk.Treeview(root, columns=(1, 2, 3, 4 ,5,6,7), height=10, show="headings")
tableAfficher.place(x=400, y=130, width=880, height=600)
style = ttk.Style(root)
style.configure("Treeview",background="#D9D9D9")
# Entete
tableAfficher.heading(1, text="ID")
tableAfficher.heading(2, text="Num_salle")
tableAfficher.heading(3, text="Nom_client")
tableAfficher.heading(4, text="Prénom_client")
tableAfficher.heading(5, text="Téléphone_client")
tableAfficher.heading(6, text="Date_reservation")
tableAfficher.heading(7, text="Prix")
# definir les dimentions des colonnes
tableAfficher.column(1, width=10)
tableAfficher.column(2, width=40)
tableAfficher.column(3, width=40)
tableAfficher.column(4, width=40)
tableAfficher.column(5, width=40)
tableAfficher.column(6, width=40)
tableAfficher.column(7, width=40)

tableAfficher.bind("<Double-Button>",callback)

def afficher():
    conn=pymysql.connect(
              host='localhost',
              user='root',
              password="",
              db='hotel')
    cur=conn.cursor()
    cur.execute("select id,num_salle,nom_client,prenom_client,telephone,date_reservation,prix from reservation_salle;")
    tableAfficher.delete(*tableAfficher.get_children())
    output=cur.fetchall()
    for i in output:
        tableAfficher.insert('',END,values=i)
    conn.close()


afficher()
root.state('zoomed')

root.mainloop()