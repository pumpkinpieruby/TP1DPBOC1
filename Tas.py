from Status import Status

class Tas(Status):
    def __init__(self):
        self.koin = 0
        self.barang = []
        
    def __init__(self, nama="", gender="", role="", senjata="", hp=0, atk=0, deff=0, spd=0, koin=0, barang=[]):
        super().__init__(nama, gender, role, senjata, hp, atk, deff, spd)
        self.koin = koin
        self.barang = barang
    
    def getKoin(self):
        return self.koin
    
    def setKoin(self, koin):
        self.koin = koin
    
    def getBarang(self):
        return self.barang
    
    def tambahBarang(self, barang):
        self.barang.append(barang)
    
    def hapusBarang(self, barang):
        if barang in self.barang:
            self.barang.remove(barang)
            
    # Fungsi untuk menyerang karakter lain
    def attack(self, target, damage):
        print(f"{self.getNama()} menyerang {target.getNama()} dan mengurangi {damage} HP!")
        target.setHP(target.getHP() - damage)
    
    # Fungsi untuk memberikan heal ke karakter
    def heal(self, target, amount):
        print(f"{self.getNama()} memberikan heal kepada {target.getNama()} dan menambahkan {amount} HP!")
        target.setHP(target.getHP() + amount)
    
    def take_quest(self, npc, quest):
        if npc.getPeran() == "Pemberi Misi" and self.getHP() > 0:
            print(f"{self.getNama()} menerima quest dari {npc.getNama()}: {quest.getDeskripsi()}")
            return True
        else:
            print(f"{self.getNama()} tidak bisa menerima quest dari {npc.getNama()} saat ini.\n")
            return False
    
    def attack_npc(self, npc):
        if npc.getPeran() == "Musuh" and self.getHP() > 0 and self.getATK() > 1500:
            print(f"{self.getNama()} menyerang {npc.getNama()}!")
            npc.setHP(npc.getHP() - self.getATK())
        else:
            print(f"{self.getNama()} tidak dapat menyerang {npc.getNama()} saat ini.")