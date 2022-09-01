class Validadores:
    def __init__(self,validadores2):
        self.validadores_entry()
    def validadores_entry(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 100