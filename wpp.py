from tkinter import *
import os

class Tela():

    def __init__(self, event):
        

        cab = PhotoImage(file="wpp.png")
        self.img1 = Label(janela, image=cab)
        self.img1.cab = cab
        self.img1.config(bg="black")
        self.img1.place(x=0, y=0)

        
        self.lb = Label(janela, text="Número")
        self.lb["font"] = ("Lucida, 20")
        self.lb.config(bg="black", foreground="white")
        self.lb.place(x=70, y=130)

        self.e1 = Entry(janela)
        self.e1["font"] = ("Arial,BOLD, 20")
        self.e1.config(bg="light grey", foreground="BLACK")
        self.e1.place(x=190, y=130, width=250)

        self.bt = Button(janela, text="Enviar")
        self.bt["font"] = ("Arial, 20")
        self.bt.config(bg="green", foreground="white")
        self.bt.place(x=340, y=200, width=100)
        self.bt.bind("<Button-1>", self.enviar)

        self.bt2 = Button(janela, text="Limpar")
        self.bt2["font"] = ("Arial, 20")
        self.bt2.config(bg="red", foreground="white")
        self.bt2.place(x=190, y=200, width=100)
        self.bt2.bind("<Button-1>", self.apagar)

    def enviar(self, event):


        n = self.e1.get()
        os.system("start chrome wa.me/550{}".format(n))

    def apagar(self, event):


      self.e1.delete(0, "end")
        

janela = Tk()
Tela(janela)
janela.title("WHATSAPP - SEM SALVAR CONTATO")
janela.geometry("500x300")
janela.config(bg="black")
janela.iconbitmap("cj.ico")
janela.mainloop()
