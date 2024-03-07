from Human import Human

class Chara(Human):
    def __init__(self):
        self.role = ""
        self.senjata = ""
    
    def __init__(self, nama="", gender="", role="", senjata=""):
        super().__init__(nama, gender)
        self.role = role
        self.senjata = senjata
    
    def getRole(self):
        return self.role
    
    def setRole(self, role):
        self.role = role
    
    def getSenjata(self):
        return self.senjata
    
    def setSenjata(self, senjata):
        self.senjata = senjata
        
    