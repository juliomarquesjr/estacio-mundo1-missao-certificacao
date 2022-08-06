import tkinter
from tkinter import Label, Entry, Button, PhotoImage
from tkinter.ttk import Treeview

from graficotecnico import GraficoTecnico
from sistema.centraliza_janelas import center

class GraficoConsultaTecnico:
    def __init__(self):
        self.principal = tkinter.Toplevel() #Top Level pois ela é filha de graficomain.py

        ## Ajustar tamanho da janela e não permitir maximizar.
        self.principal.geometry("600x360")
        self.principal.minsize(600, 360)
        self.principal.maxsize(600, 360)

        self.principal.title('Consultas - Técnicos')
        center(self.principal)

        ## Icones
        icon_cadastrar = PhotoImage(file="assets/icones/icon_cadastrar.png")
        icon_editar = PhotoImage(file="assets/icones/icon_editar.png")
        icon_remover = PhotoImage(file="assets/icones/icon_remove.png")
        icon_saida = PhotoImage(file="assets/icones/icon_saida.png")
        icon_pesquisar = PhotoImage(file="assets/icones/icon_pesquisar.png")
        icon_limpar = PhotoImage(file="assets/icones/icon_limpar.png")

        ## Labels.
        self.lb_busca = Label(self.principal, text="Buscar Técnico: ")
        self.lb_lista = Label(self.principal, text="Lista de Técnicos: ")

        ## Caixas de texto.
        self.cx_busca = Entry(self.principal, width=45, font='32')

        ## Lista de Técnicos
        self.nomes_colunas = ('col1', 'col2', 'col3')
        self.liste_tecnicos = Treeview(self.principal, columns=self.nomes_colunas, show='headings', height=12)

        self.liste_tecnicos = Treeview(self.principal, columns=self.nomes_colunas, show='headings', height=10)
        self.liste_tecnicos.column('col1', width=210, stretch=False)
        self.liste_tecnicos.column('col2', width=205, stretch=False)
        self.liste_tecnicos.column('col3', width=165, stretch=False)

        self.liste_tecnicos.heading('col1', text='Nome Copleto')
        self.liste_tecnicos.heading('col2', text='Telefone')
        self.liste_tecnicos.heading('col3', text="Cargo")
        ## Fim da lista de reserva

        ## Botões.
        self.bt_pesquisa = Button(self.principal, text="Pesquisar", image=icon_pesquisar, compound='left', padx=5, height=22)
        self.bt_limpar = Button(self.principal, text="Limpar", image=icon_limpar, compound='left', padx=5, height=22)
        self.bt_cadastrar = Button(self.principal, text="Cadastrar", image=icon_cadastrar, compound='left', padx=5, height=22, command=GraficoTecnico)
        self.bt_visul_edit = Button(self.principal, text="Visualizar/Editar", image=icon_editar, compound='left', padx=5, height=22)
        self.bt_remover = Button(self.principal, text="Remover", image=icon_remover, compound='left', padx=5, height=22)
        self.bt_fechar = Button(self.principal, text="Fechar", image=icon_saida, compound='left', padx=5, height=22, command=self.principal.destroy)

        ## Alinhamento dos componentes
        self.lb_busca.place(x=10, y=10)
        self.lb_lista.place(x=10, y=80)

        self.cx_busca.place(x=10, y=40)

        self.bt_pesquisa.place(x=425, y=35)
        self.bt_limpar.place(x=518, y=35)

        self.liste_tecnicos.place(x=10, y=80)

        self.bt_cadastrar.place(x=10, y=320)
        self.bt_visul_edit.place(x=105,y=320)
        self.bt_remover.place(x=235, y=320)
        self.bt_fechar.place(x=520,y=320)

        self.principal.mainloop() ## Abre a janela no momento que a classe é chamada ou estanciada.