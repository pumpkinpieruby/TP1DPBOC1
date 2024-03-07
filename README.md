# Janji 
Saya Septiani Eka Putri NIM 2206000 mengerjakan Tugas Praktikum 1 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin

## Desain Program 

Terdiri dari 7 class yaitu **Human**, **Chara**, **NPC**, **Status**, **Tas**, **Quest**, dan **Pemain**

### Diagram
![Diagram](<Screenshot 2024-03-07 230812.png>)

**Human:**
* Atribut:
    * nama (string): Menyimpan nama karakter (Chara atau NPC).
    * gender (string): Menyimpan jenis kelamin karakter.

**Chara (Character):**
Turunan dari kelas Human.
* Atribut:
    * role (string): Peran karakter dalam permainan (DPS, Healer, sub-DPS, Shielder).
    * senjata (string): Senjata yang dimiliki oleh karakter.

**Status:**
Turunan dari kelas Chara.
* Atribut:
    * hp (int): Menyimpan jumlah hit points (HP) karakter.
    * atk (int): Menyimpan nilai serangan (Attack) karakter.
    * deff (int): Menyimpan nilai pertahanan (Defense) karakter.
    * spd (int): Menyimpan nilai kecepatan (Speed) karakter.

**Tas (Bag):**
Turunan dari kelas Status.
* Atribut:
    * koin (int): Jumlah koin yang dimiliki oleh karakter.
    * barang (list): List barang yang dimiliki oleh karakter.

**NPC (Non-Player Character):**
Turunan dari kelas Human.
* Atribut:
    * peran (string): Peran karakter NPC dalam permainan (Pemberi Misi, Penjual, Musuh, dll.).
    * hp (int): Menyimpan jumlah hit points (HP) karakter NPC.

**Quest:**
* Atribut:
    * deskripsi (string): Deskripsi dari quest yang diberikan.
    * hadiah (string): Hadiah yang diberikan setelah menyelesaikan quest.

**Pemain (Player):**
* Atribut:
    * namaPemain (string): Nama pemain dalam permainan.
    * character (list): List karakter yang dimiliki oleh pemain.


## Alur Program
* Dalam Program yang dibuat dengan inisialisasi karakter dan objek, seperti:
    * Membuat objek Tas untuk setiap karakter pemain dengan atribut yang telah ditentukan sebelumnya.
    * Membuat objek NPC dengan peran yang berbeda-beda.
    * Membuat objek Quest dengan deskripsi dan hadiah tertentu.
    * Membuat objek Pemain yang memiliki karakter tertentu.

* Didalam program ini terdapat interaksi antara karakter dan objek, seperti :
    * Karakter pemain dapat mengambil atau menyelesaikan quest yang diberikan oleh NPC.
    * Karakter pemain dapat menyerang karakter NPC.
    * Karakter NPC juga dapat menyerang karakter pemain.
    * Karakter pemain dapat memberikan atau menerima penyembuhan (heal) dari karakter lain.

* Menampilkan informasi yang mungkin berguna untuk pemain, dimana dapat melacak perkembangan dan kondisi karakter serta NPC yang ada di dalam game.

* Contoh implementasi fungsinya, seperti :
    * Fungsi-fungsi seperti attack, heal, take_quest, dan give_quest diimplementasikan dalam kode untuk mendukung interaksi antara karakter dan objek.
    * bertujuan agar karakter dalam permainan untuk saling berinteraksi sesuai dengan peran dan tujuan mereka dalam permainan.


## Dokumentasi Program
![Dok1](<Screenshot 2024-03-07 234232.png>)
![Dok2](<Screenshot 2024-03-07 234248.png>)
![Dok3](<Screenshot 2024-03-07 234258.png>)