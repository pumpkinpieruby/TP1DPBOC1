from Tas import Tas
from NPC import NPC
from Quest import Quest
from Pemain import Pemain

# Membuat objek tas untuk setiap karakter player
DanhengIl = Tas("DanhengIL", "Male", "DPS", "Beneficent Lotus", 3448, 3252, 1098, 104, 50000, ["Potion", "Kunci"])
Loucha = Tas("Loucha", "Male", "Healer", "Pedang", 5439, 3087, 986, 101, 30000, ["Potion", "Koin"])
Blade = Tas("Blade", "Male", "sub-DPS", "Pedang", 8030, 1527, 978, 103, 40000, ["Potion", "Kunci"])
fuxuan = Tas("fuxuan", "Female", "Shielder", "Sihir", 9382, 1400, 1592, 102, 60000, ["Potion", "Koin"])


# Membuat objek NPC
adrian = NPC("Adrian", "Male", "Pemberi Misi")
lyra = NPC("Lyra", "Female", "Penjual")
Thor = NPC("Thor", "Male", "Musuh")


# Membuat objek quest
quest1 = Quest("Bertarung dengan monster", "10000 koin")
quest2 = Quest("Mengumpulkan barang langka", "20000 koin\n")

# Membuat objek pemain dan menambahkan karakter
fauzan = Pemain("Fauzan", [DanhengIl])
yasin = Pemain("Yasin", [Loucha])
bintang = Pemain("Bintang", [Blade])
mia = Pemain("Mia", [fuxuan])

# Menampilkan informasi tas karakter player
print("\nTas Karakter:")
print("Isi Tas DanhengIl:", DanhengIl.getBarang())
print("Isi Tas Loucha:", Loucha.getBarang())
print("Isi Tas Blade:", Blade.getBarang())
print("Isi Tas Fuxuan:", fuxuan.getBarang())

# Menampilkan informasi NPC
print("\nNPC:")
print("Adrian:", adrian.getNama(), "- Tipe:", adrian.getPeran())
print("Lyra:", lyra.getNama(), "- Tipe:", lyra.getPeran())
print("Thor:", Thor.getNama(), "- Tipe:", Thor.getPeran())

# Menampilkan informasi quest
print("\nQuest:")
print("Quest 1:", quest1.getDeskripsi(), "- Hadiah:", quest1.getHadiah())
print("Quest 2:", quest2.getDeskripsi(), "- Hadiah:", quest2.getHadiah())

adrian.give_quest(Blade, quest1, required_item="Kunci")
Blade.take_quest(adrian, quest1)  # Blade takes a quest from Adrian
# Menampilkan informasi karakter sebelum serangan
print("Informasi Karakter Sebelum Serangan:")
print("DanhengIl milik Fauzan:")
print(DanhengIl.get_status_table())
print("\nLoucha milik Yasin:")
print(Loucha.get_status_table())
print("\nBlade milik Bintang:")
print(Blade.get_status_table())
print("\nFuxuan milik Mia:")
print(fuxuan.get_status_table())
print("\nThor:")
print(Thor.get_status_table())  

Thor.attack(DanhengIl, 2012)
Thor.attack(Loucha,2012)
Thor.attack(Blade,2012)
Thor.attack(fuxuan,2012)
Blade.attack_npc(Thor)             # Blade successfully attacks Thor
print("\nInformasi Karakter Sesudah Serangan:")
print("DanhengIl milik Fauzan:")
print(DanhengIl.get_status_table())
print("\nLoucha milik Yasin:")
print(Loucha.get_status_table())
print("\nBlade milik Bintang:")
print(Blade.get_status_table())
print("\nFuxuan milik Mia:")
print(fuxuan.get_status_table())
print("\nThor:")
print(Thor.get_status_table())

Loucha.heal(DanhengIl, 1007)
print("\nInformasi Karakter Sesudah di heal:")
print("DanhengIl milik Fauzan:")
print(DanhengIl.get_status_table())

lyra.give_quest(Loucha, quest1, required_item="bunga")
Loucha.take_quest(lyra, quest2)   # Loucha tries to take a quest from Lyra but fails

fuxuan.attack_npc(Thor)               # Mia tries to attack Thor but fails due to low attack power
