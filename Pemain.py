
class Pemain:
    def __init__(self):
        self.namaPemain = ""
        self.character = ""
        
    def __init__(self, namaPemain="", character=""):
        self.namaPemain = namaPemain
        self.character = character
    
    def getNamaPemain(self):
        return self.namaPemain
    
    def setNamaPemain(self, namaPemain):
        self.namaPemain = namaPemain
    
    def getCharacter(self):
        return self.character
    
    def setCharacter(self, character):
        self.character = character
    
