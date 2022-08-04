import tkinter
from tkinter import Label
from tkinter import Entry
from tkinter import Button

def acao():
    print("Pressionado")

principal = tkinter.Tk()
principal.geometry("450x300")
principal.title('Consultas - Ferramentas')


lbbusca = Label(principal, text="Buscar Ferramenta: ")
lblista = Label(principal, text="Lista de Ferramentas: ")


cxbusca = Entry(principal, width = 60)


btpesquisa = Button(principal, text="Pesquisar", command=acao)
btcadastrar = Button(principal, text="Cadastrar", command=acao)
btvisul_edit = Button(principal, text="Visualizar/Editar", command=acao)
btremover = Button(principal, text="Remover", command=acao)
btfechar = Button(principal, text="Fechar", command=principal.quit)




lbbusca.place(x=10,y=10)
cxbusca.place(x=10,y=40)
btpesquisa.place(x=380,y=35)
lblista.place(x=10,y=80)
#btcadastrar.place(x=290,y=140)
#btvisul_edit.place(x=10,y=140)
#btremover.place(x=290,y=140)
#btfechar.place(x=340,y=140)


principal.mainloop()