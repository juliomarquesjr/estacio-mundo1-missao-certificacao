import tkinter
from tkinter import Label, Entry, Button, PhotoImage, messagebox
from tkinter.ttk import Treeview

from sistema.banco import Banco
from graficoferramenta import GraficoFerramenta
from sistema.centraliza_janelas import center

class GraficoConsultaFerramenta:
    def __init__(self):
        self.principal = tkinter.Toplevel() #Top Level pois ela é filha de graficomain.py

        ## Ajustar tamanho da janela e não permitir maximizar.
        self.principal.geometry("690x360")
        self.principal.resizable(width=False, height=False)

        self.principal.title('Consultas - Ferramentas')
        center(self.principal)

        ## Icones
        self.icon_cadastrar = PhotoImage(file="assets/icones/icon_cadastrar.png")
        self.icon_editar = PhotoImage(file="assets/icones/icon_editar.png")
        self.icon_remover = PhotoImage(file="assets/icones/icon_remove.png")
        self.icon_saida = PhotoImage(file="assets/icones/icon_saida.png")
        self.icon_pesquisar = PhotoImage(file="assets/icones/icon_pesquisar.png")
        self.icon_limpar = PhotoImage(file="assets/icones/icon_limpar.png")
        self.icon_atualizar = PhotoImage(file="assets/icones/icon_atualizar.png")

        ## Labels.
        self.lb_busca = Label(self.principal, text="Buscar Ferramenta: ")
        self.lb_lista = Label(self.principal, text="Lista de Ferramentas: ")

        ## Caixas de texto.
        self.cx_busca = Entry(self.principal, width=45, font='32')

        ## Lista de Ferramentas
        self.nomes_colunas = ('col1', 'col2', 'col3')
        self.lista_ferramentas = Treeview(self.principal, columns=self.nomes_colunas, show='headings', height=10)
        self.lista_ferramentas.column('col1', width=217, stretch=False)
        self.lista_ferramentas.column('col2', width=245, stretch=False)
        self.lista_ferramentas.column('col3', width=205, stretch=False)

        self.lista_ferramentas.heading('col1', text='Código')
        self.lista_ferramentas.heading('col2', text='Nome da Ferramenta')
        self.lista_ferramentas.heading('col3', text="Fabricante")
        ## Fim da lista de reserva

        ## Botões.
        self.bt_pesquisa = Button(self.principal, text="Pesquisar", image=self.icon_pesquisar, compound='left', padx=5, height=22, command=self.pesquisa_ferramenta)
        self.bt_atualizar = Button(self.principal, text="Atualizar", image=self.icon_atualizar, compound='left', padx=5,height=22, command=self.consulta_ferramentas)
        self.bt_limpar = Button(self.principal, text="Limpar", image=self.icon_limpar, compound='left', padx=5, height=22, command=self.limpar_pesquisa)
        self.bt_cadastrar = Button(self.principal, text="Cadastrar", image=self.icon_cadastrar, compound='left', padx=5, height=22, command=GraficoFerramenta)
        self.bt_visul_edit = Button(self.principal, text="Visualizar/Editar", image=self.icon_editar, compound='left', padx=5, height=22)
        self.bt_remover = Button(self.principal, text="Remover", image=self.icon_remover, compound='left', padx=5, height=22, command=self.remover_ferramenta)
        self.bt_fechar = Button(self.principal, text="Fechar", image=self.icon_saida, compound='left', padx=5, height=22, command=self.principal.destroy)

        ## Alinhamento dos componentes
        self.lb_busca.place(x=10, y=10)
        self.lb_lista.place(x=10, y=80)

        self.cx_busca.place(x=10, y=40)

        self.bt_pesquisa.place(x=425, y=35)
        self.bt_atualizar.place(x=518, y=35)
        self.bt_limpar.place(x=608, y=35)

        self.lista_ferramentas.place(x=10, y=80)

        self.bt_cadastrar.place(x=10, y=320)
        self.bt_visul_edit.place(x=105, y=320)
        self.bt_remover.place(x=235, y=320)
        self.bt_fechar.place(x=610, y=320)

        self.consulta_ferramentas()

        self.principal.focus_force()  # Mantem o focus na janela ativa
        self.principal.grab_set()  # Matem no top até ser fechada

        self.principal.mainloop() ## Abre a janela no momento que a classe é chamada ou estanciada!

    def consulta_ferramentas(self):
        self.lista_ferramentas.delete(*self.lista_ferramentas.get_children())
        consulta = Banco().consultar_dados('ferramenta')

        for valor in consulta:
            self.lista_ferramentas.insert('', tkinter.END, values=(valor[0], valor[1], valor[2]))

    def pesquisa_ferramenta(self):
        self.lista_ferramentas.delete(*self.lista_ferramentas.get_children())
        consulta = Banco().consultar_dados('ferramenta', where=f"descricao_ferramenta = '{self.cx_busca.get()}'")
        for valor in consulta:
            self.lista_ferramentas.insert('', tkinter.END, values=(valor[0], valor[1], valor[2]))

    def limpar_pesquisa(self):
        self.cx_busca.delete(0, 'end')
        #self.consulta_ferramentas()

    def remover_ferramenta(self):
        for iten_selcionado in self.lista_ferramentas.selection():
            self.cod_selecionado = self.lista_ferramentas.item(iten_selcionado)['values'][0]

        self.consulta = Banco().remover_dados('ferramenta', where=f"cod_ferramenta = '{self.cod_selecionado}'")

        if self.consulta:
            tkinter.messagebox.showinfo("Remover ferramenta", "Ferramenta removida com sucesso!")
        else:
            tkinter.messagebox.showerror("Falha ao remover", "Não foi possível remover a ferramenta. Por favor, tente novamente.")

        self.consulta_ferramentas()
        self.principal.lift()