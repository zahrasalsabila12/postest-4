DaftarMakanan = {
    'Tteokbokki'    : 15000,
    'Kimbap'        : 30000,
    'Bibimbap'      : 55000,
    'Jajangmyeon'   : 35000,
    'Bulgogi'       : 150000,    
}
DaftarMinuman = {
    'Banana Milk'   : 15000,
    'Yuja Cha'      : 10000,
    'Ice Americano' : 25000,
    'Daechu Tea'    : 10000,   
}
Harga = []
def menu(): #daftar menu
    print ('''
=========================================
      Selamat datang di Korean Cafe   
=========================================
Daftar Menu Makanan:
-----------------------------------------
    ''')
    for (key,value) in DaftarMakanan.items() :
        print(key,'- Rp', value)
    print ('''
=========================================
Daftar Menu Minuman:
-----------------------------------------
    ''')
    for (key,value) in DaftarMinuman.items() :
        print(key,'- Rp', value)
    print ('''
=========================================
    ''')
def create_menu(): #program admin
    key1 = str(input('Masukkan nama menu makanan yang ingin Anda buat: '))
    value1 = int(input('Masukkan harga menu makanan yang ingin Anda buat: Rp '))
    DaftarMakanan.update({key1:value1})
    print ('''
=========================================
     Menu Baru Berhasil Ditambahkan
=========================================
        ''')
def create_minuman():
    key2 = str(input('Masukkan nama menu minuman yang ingin Anda buat: '))
    value2 = int(input('Masukkan harga menu minuman yang ingin Anda buat: Rp '))
    DaftarMinuman.update({key2:value2})
    print ('''
=========================================
    Minuman Baru Berhasil Ditambahkan
=========================================
            ''')
def update_menu(): #program admin
        Makanan = str(input('Masukkan nama makanan pilihan Anda: '))
        update1  = int(input('Masukkan update harga: Rp '))
        DaftarMakanan[Makanan] = update1
        print('''
=========================================
     Harga Menu Berhasil Diupdate
=========================================
        ''')
def update_minuman():
        Minuman = str(input('Masukkan nama minuman pilihan Anda: '))
        update2 = int(input('Masukkan update harga: Rp '))
        DaftarMinuman[Minuman] = update2
        print('''
=========================================
     Harga Menu Berhasil Diupdate
=========================================        
        ''')
def hapus_menu(): #program admin
        makanan = str(input('Masukkan nama menu makanan yang ingin Anda hapus: '))
        del DaftarMakanan[makanan]
        print('''
=========================================
    Menu Makanan Berhasil Anda Hapus
=========================================        
        ''')
def hapus_minuman():
        minuman = str(input('Masukkan nama menu minuman yang ingin Anda hapus: '))
        del DaftarMinuman[minuman]
        print('''
=========================================
    Menu Minuman Berhasil Anda Hapus
=========================================        
        ''')
def Admin(): #program admin
    while True:
        print('''
Menu Pilihan
---------------------------------------------
[1] Tampilkan Menu
[2] Tambahkan Menu
[3] Update Harga Menu
[4] Delete Menu
[5] Keluar
---------------------------------------------
    ''')
    
        pilihan = int(input('Masukkan nomor menu pilihan Anda: '))
        if pilihan == 1:
            menu()
        elif pilihan == 2:
            while True:
                print('''
====================================
Pilih daftar Menu yang di Inginkan : 
[1] Menu Makanan
[2] Menu Minuman
[3] Exit
====================================
            ''')
                x = str(input("Masukkan Nomor menu yang ingin ditambahkan : "))
                if x == '1':
                    create_menu()
                elif x == "2":
                    create_minuman()
                elif x == '3':
                    print('''
=========================================
Tekan [Enter] untuk Kembali Ke Menu Admin
=========================================
''')
                    input("")
                    break
                else:
                    print("\nMaaf Pilihan anda masukkan tidak valid\n")
            
        elif pilihan == 3:
            while True:
                print('''
=====================================
Pilih daftar Menu yang akan di Update : 
[1] Menu Makanan
[2] Menu Minuman
[3] Exit
=====================================
            ''')
                x = str(input("Masukkan Nomor menu yang ingin ditambahkan : "))
                if x == '1':
                    update_menu()
                elif x == '2':
                    update_minuman()
                elif x == '3':
                    print('''
=========================================
Tekan [Enter] untuk Kembali Ke Menu Admin
=========================================
''')
                    input("")
                    break
                else:
                    print("\nMaaf Pilihan anda masukkan tidak valid\n")
        elif pilihan == 4:
            while True:
                print('''
=====================================
Pilih daftar Menu yang akan di Hapus : 
[1] Menu Makanan
[2] Menu Minuman
[3] Exit
=====================================
            ''')
                x = int(input("Masukkan Nomor menu yang ingin ditambahkan : "))
                if x == 1:
                    hapus_menu()
                elif x == 2:
                    hapus_minuman()
                elif x == 3:
                    print('''
=========================================
Tekan [Enter] untuk Kembali Ke Menu Admin
=========================================
''')
                    input("")
                    break
                else:
                    print("\nMaaf Pilihan anda masukkan tidak valid\n")
        elif pilihan == 5:
            print('Anda telah keluar')
            print('====================')
            break
        else:
            print('''
=======================================
Perintah yang anda masukkan tidak valid
=======================================
            ''')
def bayar(jumlahtotal):
    x = int(input("Nominal Pembayaran: Rp"))
    kembalian = x - jumlahtotal
    if kembalian >= 0:
        print("Kembalian: Rp%i" %kembalian)
    else:
        print("Uang Untuk Pembayaran Kurang!")
        bayar()    
def Total(diskon): #program kasir
    subharga = sum(Harga)
    jumlahtotal = int(subharga - diskon)
    print("Total Pembelian Anda : Rp. ", jumlahtotal)
    bayar(jumlahtotal)
def Diskon(Harga): #diskon
    Hargatotal = sum(Harga)
    hari = str(input('Masukkan hari untuk mendapatkan diskon [cth: Senin]: '))
    if hari == 'Senin':
        print('''
------------------------------------------------
*SELAMAT ANDA MENDAPAT DISKON SENIN CERIA*
              SEBESAR 10 %
------------------------------------------------
            ''')
        diskon = int(Hargatotal * 10/100)
        Total(diskon)
    elif hari == 'Minggu':
        print('''
---------------------------------------------------
*SELAMAT ANDA MENDAPAT DISKON MINGGU BAHAGIA*
              SEBESAR 25 %
---------------------------------------------------
            ''')
        diskon = int(Hargatotal * 25/100)
        Total(diskon)
    else :
        print('''
------------------------------------------------
      xxxx MAAF HARI INI TIDAK ADA xxxx
                   DISKON
------------------------------------------------
            ''')
        diskon = 0
        Total(diskon)
def User(): #program user/kasir
    menu()
    pilih = str(input('Pilih Jenis Menu [Makanan/Minuman]: '))
    if pilih == 'Makanan':
        makanan = DaftarMakanan[input('Nama makanan: ')]
        jumlah1 = int(input('Jumlah pesanan: '))
        Harga1 = jumlah1 * makanan
        print("Jumlah Makanan : ", Harga1)
        Harga.append(Harga1)
        pesan = str(input('Ingin pesan lagi? [Y/T]: '))
        if pesan == 'Y':
            User()
        else:
            Diskon(Harga)
    elif pilih == 'Minuman':
        minuman = DaftarMinuman[input('Nama minuman: ')]
        jumlah2 = int(input('Jumlah pesanan: ')) 
        Harga2 = jumlah2 * minuman
        print("Jumlah Minuman : ", Harga2)
        Harga.append(Harga2)
        pesan = str(input('Ingin pesan lagi? [Y/T]: '))
        if pesan == 'Y':
            User()
        else:
            Diskon(Harga)
    else:
        print('''
=========================================
    Maaf Penulisan Pilihan yang Anda
          Masukkan Tidak Valid
=========================================
        ''')
        User()

loop = 1
while loop == 1 :
    print ('''
=========================================
|   Selamat Datang di Menu Registrasi   |
|       Program Kasir Korean Caffe      |
=========================================
>>> Silahkan Login :

    ''')
    username = str(input('username: '))
    pengguna = str(input('Anda ingin masuk sebagai? [Admin/User]: '))
    password = str(input('Masukkan password: '))
    if pengguna == 'Admin' and password == '063' :
        print('Admin: ',username)
        Admin()
    elif pengguna == 'User' and password == '210' :
        print('User: ',username)
        User()
        yes = True
        while yes == True:
            berhenti = str(input("Kembali ke menu kasir? [Y/N] : "))
            if berhenti == "Y" or berhenti == "yes" or berhenti == "y":
                Harga.clear()
                User()
                yes = True
            elif berhenti == "N" or berhenti == "No" or berhenti == "n":
                print("Terima Kasih Telah Menggunakan Program Kasir")
                break
    else:
        print('!Maaf Pengguna/Password anda tidak Valid!')