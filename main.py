import tkinter
from tkinter import messagebox

from graficomain import GraficoMain
from sistema.banco import Banco

class Main:
    def __init__(self):
        self.abre_janela_inicial()

    def abre_janela_inicial(self):
        banco = Banco().conectar()

        if banco == False:
            tkinter.messagebox.showerror("Falha na conexão", "Não foi possivel conectar ao banco de dados Postgres. "
                                                             "Por favor, as configurações ou os dados de conexão")
        else:
            GraficoMain()

if __name__ == "__main__":
    janela = Main()