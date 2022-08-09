import tkinter
from tkinter import Label, PhotoImage, Button, messagebox
from tkinter.ttk import Treeview
import tkinter as tk
import tkinter.font as tkFont

from graficoconfig import GraficoConfig
from graficoconsferramenta import GraficoConsultaFerramenta
from graficoconstecnico import GraficoConsultaTecnico
from graficoreserva import GraficoReserva

from sistema.centraliza_janelas import center

class GraficoMain:
    def __init__(self):
        self.principal = tkinter.Tk()

        ## Ajustar tamanho da janela e não permitir maximizar
        self.principal.geometry("700x440")
        self.principal.resizable(width=False, height=False)


        self.principal.title('Conteúdo Audiovisual LTDA')
        center(self.principal)

        self.icon_config = PhotoImage(file="assets/icones/icon_config.png")
        self.icon_saida = PhotoImage(file="assets/icones/icon_saida.png")
        self.icon_reserva = PhotoImage(file="assets/icones/icon_reservas.png")
        self.icon_ferramenta = PhotoImage(file="assets/icones/icon_ferramenta.png")
        self.icon_tecnico = PhotoImage(file="assets/icones/icon_tecnico.png")
        self.icon_sobre = PhotoImage(file="assets/icones/icon_about.png")

        self.lb_sistema = Label(self.principal, text="Sistema de Reservas",font=tkFont.Font(size=20))
        self.lb_expira = Label(self.principal, text="Reservas Expirando",font=tkFont.Font(size=15))

        self.bt_tecnico = Button(self.principal, image=self.icon_tecnico, height=22, compound='left', padx=5, text="Técnicos", command=GraficoConsultaTecnico)
        self.bt_ferramenta = Button(self.principal, image=self.icon_ferramenta, height=22, compound='left', padx=5, text="Ferramentas", command=GraficoConsultaFerramenta)
        self.bt_reservar = Button(self.principal, image=self.icon_reserva, height=22, compound='left', padx=5, text="Reservas",command=GraficoReserva)
        self.bt_config = Button(self.principal, text="Config Email", image=self.icon_config, height=22, padx=5, compound='left', command=GraficoConfig)
        self.bt_sobre = Button(self.principal, text="Sobre", image=self.icon_sobre, height=22, padx=5, compound='left', command=self.sobre)
        self.bt_sair = Button(self.principal, text="Sair", image=self.icon_saida, compound='left', height=22, padx=5, command=self.principal.destroy)

        ## Inicio da Lista de Reservas
        self.nomes_colunas = ('col1', 'col2', 'col3')
        self.lista_reservas = Treeview(self.principal, columns=self.nomes_colunas, show='headings', height=14)
        self.lista_reservas.column('col1', width=255, stretch=False)
        self.lista_reservas.column('col2', width=255, stretch=False)
        self.lista_reservas.column('col3', width=168, stretch=False)

        self.lista_reservas.heading('col1', text='Ferramenta')
        self.lista_reservas.heading('col2', text='Tecnico')
        self.lista_reservas.heading('col3', text="Previsão de Entrega")
        ## Fim da lista de reserva

        self.lb_sistema.pack(side=tk.TOP)
        self.lb_expira.place(x=10,y=50)
        self.lista_reservas.place(x=10, y=80)
        self.bt_tecnico.place(x=10,y=400)
        self.bt_ferramenta.place(x=100,y=400)
        self.bt_reservar.place(x=210,y=400)
        self.bt_config.place(x=300,y=400)
        self.bt_sobre.place(x=412, y=400)
        self.bt_sair.place(x=635,y=400)

        self.principal.mainloop() ## Abre a janela no momento que a classe é chamada ou estanciada!

    def sobre(self):
        tk.messagebox.showinfo('Criadores', 'Diego Gomes\nJulio Marques\nKauã Marques\nValéria Souza ')

if __name__ == "__main__":
    GraficoMain()
