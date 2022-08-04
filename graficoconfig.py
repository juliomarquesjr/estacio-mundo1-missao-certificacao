import tkinter
from tkinter import Label
from tkinter import Entry
from tkinter import Button

def acao():
    print("Pressionado")

principal = tkinter.Tk()
principal.geometry("200x175")
principal.title('Configurações')


lbhost = Label(principal, text="Host: ")
lbusuario = Label(principal, text="Usuário: ")
lbsenha = Label(principal, text="Senha: ")
lbporta = Label(principal, text="Porta: ")


cxhost = Entry(principal, width = 15)
cxusuario = Entry(principal, width = 15)
cxsenha = Entry(principal, width = 15)
cxporta = Entry(principal, width = 15)


btsalvar = Button(principal, text="Salvar", command=acao)
btfechar = Button(principal, text="Fechar", command=principal.quit)


lbhost.place(x=20,y=10)
cxhost.place(x=75,y=10)
lbusuario.place(x=20,y=40)
cxusuario.place(x=75,y=40)
lbsenha.place(x=20,y=70)
cxsenha.place(x=75,y=70)
lbporta.place(x=20,y=100)
cxporta.place(x=75,y=100)
btsalvar.place(x=90,y=140)
btfechar.place(x=140,y=140)


principal.mainloop()

