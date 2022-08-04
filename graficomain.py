import tkinter
from tkinter import Label
from tkinter import Button
import tkinter as tk
import tkinter.font as tkFont

from graficoconfig import GraficoConfig
from sistema.centraliza_janelas import center

class GraficoMain:
    def __init__(self):
        self.principal = tkinter.Tk()
        self.principal.geometry("600x400")
        self.principal.title('Conteúdo Audiovisual LTDA')
        center(self.principal)

        self.lbsistema = Label(self.principal, text="Sistema de Reservas",font=tkFont.Font(size=20))
        self.lbexpira = Label(self.principal, text="Reservas Expirando",font=tkFont.Font(size=15))

        self.bttecnico = Button(self.principal, text="Técnicos")
        self.btferramenta = Button(self.principal, text="Ferramentas")
        self.btreservar = Button(self.principal, text="Reservas")
        self.btconfig = Button(self.principal, text="Configurações", command=GraficoConfig)
        self.btsair = Button(self.principal, text="Sair", command=self.principal.destroy)

        self.lbsistema.pack(side=tk.TOP)
        self.lbexpira.place(x=10,y=50)
        self.bttecnico.place(x=10,y=360)
        self.btferramenta.place(x=75,y=360)
        self.btreservar.place(x=160,y=360)
        self.btconfig.place(x=225,y=360)
        self.btsair.place(x=550,y=360)

        self.principal.mainloop()

janela = GraficoMain()