import tkinter
from tkinter import Label
from tkinter import Button
import tkinter as tk
import tkinter.font as tkFont

from graficoconfig import GraficoConfig
from sistema.centraliza_janelas import center

def abrir_configuracoes():
    janela = GraficoConfig()

principal = tkinter.Tk()
principal.geometry("600x400")
principal.title('Conteúdo Audiovisual LTDA')
center(principal)

lbsistema = Label(principal, text="Sistema de Reservas",font=tkFont.Font(size=20))
lbexpira = Label(principal, text="Reservas Expirando",font=tkFont.Font(size=15))

bttecnico = Button(principal, text="Técnicos")
btferramenta = Button(principal, text="Ferramentas")
btreservar = Button(principal, text="Reservas")
btconfig = Button(principal, text="Configurações", command=abrir_configuracoes)
btsair = Button(principal, text="Sair", command=principal.destroy)

lbsistema.pack(side=tk.TOP)
lbexpira.place(x=10,y=50)
bttecnico.place(x=10,y=360)
btferramenta.place(x=75,y=360)
btreservar.place(x=160,y=360)
btconfig.place(x=225,y=360)
btsair.place(x=550,y=360)


principal.mainloop()