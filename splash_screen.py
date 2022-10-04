from tkinter import *
import customtkinter

fenetre=Tk()
fenetre.geometry('200x200')
Label(fenetre,text="ALOOOOO",font=18).pack()

def main():
    fenetre.destroy()
    root=Tk()
    root.geometry('400x400')
   

    def show():
       p = password.get() #get password from entry
       print(p)


    app = Tk()   
    password = StringVar() #Password variable
    passEntry = Entry(root, textvariable=password, show='*').pack() 
    submit = Button(root, text='Show Console',command=show).pack()      
    app.mainloop() 

fenetre.after(4000,main)
fenetre.mainloop()