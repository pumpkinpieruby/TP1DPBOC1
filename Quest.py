class Quest:
    def __init__(self):
        self.deskripsi = ""
        self.hadiah = ""
        
    def __init__(self, deskripsi="", hadiah=""):
        self.deskripsi = deskripsi
        self.hadiah = hadiah
    
    def getDeskripsi(self):
        return self.deskripsi
    
    def setDeskripsi(self, deskripsi):
        self.deskripsi = deskripsi
    
    def getHadiah(self):
        return self.hadiah
    
    def setHadiah(self, hadiah):
        self.hadiah = hadiah
