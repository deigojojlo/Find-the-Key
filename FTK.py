from tkinter import *
from random import randint 

class Mine() :
    def __init__(self) -> None:
        self.fen = Tk()
        self.fen.title("Find the key")
        self.fen.geometry("1080x1900")
        self.fen.minsize(720,520)
        self.fen.config(background="#D2D2D2")
        self.l1 = Frame(self.fen)
        self.l2 = Frame(self.fen)
        self.l3 = Frame(self.fen)
        self.l = [self.l1,self.l2,self.l3]
        self.clavier = [["a","z","e","r","t","y","u","i","o","p"], 
             ["q","s","d","f","g","h","j","k","l","m"],
             ["w","x","c","v","b","n"]]
        self.lfin = Label(self.fen , text = "", bg = '#D2D2D2')
        self.entry = Entry(self.fen,bd = 10, relief = FLAT)
        self.restart = Button(self.fen,text = "restart", bg = "#D2D2D2", width = 10)

    def  packing(self):
        self.restart.pack(side = TOP , anchor= SE)
        self.l1.pack()
        self.l2.pack()
        self.l3.pack()
        self.entry.pack(pady = 25)
        self.lfin.pack()

    def reset(self):
        for i in range(len(self.clavier1)) :
            for k in range(len(self.clavier1[i])) :
                self.clavier1[i][k].config(bg = "#D2D2D2")
        self.start()
        self.lfin.config(text='')

    def create(self):
        for i in range(3):
            self.clavier1.append([])
            for k in range(len(self.clavier[i])) :
                self.clavier1[i].append(0)
                self.clavier1[i][k] = Label(self.l[i], text = self.clavier[i][k].upper(), bg ="#D2D2D2", font=("calibri", 15), width=10)
                self.clavier1[i][k].grid(row = i , column = k)
            
    def start(self):
        self.case = randint(1,26)
        self.essai = []
    
    def place(self,lettre) :
        for i in range(3):
            for k in range(len(self.clavier[i])) :
                if lettre == self.clavier[i][k].upper():
                    return (i,k)
            
    def get_entry(self,event):
        m = str(self.entry.get())
        self.entry.delete(0,1)
        if m not in self.essai and len(m) == 1 and m in self.clavier[0]+self.clavier[1]+self.clavier[2]:
            dix,uni = self.place(m.upper())
            if m.upper() == chr(self.case+64) :
                self.clavier1[dix][uni].config(bg = "#00FF00")
                self.lfin.config(text = "gagné")
            else :
                if m not in self.essai :
                    self.clavier1[dix][uni].config(bg = "#FF0000")
                    self.essai.append(m)
                    if len(self.essai) == 13 : 
                        self.lfin.config(text = "perdu")

    def ready(self):
        self.fen.bind('<Return>',self.get_entry)
        self.start()
        self.clavier1 = []
        self.create()
        self.restart.config(command= self.reset)
        self.packing()
        self.fen.mainloop()

game = Mine()
game.ready()
game.start()
