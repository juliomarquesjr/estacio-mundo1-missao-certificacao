from openpyxl import Workbook
import pandas as pd

class Exportacao:
    def __init__(self, tabela):
        self.tabela = tabela

    def exportar(self):
        wb = Workbook()
        ws = wb.active

        # Adiciona as linhas ao WB onde será gerado o arquivo
        for linha in self.tabela:
            ws.append([linha[9], linha[0], linha[1],
                       linha[2], linha[3], linha[4],
                       linha[5], linha[6], linha[7],
                       linha[8]])

        # Salvando o arquivo e revisando se irá ocorrer erro
        try:
            wb.save("assets/exportacao/ferramentas.xlsx")

            read_file = pd.read_excel(r'assets/exportacao/ferramentas.xlsx', sheet_name='Sheet')
            read_file.to_csv(r'assets/exportacao/ferramentas.csv', index=None, header=True)

            return True
        except:
            print("Erro ao salvar o arquivo: ferramenta.xlsx")
            return False