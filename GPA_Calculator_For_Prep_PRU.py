import tkinter
from tkinter import *
master = Tk()
#-------------------------------------------------------------------#
canvas = Canvas(master, height=750, width=450,bg='#004082')
canvas.pack()
#-------------------------------------------------------------------#
frame_ust=Frame(master)
frame_ust.place(relx=0.07, rely=0.1, relwidth=0.85, relheight=0.85)
#-------------------------------------------------------------------#
baslik = Label(frame_ust, text="Piri Reis Üniversitesi" , font="Verdana 18 bold")
baslik.pack()
baslik = Label(frame_ust, text="Hazırlık Bölümü" , font="Verdana 18 bold")
baslik.pack()
baslik = Label(frame_ust, text="Ortalama Hesaplama" , font="Verdana 18 bold")
baslik.pack()
#-------------------------------------------------------------------#
not1b= Label(frame_ust, text="Achivment:", font="Verdana 9 bold")
not1b.place(x=10,y=140)
not1 = tkinter.Entry(frame_ust)
not1.place(x=130,y=140)
#-------------------------------------------------------------------#
not2b= Label(frame_ust, text="Reader Quiz:", font="Verdana 9 bold")
not2b.place(x=10,y=170)
not2 = tkinter.Entry(frame_ust)
not2.place(x=130,y=170)
#-------------------------------------------------------------------#
not3b= Label(frame_ust, text="Speaking:", font="Verdana 9 bold")
not3b.place(x=10,y=200)
not3 = tkinter.Entry(frame_ust)
not3.place(x=130,y=200)
#-------------------------------------------------------------------#
not4b= Label(frame_ust, text="Writing:", font="Verdana 9 bold")
not4b.place(x=10,y=230)
not4 = tkinter.Entry(frame_ust)
not4.place(x=130,y=230)
#-------------------------------------------------------------------#
not5b= Label(frame_ust, text="Online Ödevler:", font="Verdana 9 bold")
not5b.place(x=10,y=260)
not5 = tkinter.Entry(frame_ust)
not5.place(x=130,y=260)
#-------------------------------------------------------------------#
not6b= Label(frame_ust, text="HW/P:", font="Verdana 9 bold")
not6b.place(x=10,y=290)
not6 = tkinter.Entry(frame_ust)
not6.place(x=130,y=290)
#-------------------------------------------------------------------#
not7b= Label(frame_ust, text="Writing Exit:", font="Verdana 9 bold")
not7b.place(x=10,y=320)
not7 = tkinter.Entry(frame_ust)
not7.place(x=130,y=320)
#-------------------------------------------------------------------#
not8b= Label(frame_ust, text="Speaking Exit:", font="Verdana 9 bold")
not8b.place(x=10,y=350)
not8 = tkinter.Entry(frame_ust)
not8.place(x=130,y=350)
#-------------------------------------------------------------------#
def modulici():
    c1 = float(not1.get())
    c2 = float(not2.get())
    c3 = float(not3.get())
    c4 = float(not4.get())
    c5 = float(not5.get())
    c6 = float(not6.get())

    arasinav = (c1 * 0.60)
    b2 = (c2 * 0.10)
    b3 = (c3 * 0.10)
    b4 = (c4 * 0.20)
    b5 = (c5 * 0.50)
    b6 = (c6 * 0.10)

    portfolio = (b2+b3+b4+b5+b6)*0.40

    modulici1.configure(text=str(portfolio + arasinav))
# -------------------------------------------------------------------#
def genelort():
    c1 = float(not1.get())
    c2 = float(not2.get())
    c3 = float(not3.get())
    c4 = float(not4.get())
    c5 = float(not5.get())
    c6 = float(not6.get())
    c7 = float(not7.get())
    c8 = float(not8.get())

    arasinav = (c1 * 0.60)
    b2 = (c2 * 0.10)
    b3 = (c3 * 0.10)
    b4 = (c4 * 0.20)
    b5 = (c5 * 0.50)
    b6 = (c6 * 0.10)
    exit1 = (c7 * 0.75)
    exit2 = (c8 * 0.25)

    portfolio2 = (b2+b3+b4+b5+b6)*0.40

    Modulici = (arasinav+portfolio2)

    exitsonuc = (exit1+exit2)

    ortalama.configure(text=str((Modulici + exitsonuc)/2))

#-------------------------------------------------------------------#
tus1 = tkinter.Button(frame_ust, text="Modül Ortalaması Hesapla",font="Verdana 9 bold", width=25, command=modulici)
tus1.place(x=80,y=390)
tus2 = tkinter.Button(frame_ust, text="Genel Ortalama Hesapla ",font="Verdana 9 bold", width=25, command=genelort)
tus2.place(x=80,y=470)
#-------------------------------------------------------------------#
modulici1= tkinter.Label(frame_ust, text="Modül İçi Notunuz", font="Verdana 14 bold")
modulici1.place(x=80,y=430)
ortalama= tkinter.Label(frame_ust, text="Dönem sonu Notunuz", font="Verdana 14 bold")
ortalama.place(x=80,y=500)
#-------------------------------------------------------------------#
master.mainloop()