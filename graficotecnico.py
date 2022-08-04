import tkinter
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import ttk

def acao():
    print("Pressionado")

principal = tkinter.Tk()
principal.geometry("400x175")
principal.title('Técnicos')


lbnome = Label(principal, text="Nome: ")
lbcpf = Label(principal, text="CPF: ")
lbtel = Label(principal, text="Telefone: ")
lbequipe = Label(principal, text="Equipe: ")
lbturno = Label(principal, text="Turno: ")


cxnome = Entry(principal, width = 45)
cxcpf = Entry(principal, width = 16)
cxtel = Entry(principal, width = 14)
cxequipe = Entry(principal, width = 35)
cxturno = ttk.Combobox(principal)
cxturno['values'] = ("Manhã","Tarde","Noite")


bteditar = Button(principal, text="Editar", command=acao)
btsalvar = Button(principal, text="Salvar", command=acao)
btfechar = Button(principal, text="Fechar", command=principal.quit)


lbnome.place(x=10,y=10)
cxnome.place(x=60,y=10)
lbcpf.place(x=10,y=40)
cxcpf.place(x=60,y=40)
lbtel.place(x=185,y=40)
cxtel.place(x=245,y=40)
lbequipe.place(x=10,y=70)
cxequipe.place(x=60,y=70)
lbturno.place(x=10,y=100)
cxturno.place(x=60,y=100)
bteditar.place(x=10,y=140)
btsalvar.place(x=290,y=140)
btfechar.place(x=340,y=140)


principal.mainloop()