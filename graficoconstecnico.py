import tkinter
from tkinter import Label, Entry, Button, PhotoImage, messagebox, ttk
from tkinter.ttk import Treeview

from graficotecnico import GraficoTecnico
from sistema.centraliza_janelas import center

from sistema.banco import Banco

class GraficoConsultaTecnico:
    def __init__(self):
        self.principal = tkinter.Toplevel() #Top Level pois ela é filha de graficomain.py

        ## Ajustar tamanho da janela e não permitir maximizar.
        self.principal.geometry("692x360")
        self.principal.resizable(width=False, height=False)

        self.principal.title('Consultas - Técnicos')
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
        self.lb_busca = Label(self.principal, text="Buscar Técnico: ")
        self.lb_lista = Label(self.principal, text="Lista de Técnicos: ")

        ## Caixas de texto.
        self.cx_busca = Entry(self.principal, width=35, font='32')
        self.cx_opcoes = ttk.Combobox(self.principal, width=10, state="readonly")
        self.cx_opcoes['values'] = ("Nome", "CPF", "Equipe")
        self.cx_opcoes.current(0)

        ## Lista de Técnicos
        self.nomes_colunas = ('col1', 'col2', 'col3')
        self.lista_tecnicos = Treeview(self.principal, columns=self.nomes_colunas, show='headings', height=10)
        self.lista_tecnicos.column('col1', width=240, stretch=False)
        self.lista_tecnicos.column('col2', width=235, stretch=False)
        self.lista_tecnicos.column('col3', width=195, stretch=False)

        self.lista_tecnicos.heading('col1', text='Nome')
        self.lista_tecnicos.heading('col2', text='CPF')
        self.lista_tecnicos.heading('col3', text="Equipe")
        ## Fim da lista de reserva

        ## Botões.
        self.bt_atualizar = Button(self.principal, text="Atualizar", image=self.icon_atualizar, compound='left', padx=5, height=22, command=self.consulta_tecnicos)
        self.bt_pesquisa = Button(self.principal, text="Pesquisar", image=self.icon_pesquisar, compound='left', padx=5, height=22, command=self.pesquisa_tecnico)
        self.bt_limpar = Button(self.principal, text="Limpar", image=self.icon_limpar, compound='left', padx=5, height=22, command=self.limpar_pesquisa)
        self.bt_cadastrar = Button(self.principal, text="Cadastrar", image=self.icon_cadastrar, compound='left', padx=5, height=22, command=GraficoTecnico)
        self.bt_visul_edit = Button(self.principal, text="Visualizar/Editar", image=self.icon_editar, compound='left', padx=5, height=22, command=self.editar_tecnico)
        self.bt_remover = Button(self.principal, text="Remover", image=self.icon_remover, compound='left', padx=5, height=22, command=self.remover_tecnico)
        self.bt_fechar = Button(self.principal, text="Fechar", image=self.icon_saida, compound='left', padx=5, height=22, command=self.principal.destroy)

        ## Alinhamento dos componentes
        self.lb_busca.place(x=10, y=10)
        self.lb_lista.place(x=10, y=80)

        self.cx_busca.place(x=10, y=40)
        self.cx_opcoes.place(x=335,y=41)

        self.bt_pesquisa.place(x=425, y=35)
        self.bt_atualizar.place(x=518, y=35)
        self.bt_limpar.place(x=608, y=35)

        self.lista_tecnicos.place(x=10, y=80)

        self.bt_cadastrar.place(x=10, y=320)
        self.bt_visul_edit.place(x=105,y=320)
        self.bt_remover.place(x=235, y=320)
        self.bt_fechar.place(x=610,y=320)

        self.consulta_tecnicos()

        self.principal.focus_force()  # Mantem o focus na janela ativa
        self.principal.grab_set()  # Matem no top até ser fechada

        self.principal.mainloop() ## Abre a janela no momento que a classe é chamada ou estanciada!


    def consulta_tecnicos(self):
        if self.cx_busca.get() != '':
            self.pesquisa_tecnico()
        else:
            self.lista_tecnicos.delete(*self.lista_tecnicos.get_children())
            consulta = Banco().consultar_dados('tecnico')
            for valor in consulta:
                self.lista_tecnicos.insert('', tkinter.END, values=(valor[0], valor[1], valor[4]))

    def pesquisa_tecnico(self):
        var_busca = 'nome'

        if self.cx_opcoes.get() == "Nome":
            var_busca = 'nome'
        elif self.cx_opcoes.get() == "Equipe":
            var_busca = 'nome_equipe'
        elif self.cx_opcoes.get() == "CPF":
            var_busca = 'cpf'

        self.lista_tecnicos.delete(*self.lista_tecnicos.get_children())
        self.consulta = Banco().consultar_nomes('tecnico', var_busca, like=self.cx_busca.get())

        for valor in self.consulta:
            self.lista_tecnicos.insert('', tkinter.END, values=(valor[0], valor[1], valor[4]))

    def limpar_pesquisa(self):
        self.cx_busca.delete(0, 'end')

    def remover_tecnico(self):
        self.cpf_selecionado = False
        for iten_selcionado in self.lista_tecnicos.selection():
            self.cpf_selecionado = self.lista_tecnicos.item(iten_selcionado)['values'][1]

        if self.cpf_selecionado == False:
            tkinter.messagebox.showerror("Falha ao remover",
                                         "Por favor, selecione um técnico para realizar a remoção.", parent=self.principal)
        else:
            self.consulta = Banco().remover_dados('tecnico', where=f"cpf = '{self.cpf_selecionado}'")


            if self.consulta:
                tkinter.messagebox.showinfo("Remover técnico", "Técnico Removido com sucesso!", parent=self.principal)
            else:
                tkinter.messagebox.showerror("Falha ao remover", "Não foi possível remover o técnico. Por favor, tente novamente.", parent=self.principal)

        self.principal.lift()
        self.consulta_tecnicos()

    def editar_tecnico(self):
        self.cpf_selecionado = False

        for item_selecionado in self.lista_tecnicos.selection():
            self.cpf_selecionado = \
            self.lista_tecnicos.item(item_selecionado)['values'][1]

        if self.cpf_selecionado == False:
            tkinter.messagebox.showerror("Erro ao abrir técnico", "Por favor, selecione um técnico na lista para realizar sua Visualização/Edição.", parent=self.principal)
        else:
            GraficoTecnico(self.cpf_selecionado)