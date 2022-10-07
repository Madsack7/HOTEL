from ast import mod
from doctest import master
from pydoc import text
from re import I
from signal import default_int_handler
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import  customtkinter
from subprocess import call
import pymysql
splash_fenetre=Tk()
splash_fenetre.geometry('800x600')
splash_fenetre.configure(background="#4B4745",borderwidth=2)
splash_fenetre.overrideredirect(1)
splash_fenetre.attributes("-toolwindow",1)

scn_width=splash_fenetre.winfo_screenwidth()
scn_height=splash_fenetre.winfo_screenheight()
fn_width=800
fn_height=600
x_cor=int((scn_width /2) - (fn_width/2))
y_cor=int((scn_height /2) - (fn_height/2))
splash_fenetre.geometry("{}x{}+{}+{}".format(fn_width,fn_height,x_cor,y_cor))
print(x_cor)
print(y_cor)
print(scn_width)
print(scn_height)
img=ImageTk.PhotoImage(Image.open("image\imgsplash.png"))
splash_cadre=customtkinter.CTkFrame(splash_fenetre,width=700,height=400,bg_color="#4B4745",corner_radius=20,border_color="#ffffff",border_width=2)
x=customtkinter.CTkLabel(splash_cadre,image=img,bg_color="#ffffff",width=688,height=388,corner_radius=20)
x.pack(expand=YES)
splash_cadre.pack_propagate(False)
splash_cadre.pack(expand=YES)
#
index=0
def main():
    splash_fenetre.destroy()
    fenetre = Tk()
    fenetre.title("AW KA HÔTEL")
    fenetre.geometry("800x700+0+0")
    fenetre.configure(background="#4B4745")
    fenetre.iconbitmap("image\icone_logo.ico")
    #imag=ImageTk.PhotoImage(Image.open("image\images (5).png"))
    #x=Label(image=imag,font=("Arial",30))
    #x.pack()
    frame=customtkinter.CTkFrame(master=fenetre,width=800,corner_radius=20,fg_color="#4B4745",border_color="#FFFFFF",border_width=2,height=400)
    frame.grid(row=0, column=0, columnspan=2, rowspan=4, pady=200, padx=240, sticky="nsew")
    label=customtkinter.CTkLabel(master=frame,text="CONNEXION",corner_radius=20,width=700,height=40,fg_color="#4B4745",text_color="#FFFFFF",text_font=("Inter",25))
    label.place(y=20,x=90)
    
    

    show_face='😃'
    hide_face='😑'

    """def show():
       
        if entry_mdp.cget('show')=='*':
            entry_mdp.config(show='')
            show_hide_button.config(text=show_face)
        else:
            entry_mdp.config(show='')
            show_hide_button.config(text=hide_face)"""

    label_email=customtkinter.CTkLabel(master=frame,text="Email",corner_radius=20,width=100,height=40,fg_color="#4B4745",text_color="#FFFFFF",text_font=("Inter",18))
    label_email.place(y=100,x=50)
    
    label_info=customtkinter.CTkLabel(master=frame,text="l",corner_radius=20,width=100,height=40,fg_color="#4B4745",text_color="#FFFFFF",text_font=("Inter",18))
    label_info.place(x=420,y=630)
    vf=StringVar()
    #label_info=Label(fenetre,text=l[index],textvariable=vf,bg="#FFFFFF",width=50,font="Inter, 12").place(x=420,y=630)
    
    label_mdp=customtkinter.CTkLabel(master=frame,text="Mot de passe",corner_radius=20,width=100,height=40,fg_color="#4B4745",text_color="#FFFFFF",text_font=("Inter",18))
    label_mdp.place(y=200,x=50)
    v1=StringVar()
    entry_email=customtkinter.CTkEntry(master=frame,corner_radius=20,text=v1,width=300,height=40,fg_color="#FFFFFF",text_color="#4B4745",text_font=("Inter",15))
    entry_email.place(y=100,x=300)
 
    v2=StringVar()
    entry_mdp=customtkinter.CTkEntry(master=frame,corner_radius=20,text=v2,width=300,height=40,fg_color="#FFFFFF",text_color="#4B4745",text_font=("Inter",15),show='*')
    entry_mdp.place(y=200,x=300)
    
    #btn=Button(frame,text=hide_face,width=10).place(y=200,x=660)
    #show_hide_button=customtkinter.CTkButton(frame,text=hide_face,fg_color="#FFFFFF",text_font=('Bold',15),width=15,command=show)
    #show_hide_button.place(y=200,x=660)
    def connecter():
        
          mdp=entry_mdp.get()
          nb=mdp.__len__()
          if entry_email.get()=="" or entry_mdp.get()=="":
               messagebox.showinfo("Echec","Tous les champs sont réquis")
          elif nb<8:
             messagebox.showinfo("Echec","le nombre de caractère mot de passe  doit être supérieure ou égal à 8")
          else:
             conn=pymysql.connect(
                 host='localhost',
                 user='root',
                 password ='',
                 db='hotel'
             )
             cur=conn.cursor()
             cur.execute("select email,mot_de_passe,role from utilisateur where email='"+entry_email.get()+"' and mot_de_passe='"+entry_mdp.get()+"';")
             output=cur.fetchone()
             print(output)
             if output==None:
                 messagebox.showerror('Echec','Email ou Mot de passe incorrect')
                 entry_email.delete(0,END)
                 entry_mdp.delete(0,END)
             else:
                 if output[2]=="Admin":
                      fenetre.destroy()
                      call(["python","dashboard_admin.py"])
                 elif output[2]=="Gérant":
                     fenetre.destroy()
                     call(["python","dashboard.py"])
                 else:
                     fenetre.destroy()
                     call(["python","dashboard_responsable.py"])

             """for i in output:

                 if i[0]==entry_email.get() and i[1]==entry_mdp.get():
                      fenetre.destroy()
                      call(["python","dashboard_admin.py"])
                        
                 elif i[0]==entry_email.get() and i[1]==entry_mdp.get() and i[2]=="Gérant" :
                      fenetre.destroy()
                      call(["python","dashboard.py"])
                          

                 elif i[0]==entry_email.get() and i[1]==entry_mdp.get() and  i[2]=="Responsable":
                      fenetre.destroy()
                      call(["python","dashboard.py"])
                 else:
                      messagebox.showerror('Echec','Email ou Mot de passe incorrect')"""
                         
                              
                 
             conn.close()



    Button_connecter = customtkinter.CTkButton(master= frame,text= "Connectez-vous",text_font="none 12",text_color="white",hover= True,
    hover_color= "black",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=20,
    border_color= "#d3d3d3",
    fg_color= "#827F7D",command=connecter)
    Button_connecter.place(x=380,y=300)
    
    

    
    l=["Bienvenue sur l'application AW KA HÔTEL"," "," "," "," ","S","Si"]
    def animation():
        global index
        label_info.set_text(l[0])
        index += 1
        fenetre.after(500,animation)

    

    fenetre.after(1000,animation)
    """a=customtkinter.CTkFrame(fenetre,bg_color="#ffffff",width=800,height=400,corner_radius=20,border_color="#ffffff",border_width=3)
    cadre=customtkinter.CTkFrame(fenetre,bg_color="#60554F")
    s=Label(a,text="CONNEXION", font=("Arial", 20), width=38, height=1, fg="#FFFFFF",bg="#4B4745")
    s.place(x=120,y=20)



    email = Label(a, text="EMAIL ", font=("Arial", 20), width=6, height=1,  fg="#FFFFFF",bg="#4B4745")
    #Nom.grid(row=0, column=0)
    email.place(x=1,y=100)

    #entre1= Entry(a, font=("Arial", 20), bg="#9E9696", fg="black", width=20)
    # entre1.place(x=300,y=110)
    v1=StringVar()
    entre1=customtkinter.CTkEntry(master=fenetre,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF",textvariable=v1)
    entre1.place(x=550,y=300, width=300)

    mot_passe=Label(a, text="MOT DE PASSE ", font=("Arial", 20), width=13, height=2,  fg="#FFFFFF",bg="#4B8589")
    mot_passe.place(x=4,y=150 )
    v2=StringVar()
    entre2=customtkinter.CTkEntry(master=fenetre,textvariable=v2, height=30,width=40,bg= "#4B8589",border_width=1,corner_radius=20,fg_color="#FFFFFF")
    entre2.place(x=550,y=370, width=300)

    #entre2= Entry(a, font=("Arial", 20), bg="#9E9696", fg="black", width=20)
    #entre2.place(x=300,y=170)

    
#bouton=#Button=Button(a,text="se connecter",font=("Arial", 15), width=17, height=1,  fg="white",bg="#5C4D4D")
#bouton.#place(x=200,y=300)
    button= customtkinter.CTkButton(master=fenetre,text="se connecter",height=30,width=40,border_width=2,corner_radius=20,fg_color="#FFFFFF",command=connecter)
    button.place(x=650,y=450)
#b4 = Button(text='<-',font=("Arial",16),background='#5C4D4D',width=5)
#b4.place(x=0, y=0)


    a.pack_propagate(False)
    a.pack(expand=YES)
    a.pack()
    a.place(x=260,y=200)"""

    fenetre.state('zoomed')

    fenetre.mainloop()

progress_label=customtkinter.CTkLabel(master=splash_fenetre,text="Veuillez patienter...",text_color="#FFFFFF",fg_color="#4B4745",width=140, height=28).place(x=338,y=520)
progressbar = customtkinter.CTkProgressBar(master=splash_fenetre,orient='horizontal',mode="determinate",determinate_speed=1,fg_color="#827F7D",progress_color="#FFFFFF")
progressbar.place(x=300,y=550)
i=0

def progress():
    
   global i
   if i<=10:
       
       progressbar.after(1000,progress)
       progressbar.set(0.1*i)
       #progressbar['value']=10*i
       i+=1


progress()

splash_fenetre.after(10000,main)
splash_fenetre.mainloop()



