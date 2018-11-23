from tkinter import*
from tkinter import messagebox
import random
glowneOkno=Tk()

def zapis():
    zawartosc=str(Pole3.get())
    plik_tekstowy = open ("zapis.txt","a")
    plik_tekstowy.write(zawartosc)
    plik_tekstowy.close()
def akcjaAutor ():
    messagebox.showinfo ( "Autor" , "Autorem kalkulatora jest \nJakub Piotr Grochowski" )
pasekMenu = Menu (glowneOkno)
pierwszeMenu = Menu (pasekMenu, tearoff=0)
pierwszeMenu.add_command (label="Wyjdz", command = glowneOkno.quit)
pierwszeMenu.add_command (label="Zapis", command = zapis)
pasekMenu.add_cascade (label="File", menu=pierwszeMenu)
pomocMenu = Menu (pasekMenu , tearoff =0)
pomocMenu.add_command (label = "O Autorze ", command = akcjaAutor )
pasekMenu.add_cascade (label = "Autor", menu = pomocMenu )
wartosc = IntVar()

def przyciski1():
    if wartosc.get()==1:
        wynik=int(Pole1.get())+int(Pole2.get())
        messagebox.showinfo("Wynik",wynik)
    if wartosc.get()==2:
        wynik=int(Pole1.get())-int(Pole2.get())
        messagebox.showinfo("Wynik",wynik)
    if wartosc.get()==3:
        wynik=int(Pole1.get())*int(Pole2.get())
        messagebox.showinfo("Wynik",wynik)
    if wartosc.get()==4:
        wynik=int(Pole1.get())/int(Pole2.get())
        messagebox.showinfo("Wynik",wynik)
    if wartosc.get()==0:
        messagebox.showinfo("Czyszczenie...","Wyczyszczono :D")
    if wartosc.get()==5:
        kostka = random.randint (1,100)
        messagebox.showinfo("losowanie",kostka)

def przyciski2():
    messagebox.showinfo("Wynik",Pole1.get())
    pierwsza=Pole1.get()
oPT1=Label(glowneOkno,text="Podaj pierwszą liczbę")
oPT1.grid(row=0,column=0)
Pole1=Entry(glowneOkno)
Pole1.grid(row=1,column=0)
def przyciski3():
    messagebox.showinfo("Wynik",Pole2.get())
    druga=Pole2.get()
oPT2=Label(glowneOkno,text="Podaj drugą liczbę")
oPT2.grid(row=0,column=1)
Pole2=Entry(glowneOkno)
Pole2.grid(row=1,column=1)
def przyciski4():
    messagebox.showinfo("Wynik",Pole3.get())
    druga=Pole3.get()
oPT3=Label(glowneOkno,text="Notatnik")
oPT3.grid(row=9,column=1)
Pole3=Entry(glowneOkno)
Pole3.grid(row=10,column=1)

rprzycisk1=Radiobutton(glowneOkno,text="Wybor1(+)",variable=wartosc,value=1,bg="blue",fg="white")
rprzycisk1.grid(row=2,column=0)
rprzycisk2=Radiobutton(glowneOkno,text="Wybor2(-)",variable=wartosc,value=2,bg="blue",fg="white")
rprzycisk2.grid(row=3,column=0)
rprzycisk3=Radiobutton(glowneOkno,text="Wybor3(*)",variable=wartosc,value=3,bg="blue",fg="white")
rprzycisk3.grid(row=4,column=0)
rprzycisk4=Radiobutton(glowneOkno,text="Wybor4(/)",variable=wartosc,value=4,bg="blue",fg="white")
rprzycisk4.grid(row=5,column=0)
rprzycisk4=Radiobutton(glowneOkno,text="Clear(C)",variable=wartosc,value=0,bg="red")
rprzycisk4.grid(row=3,column=2)
przycisk = Button(glowneOkno,text="Oblicz",command=przyciski1,bg="green")
przycisk.grid(row=6,column=1)
rprzycisk5=Radiobutton(glowneOkno,text="Losuj",variable=wartosc,value=5,bg="black",fg="red")
rprzycisk5.grid(row=7,column=1)

# zapis=Radiobutton(glowneOkno,text="Zapis",wariable=wartosc,value=5,bg="black",fg="white")
# zapis.grid(row=10,column=2)

glowneOkno.title("Kalkulator")
glowneOkno.geometry("400x400")
glowneOkno . config ( menu = pasekMenu )
glowneOkno.mainloop()
