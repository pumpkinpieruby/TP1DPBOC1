from tabulate import tabulate
from Chara import Chara

class Status(Chara):
    def __init__(self):
        self.hp = 0
        self.atk = 0
        self.deff = 0
        self.spd = 0
    
    def __init__(self, nama="", gender="", role="", senjata="", hp=0, atk=0, deff=0, spd=0):
        super().__init__(nama, gender, role, senjata)
        self.hp = hp
        self.atk = atk
        self.deff = deff
        self.spd = spd
    
    def getHP(self):
        return self.hp
    
    def setHP(self, hp):
        self.hp = hp
    
    def getATK(self):
        return self.atk
    
    def setATK(self, atk):
        self.atk = atk
    
    def getDEFF(self):
        return self.deff
    
    def setDEFF(self, deff):
        self.deff = deff
    
    def getSPD(self):
        return self.spd
    
    def setSPD(self, spd):
        self.spd = spd
    
    def get_status_table(self):
        headers = ["Nama", "Gender", "Role", "Senjata", "HP", "ATK", "DEFF", "SPD"]
        data = [[self.getNama(), self.getGender(), self.role, self.senjata, self.hp, self.atk, self.deff, self.spd]]
        return tabulate(data, headers=headers, tablefmt="grid")
    
