class Validadores:
    def __init__(self, valid1):
        self.validadores_entry ("")
    def validadores_entry(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 100

