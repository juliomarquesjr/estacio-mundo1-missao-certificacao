import tkinter
from tkinter import Label, ttk, Button, Entry, PhotoImage, messagebox

from sistema.centraliza_janelas import center
from tecnico import Tecnico

class GraficoTecnico():
    def __init__(self):
        self.principal = tkinter.Toplevel()

        self.principal.geometry("400x150")
        self.principal.title('Técnicos')
        self.principal.resizable(height=False, width=False)
        center(self.principal)


        ## Labels
        self.lb_nome = Label(self.principal, text="Nome: ")
        self.lb_cpf = Label(self.principal, text="CPF: ")
        self.lb_tel = Label(self.principal, text="Telefone: ")
        self.lb_equipe = Label(self.principal, text="Equipe: ")
        self.lb_turno = Label(self.principal, text="Turno: ")

        ## Icones
        self.icon_salvar = PhotoImage(file="assets/icones/icon_salvar.png")
        self.icon_fechar = PhotoImage(file="assets/icones/icon_saida.png")
        self.icon_editar = PhotoImage(file="assets/icones/icon_editar.png")

        ## Caixas de Texto
        self.cx_nome = Entry(self.principal, width=54)
        self.cx_cpf = Entry(self.principal, width=22)
        self.cx_tel = Entry(self.principal, width=20)
        self.cx_equipe = Entry(self.principal, width=22)
        self.cx_turno = ttk.Combobox(self.principal, width=17)
        self.cx_turno['values'] = ("Manhã", "Tarde", "Noite")

        ## Botoes
        self.bt_editar = Button(self.principal, text="Editar", image=self.icon_editar, compound='left', padx=5, height=22)
        self.bt_salvar = Button(self.principal, text="Salvar", image=self.icon_salvar, compound='left', padx=5, height=22, command=self.cadastrar)
        self.bt_fechar = Button(self.principal, text="Fechar", image=self.icon_fechar, compound='left', padx=5, height=22, command=self.principal.destroy)

        ## Alinhamento dos componentes
        self.lb_nome.place(x=10,y=10)
        self.lb_cpf.place(x=10, y=40)
        self.lb_tel.place(x=205, y=40)
        self.lb_equipe.place(x=10, y=70)
        self.lb_turno.place(x=205, y=70)

        self.cx_nome.place(x=60,y=10)
        self.cx_cpf.place(x=60, y=40)
        self.cx_tel.place(x=265, y=40)
        self.cx_equipe.place(x=60, y=70)
        self.cx_turno.place(x=265, y=70)

        self.bt_editar.place(x=10,y=110)
        self.bt_salvar.place(x=85,y=110)
        self.bt_fechar.place(x=320,y=110)


        self.principal.mainloop() ## Abre a janela no momento em que a classe é estanciada

    def cadastrar(self):
        self.novo_tecnico = Tecnico(self.cx_nome.get(),
                                    self.cx_cpf.get(),
                                    self.cx_tel.get(),
                                    self.cx_turno.get(),
                                    self.cx_equipe.get())

        if self.novo_tecnico.cadastra_banco():
            tkinter.messagebox.showinfo("Cadastro de Tecnico", "Cadastro realizado com sucesso!")
        else:
            tkinter.messagebox.showerror("Falha ao cadastrar", "Deu uma ruim maluco!")

        self.principal.lift()