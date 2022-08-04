import tkinter
from tkinter import Label
from tkinter import Entry
from tkinter import Button

def acao():
    print("Pressionado")

principal = tkinter.Tk()
principal.geometry("500x230")
principal.title('Ferramentas')


lbcodigo = Label(principal, text="Código: ")
lbtamanho = Label(principal, text="Tamanho: ")
lbvolts = Label(principal, text="Voltagem: ")
lbund = Label(principal, text="Unidade: ")
lbtipo = Label(principal, text="Tipo: ")
lbmat = Label(principal, text="Material: ")
lbref = Label(principal, text="Referência: ")
lbtemp = Label(principal, text="Tempo Limite: ")
lbfab = Label(principal, text="Fabricante: ")
lbdesc = Label(principal, text="Descrição: ")


cxcodigo = Entry(principal, width = 15)
cxtamanho = Entry(principal, width = 25)
cxvolts = Entry(principal, width = 20)
cxund = Entry(principal, width = 20)
cxtipo = Entry(principal, width = 20)
cxmat = Entry(principal, width = 20)
cxref = Entry(principal, width = 30)
cxtemp = Entry(principal, width = 7)
cxfab = Entry(principal, width = 35)
cxdesc = Entry(principal, width = 65)


bteditar = Button(principal, text="Editar", command=acao)
btsalvar = Button(principal, text="Salvar", command=acao)
btfechar = Button(principal, text="Fechar", command=principal.quit)


lbcodigo.place(x=10,y=10)
cxcodigo.place(x=60,y=10)
lbtamanho.place(x=260,y=10)
cxtamanho.place(x=320,y=10)
lbvolts.place(x=10,y=40)
cxvolts.place(x=70,y=40)
lbund.place(x=295,y=40)
cxund.place(x=350,y=40)
lbtipo.place(x=10,y=70)
cxtipo.place(x=45,y=70)
lbmat.place(x=295,y=70)
cxmat.place(x=350,y=70)
lbref.place(x=10,y=100)
cxref.place(x=75,y=100)
lbtemp.place(x=340,y=100)
cxtemp.place(x=425,y=100)
lbfab.place(x=10,y=130)
cxfab.place(x=75,y=130)
lbdesc.place(x=10,y=160)
cxdesc.place(x=75,y=160)
bteditar.place(x=10,y=195)
btsalvar.place(x=390,y=195)
btfechar.place(x=440,y=195)


principal.mainloop()