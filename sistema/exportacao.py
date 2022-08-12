from openpyxl import Workbook

class Exportacao:
    def __init__(self, tabela):
        self.tabela = tabela

    def exportar(self):
        wb = Workbook()
        ws = wb.active

        # Adiciona as linhas ao WB onde será gerado o arquivo
        for linha in self.tabela:
            ws.append([linha[0], linha[1], linha[2], linha[3], linha[4]])
            print(linha[0])

        # Salvando o arquivo e revisando se irá ocorrer erro
        try:
            wb.save("assets/exportacao/ferramentas.xlsx")
            return True
        except:
            print("Erro ao salvar o arquivo: ferramenta.xlsx")
            return False