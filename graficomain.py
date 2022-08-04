import tkinter
from tkinter import Label, PhotoImage, Button
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

        self.icon_config = PhotoImage(file="assets/icones/icon_config.png")
        self.icon_saida = PhotoImage(file="assets/icones/icon_saida.png")
        self.icon_reserva = PhotoImage(file="assets/icones/icon_reservas.png")
        self.icon_ferramenta = PhotoImage(file="assets/icones/icon_ferramenta.png")
        self.icon_tecnico = PhotoImage(file="assets/icones/icon_tecnico.png")

        self.lbsistema = Label(self.principal, text="Sistema de Reservas",font=tkFont.Font(size=20))
        self.lbexpira = Label(self.principal, text="Reservas Expirando",font=tkFont.Font(size=15))

        self.bttecnico = Button(self.principal, image=self.icon_tecnico, height=22, compound='left', padx=5, text="Técnicos")
        self.btferramenta = Button(self.principal, image=self.icon_ferramenta, height=22, compound='left', padx=5, text="Ferramentas")
        self.btreservar = Button(self.principal, image=self.icon_reserva, height=22, compound='left', padx=5, text="Reservas")
        self.btconfig = Button(self.principal, text="Configurações", image=self.icon_config, height=22, padx=5, compound='left', command=GraficoConfig)
        self.btsair = Button(self.principal, text="Sair", image=self.icon_saida, compound='left', height=22, padx=5, command=self.principal.destroy)

        self.lbsistema.pack(side=tk.TOP)
        self.lbexpira.place(x=10,y=50)
        self.bttecnico.place(x=10,y=360)
        self.btferramenta.place(x=100,y=360)
        self.btreservar.place(x=210,y=360)
        self.btconfig.place(x=300,y=360)
        self.btsair.place(x=530,y=360)

        self.principal.mainloop()

janela = GraficoMain()