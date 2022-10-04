
from doctest import master
from tkinter import *
import tkinter.ttk as ttk
from turtle import width
from PIL import ImageTk, Image
import mysql.connector  
from subprocess import call
from tkinter import ttk,Entry
import customtkinter



fenetre=Tk()
fenetre.title("Hotel")
fenetre.geometry("1280x720")
fenetre.minsize(480,320)
fenetre.config(background='#4B4745')

frame5=customtkinter.CTkFrame(master=fenetre,width=1270,height=100,corner_radius=10,fg_color="#FFFFFF")
frame5.place(x=5,y=3)

label1=customtkinter.CTkLabel(master=frame5,text='AW KA HÔTEL',text_color="#4B4745",text_font=("Inter",40),width=1270,height=90).pack(expand=YES)
frame=customtkinter.CTkFrame(master=fenetre,width=1270,height=70,corner_radius=10,fg_color="#827F7D")
frame.place(x=5,y=100)
#fenetre.attributes('-alpha',0.7)
#fenetre.iconbitmap("IKA_HOTEL.ico")



"""can=Canvas(fenetre,width=1280,height=740)
img=PhotoImage(file="image\image_back2.png")
can.create_image(637,350,image=img)
can.place(x=0,y=0)
photo1 = PhotoImage(file = "image\employe.png") 
photo2 = PhotoImage(file = "image\chambre (4).png")
photo3 = PhotoImage(file = "image\client.png")
photo4 = PhotoImage(file = "image\salle.png")
photo5 = PhotoImage(file = "image\\restaurant.png")


#cadre=Frame(fenetre,bg='#C6C2C2',bd=1,relief=SUNKEN,height=515,width=350)
#cadre.place(x=250,y=200)

# Ajouter l'image dans le bouton 
#Button(gui, image=photo).pack(side=TOP) 
def slide(x):
    fenetre.attributes('-alpha',my_slider.get())
    


my_slider=ttk.Scale(cadre,from_=0.1,to=1.0,value=0.7,orient=HORIZONTAL,command=slide)
my_slider.pack(pady=60)."""

def employer():
    call(["python","Employe.py"])

def utilisateur():
    call(["python", "Utilisateurs.py"])




def chambre():
    call(["python","chambre.py"])
    
    
    
def client():
    call(["python","Client.py"])
    
    
    
def salle_():
    call(["python","Salle.py"])
    
    
    
def restaurant():
    call(["python","Restaurant.py"])

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hotel"
)

def totalchambre():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hotel"
    )
    mycursor = mydb.cursor()


    query = "SELECT COUNT(num_chambre) AS Total FROM chambre ;"
    mycursor.execute(query)

    myresult = mycursor.fetchall()

    print(myresult[-1][-1])
    return str(myresult[-1][-1])


mydb.close()

def totalclient():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hotel"
    )
    mycursor = mydb.cursor()


    query = "SELECT COUNT(telephone) AS Total FROM client ;"
    mycursor.execute(query)

    myresult = mycursor.fetchall()

    print(myresult[-1][-1])
    return str(myresult[-1][-1])


mydb.close()


def totalemployé():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hotel"
    )
    mycursor = mydb.cursor()


    query = "SELECT COUNT(telephone) AS Total FROM employe ;"
    mycursor.execute(query)

    myresult = mycursor.fetchall()

    print(myresult[-1][-1])
    return str(myresult[-1][-1])


mydb.close()


def totalsalle():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hotel"
    )
    mycursor = mydb.cursor()


    query = "SELECT COUNT(num_salle) AS Total FROM salle ;"
    mycursor.execute(query)

    myresult = mycursor.fetchall()

    print(myresult[-1][-1])
    return str(myresult[-1][-1])


mydb.close()
    
    
#b1 =Button(fenetre,image=photo1, text="",background='#FFFFFF',font=("Inria Sans",30),fg="#000000",width=153).place(x=0,y=1)

b1= customtkinter.CTkButton(master=frame,hover_color="#302D2B",text="Employé",text_font=("Inter",25),text_color="#FFFFFF",fg_color="#827F7D",border_width=1,border_color="#827F7D",corner_radius=20,width=200,height=80,command=employer).place(x=0,y=3)
#buttEnregistrer.place(x=10,y=560,width=100)
b2 =customtkinter.CTkButton(master=frame,hover_color="#302D2B", text="Salle",text_font=("Inter",25),text_color="#FFFFFF",fg_color="#827F7D",border_width=1,border_color="#827F7D",corner_radius=20,width=200,height=80,command=salle_).place(x=210,y=3)

b3 =customtkinter.CTkButton(master=frame,hover_color="#302D2B", text="Client",text_font=("Inter",25),text_color="#FFFFFF",fg_color="#827F7D",border_width=1,border_color="#827F7D",corner_radius=20,width=200,height=80,command=client).place(x=430,y=3)

b4=customtkinter.CTkButton(master=frame,hover_color="#302D2B", text="Restaurant",text_font=("Inter",25),text_color="#FFFFFF",fg_color="#827F7D",border_width=1,border_color="#827F7D",corner_radius=20,width=200,height=80,command=restaurant).place(x=650,y=3)

b5 =customtkinter.CTkButton(master=frame,hover_color="#302D2B",text="Chambre",text_font=("Inter",25),text_color="#FFFFFF",fg_color="#827F7D",border_width=1,border_color="#827F7D",corner_radius=20,width=200,height=80,command=chambre).place(x=870,y=3)

b6 =customtkinter.CTkButton(master=frame,hover_color="#302D2B",text="Utilisateur",text_font=("Inter",25),text_color="#FFFFFF",fg_color="#827F7D",border_width=1,border_color="#827F7D",corner_radius=20,width=200,height=80,command=utilisateur).place(x=1080,y=3)

label=customtkinter.CTkLabel(master=fenetre,text="Statistiques",corner_radius=20,fg_color="#4B4745",text_color="#FFFFFF",text_font=("Inter",20))
label.place(y=240,x=550)

frame1=customtkinter.CTkFrame(master=fenetre,width=900,corner_radius=20,fg_color="#4B4745",border_color="#FFFFFF",border_width=2,height=450).place(x=190,y=275)
#frame1.grid(row=0, column=0, columnspan=2, rowspan=4, pady=275, padx=190, sticky="nsew")
frame2=customtkinter.CTkFrame(master=frame1,width=430,fg_color="#827F7D",height=215,border_width=2,border_color="#302D2B",corner_radius=20).place(x=200,y=280)
label2=customtkinter.CTkLabel(master=frame2,width=350,fg_color="#827F7D",text="Total Chambres",text_color="#FFFFFF",text_font=("Jacques Francois",30)).place(x=240,y=290)
label22 = customtkinter.CTkLabel(master=frame2, width=350, fg_color="#827F7D", text=totalchambre(),
                                text_color="#FFFFFF", text_font=("Jacques Francois", 30)).place(x=240, y=360)

frame3=customtkinter.CTkFrame(master=frame1,width=430,fg_color="#827F7D",height=215,border_width=2,border_color="#302D2B",corner_radius=20).place(x=200,y=505)
label3=customtkinter.CTkLabel(master=frame3,width=350,fg_color="#827F7D",text="Total Employés",text_color="#FFFFFF",text_font=("Jacques Francois",30)).place(x=240,y=515)
label33 = customtkinter.CTkLabel(master=frame3, width=350, fg_color="#827F7D", text= totalemployé(),
                                text_color="#FFFFFF", text_font=("Jacques Francois", 30)).place(x=240, y=605)

frame4=customtkinter.CTkFrame(master=frame1,width=430,fg_color="#827F7D",height=215,border_width=2,border_color="#302D2B",corner_radius=20).place(x=650,y=280)
label4=customtkinter.CTkLabel(master=frame4,width=350,fg_color="#827F7D",text="Total Salles",text_color="#FFFFFF",text_font=("Jacques Francois",30)).place(x=690,y=290)
label44 = customtkinter.CTkLabel(master=frame4, width=350, fg_color="#827F7D", text=totalsalle(), text_color="#FFFFFF",
                                text_font=("Jacques Francois", 30)).place(x=690, y=360)

frame6=customtkinter.CTkFrame(master=frame1,width=430,fg_color="#827F7D",height=215,border_width=2,border_color="#302D2B",corner_radius=20).place(x=650,y=505)
label6=customtkinter.CTkLabel(master=frame6,width=350,fg_color="#827F7D",text="Total Clients",text_color="#FFFFFF",text_font=("Jacques Francois",30)).place(x=690,y=515)
label66 = customtkinter.CTkLabel(master=frame6, width=350, fg_color="#827F7D", text= totalclient(),
                                text_color="#FFFFFF", text_font=("Jacques Francois", 30)).place(x=690, y=600)


"""cadre=Frame(fenetre,bg='#C6C2C2',bd=1,relief=SUNKEN,height=515,width=350)

def client():
    fenetre.destroy()
    call(["python","client.py"])

def chambre():
    fenetre.destroy()
    call(["python","chambre.py"])

def employe():
    fenetre.destroy()
    call(["python","empoye.py"])

def salle():
    fenetre.destroy()
    call(["python","salle.py"])

b1 =Button(cadre, text="CLIENT",background='#5C4D4D',font=("Inria Sans",30),fg="#ffffff",width=15,command=client)
b1.place(y=1, x=2)

b2 =Button(cadre, text="CHAMBRE",background='#5C4D4D',font=("Inria Sans",30),fg="#ffffff",width=15,command=chambre)
b2.place(y=150, x=2)

b3 =Button(cadre, text="SALLE",background='#5C4D4D',font=("Inria Sans",30),fg="#ffffff",width=15,command=salle)
b3.place(y=290, x=2)

b4 =Button(cadre, text="EMPLOYE",background='#5C4D4D',font=("Inria Sans",30),fg="#ffffff",width=15,command=employe)
b4.place(y=430, x=2)

cadre1=Frame(fenetre,bg='#C6C2C2',bd=1,relief=SUNKEN,height=200,width=300)
nom=Label(cadre1,text="!!!!!!",font=('Inria Sans',50),bg='#A69D9D').pack(expand=YES)
cadre1.pack_propagate(False)
cadre1.place(x=430,y=185)

cadre2=Frame(fenetre,bg='#C6C2C2',bd=1,relief=SUNKEN,height=200,width=300)
nom=Label(cadre2,text="!!!!!!",font=('Inria Sans',50),bg='#A69D9D').pack(expand=YES)
cadre2.pack_propagate(False)
cadre2.place(x=900,y=185)

cadre3=Frame(fenetre,bg='#C6C2C2',bd=1,relief=SUNKEN,height=200,width=300)
nom=Label(cadre3,text="!!!!!!",font=('Inria Sans',50),bg='#A69D9D').pack(expand=YES)
cadre3.pack_propagate(False)
cadre3.place(x=430,y=490)

cadre4=Frame(fenetre,bg='#C6C2C2',bd=1,relief=SUNKEN,height=200,width=300)
nom=Label(cadre4,text="!!!!!!",font=('Inria Sans',50),bg='#A69D9D').pack(expand=YES)
cadre4.pack_propagate(False)
cadre4.place(x=900,y=490)

cadre5=Frame(fenetre,bg='#5C4D4D',bd=1,relief=SUNKEN,height=175,width=900)
img = ImageTk.PhotoImage(Image.open("IKA_HOTEL.ico"),size=1)
panel =Label(cadre5, image = img,width=600)
panel.pack(side = "left")


date = datetime.date.today()
print(date)
panel1 =Label(cadre5, text=date,width=425,bg='#5C4D4D',font=("Inria Sans",20),fg="#ffffff")
panel1.pack(side = "right")

cadre5.pack_propagate(False)
cadre5.place(x=1,y=1)


degiskenler=['CLIENT','CHAMBRE','SALLE','EMPLOYE']
rolechamp=Combobox(fenetre, values=degiskenler,font=("Inria Sans",20)).place(width=200,height=40,y=130,x=1000)

nom=Label(fenetre,text="Email:neka_hotel@gmail.com     Contact:+223 71195096     Adresse:ACI 2000",font=('Inria Sans',10),bg='#A69D9D').pack(side=BOTTOM)

cadre.pack_propagate(False)
cadre.place(x=1,y=180)."""

fenetre.state("zoomed")
fenetre.mainloop()