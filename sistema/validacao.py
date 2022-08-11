class Validadores:
    def validadores_entry2(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= 100

