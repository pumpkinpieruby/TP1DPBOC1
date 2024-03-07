from Human import Human
from tabulate import tabulate

class NPC(Human):
    def __init__(self):
        self.peran = ""
        self.hp = 0
        
    def __init__(self, nama="", gender="", peran="", hp=1500):  # Assume default HP is 1500
        super().__init__(nama, gender)
        self.peran = peran
        self.hp = hp
    
    def getPeran(self):
        return self.peran
    
    def setPeran(self, peran):
        self.peran = peran

    def getHP(self):
        return self.hp

    def setHP(self, hp):
        self.hp = hp

    def increaseHP(self, amount):
        self.hp += amount

    def decreaseHP(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
    
    def attack(self, target, damage):
        print(f"{self.nama} menyerang {target.getNama()} dan mengurangi {damage} HP!")
        target.setHP(target.getHP() - damage)
    
    def give_quest(self, chara, quest, required_item=None):
        if required_item and required_item not in chara.getBarang():
            print(f"{self.getNama()} tidak dapat memberikan quest kepada {chara.getNama()} karena {chara.getNama()} tidak memiliki barang yang dibutuhkan.")
            return False

        if chara.getHP() > 0:
            print(f"{self.getNama()} memberikan quest kepada {chara.getNama()}: {quest.getDeskripsi()}")
            return True
        else:
            print(f"{self.getNama()} tidak dapat memberikan quest kepada {chara.getNama()} karena karakter sedang tidak aktif.\n")
            return False
        
    def get_status_table(self):
        headers = ["Nama", "Gender", "Peran", "HP"]
        data = [[self.getNama(), self.getGender(), self.peran, self.hp]]
        return tabulate(data, headers=headers, tablefmt="grid")