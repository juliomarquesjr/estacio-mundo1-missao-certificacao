import tkinter
from tkinter import Label, Entry, Button, PhotoImage, messagebox, ttk
from tkinter.ttk import Treeview

from sistema.banco import Banco
from sistema.exportacao import Exportacao
from graficoferramenta import GraficoFerramenta
from ferramenta import Ferramenta
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
        self.icon_imprimir = PhotoImage(file="assets/icones/icon_imprimir.png")
        self.icon_saida = PhotoImage(file="assets/icones/icon_saida.png")
        self.icon_pesquisar = PhotoImage(file="assets/icones/icon_pesquisar.png")
        self.icon_limpar = PhotoImage(file="assets/icones/icon_limpar.png")
        self.icon_atualizar = PhotoImage(file="assets/icones/icon_atualizar.png")

        ## Labels.
        self.lb_busca = Label(self.principal, text="Buscar Ferramenta: ")
        self.lb_lista = Label(self.principal, text="Lista de Ferramentas: ")

        ## Caixas de texto.
        self.cx_busca = Entry(self.principal, width=35, font='32')
        self.cx_opcoes = ttk.Combobox(self.principal, width=10, state="readonly")
        self.cx_opcoes['values'] = ("Nome", "Fabricante")
        self.cx_opcoes.current(0)

        ## Lista de Ferramentas
        self.nomes_colunas = ('col1', 'col2', 'col3', 'col4')
        self.lista_ferramentas = Treeview(self.principal, columns=self.nomes_colunas, show='headings', height=10)
        self.lista_ferramentas.column('col1', width=295, stretch=False)
        self.lista_ferramentas.column('col2', width=107, stretch=False)
        self.lista_ferramentas.column('col3', width=165, stretch=False)
        self.lista_ferramentas.column('col4', width=105, stretch=False)

        self.lista_ferramentas.heading('col1', text='Nome da Ferramenta')
        self.lista_ferramentas.heading('col2', text='Código')
        self.lista_ferramentas.heading('col3', text="Fabricante")
        self.lista_ferramentas.heading('col4', text="Tempo")
        ## Fim da lista de reserva

        ## Botões.
        self.bt_pesquisa = Button(self.principal, text="Pesquisar", image=self.icon_pesquisar, compound='left', padx=5, height=22, command=self.pesquisa_ferramenta)
        self.bt_atualizar = Button(self.principal, text="Atualizar", image=self.icon_atualizar, compound='left', padx=5,height=22, command=self.consulta_ferramentas)
        self.bt_limpar = Button(self.principal, text="Limpar", image=self.icon_limpar, compound='left', padx=5, height=22, command=self.limpar_pesquisa)
        self.bt_cadastrar = Button(self.principal, text="Cadastrar", image=self.icon_cadastrar, compound='left', padx=5, height=22, command=GraficoFerramenta)
        self.bt_visul_edit = Button(self.principal, text="Visualizar/Editar", image=self.icon_editar, compound='left', padx=5, height=22, command=self.editar_ferramenta)
        self.bt_remover = Button(self.principal, text="Remover", image=self.icon_remover, compound='left', padx=5, height=22, command=self.remover_ferramenta)
        self.bt_imprimir = Button(self.principal, text="Imprimir", image=self.icon_imprimir, compound='left', padx=5, height=22, command=self.exportar_csv)
        self.bt_fechar = Button(self.principal, text="Fechar", image=self.icon_saida, compound='left', padx=5, height=22, command=self.principal.destroy)

        ## Alinhamento dos componentes
        self.lb_busca.place(x=10, y=10)
        self.lb_lista.place(x=10, y=80)

        self.cx_busca.place(x=10, y=40)
        self.cx_opcoes.place(x=335, y=41)

        self.bt_pesquisa.place(x=425, y=35)
        self.bt_atualizar.place(x=518, y=35)
        self.bt_limpar.place(x=608, y=35)

        self.lista_ferramentas.place(x=10, y=80)

        self.bt_cadastrar.place(x=10, y=320)
        self.bt_visul_edit.place(x=105, y=320)
        self.bt_remover.place(x=235, y=320)
        self.bt_imprimir.place(x=518, y=320)
        self.bt_fechar.place(x=608, y=320)

        self.consulta_ferramentas()

        self.principal.focus_force()  # Mantem o focus na janela ativa
        self.principal.grab_set()  # Matem no top até ser fechada

        self.principal.mainloop() ## Abre a janela no momento que a classe é chamada ou estanciada!

    def consulta_ferramentas(self):
        self.lista_ferramentas.delete(*self.lista_ferramentas.get_children())
        consulta = Banco().consultar_dados('ferramenta')

        for valor in consulta:
            self.lista_ferramentas.insert('', tkinter.END, values=(valor[0], valor[9], valor[1], f'{valor[8]} horas'))

    def pesquisa_ferramenta(self):
        var_busca = 'descricao_ferramenta'

        if self.cx_opcoes.get() == "Nome":
            var_busca = 'descricao_ferramenta'

        elif self.cx_opcoes.get() == 'Fabricante':
            var_busca = 'fabricante'


        self.lista_ferramentas.delete(*self.lista_ferramentas.get_children())
        self.consulta = Banco().consultar_nomes('ferramenta', var_busca, like=self.cx_busca.get())

        for valor in self.consulta:
            self.lista_ferramentas.insert('', tkinter.END, values=(valor[0], valor[9], valor[1], f'{valor[8]} horas'))

    def limpar_pesquisa(self):
        self.cx_busca.delete(0, 'end')

    def remover_ferramenta(self):
        self.cod_selecionado = False
        for iten_selcionado in self.lista_ferramentas.selection():
            self.cod_selecionado = self.lista_ferramentas.item(iten_selcionado)['values'][1]

        if self.cod_selecionado == False:
            tkinter.messagebox.showerror("Falha ao remover",
                                         "Por favor, selecione uma ferramenta para realizar a remoção.", parent=self.principal)
        else:
            self.consulta = Ferramenta().remover_banco(self.cod_selecionado)

            if self.consulta:
                tkinter.messagebox.showinfo("Remover ferramenta", "Ferramenta removida com sucesso!", parent=self.principal)
            else:
                tkinter.messagebox.showerror("Falha ao remover", "Não foi possível remover a ferramenta. Por favor, tente novamente.", parent=self.principal)

            self.principal.lift()
            self.consulta_ferramentas()

    def editar_ferramenta(self):
        self.cod_ferramenta = False

        for item_selecionado in self.lista_ferramentas.selection():
            self.cod_ferramenta = \
                self.lista_ferramentas.item(item_selecionado)['values'][1]

        if self.cod_ferramenta == False:
            tkinter.messagebox.showerror("Erro ao abrir técnico",
                                         "Por favor, selecione um técnico na lista para realizar sua Visualização/Edição.",
                                         parent=self.principal)
        else:
            GraficoFerramenta(self.cod_ferramenta)

    def exportar_csv(self):
        self.data_banco = Banco().consultar_dados('ferramenta')
        self.resultado = Exportacao(self.data_banco).exportar()

        if self.resultado == True:
            tkinter.messagebox.showinfo("Exportar Excel", "Exportação realizada com sucesso", parent=self.principal)
        else:
            tkinter.messagebox.showerror("Exportar Excel", "Falha ao realizar a exportação. Verifique com o administrador do sistema.",
                                         parent=self.principal)