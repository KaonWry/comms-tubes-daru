
print("=====================================")

NamaPengguna = ['Kannitha', 'Alfi', 'Zisqow', 'Daru', 'Nadya']
PinPengguna = ['323', '039', '271', '123', '059']
TabunganPengguna = [20000, 30000, 20000, 40000, 10000]
Saldo = 0
TarikTunai = 0
Transfer = 0
Jumlah = 0
Counter1 = 1
Counter2 = 5
i = 0

# Agar program berjalan dengan baik, masukkan input seperti di bawah.
while True:
    # os.system("cls")
    print("                                        ")
    print(" ----Selamat datang di Bank Ganesha---- ")
    print("========================================")
    print("=<< 1. Buka Rekening Baru            >>=")
    print("=<< 2. Tarik Tunai                   >>=")
    print("=<< 3. Setor Tunai                   >>=")
    print("=<< 4. Transfer                      >>=")
    print("=<< 5. List Nasabah dan Info         >>=")
    print("=<< 6. Keluar                        >>=")
    print("========================================")
    print("                                        ")
    # Pilih nomor dari data di atas
    PilihNomor = input("Pilih nomor dari menu di atas: ")
    if PilihNomor == "1":
        print("Buka rekening baru")
        # Membatasi rekening yang bisa dibuat oleh user.
        NomorPengguna = eval(input("Jumlah rekening yang akan dibuat: "))
 
        i = i + NomorPengguna
        # Membatasi pembuatan rekening menjadi paling banyak 7.
        if i > 7:
            print("\n")
            print("Jumlah rekening terlalu tinggi atau rendah, masukkan jumlah baru.")
            i = i - NomorPengguna
        else:
            # While loop akan bekerja sesuai dengan jumlah akun yang diinput di atas.
            while Counter1 <= i:
                # Data yang dimasukkan akan otomatis masuk ke daftar nasabah.
                Nama = input("Masukkan Nama Lengkap: ")
                NamaPengguna.append(Nama)
                pin = str(input("Masukkan pin rekening: "))
                PinPengguna.append(pin)
                Jumlah = 0
                Saldo = eval(input("Masukkan tabungan awal rekening: Rp"))
                Jumlah = Jumlah + Saldo
                TabunganPengguna.append(Jumlah)
                print("\nNama=", end=" ")
                print(NamaPengguna[Counter2])
                print("Pin=", end=" ")
                print(PinPengguna[Counter2])
                print("Jumlah=", end=" ")
                print(TabunganPengguna[Counter2], end=" ")
    
                Counter1 = Counter1 + 1
                Counter2 = Counter2 + 1
                print("\nNama Anda sudah dimasukkan ke daftar nasabah Bank Ganesha")
                print("Pin Anda sudah terdaftar dalam sistem")
                print("Jumlah tabungan Anda sudah terdaftar dalam sistem")
                print("!!!Rekening berhasil dibuat!!!")
                print("\n")
                print("Nama Anda sudah terdaftar dalam daftar nasabah Bank Ganesha")
                print(NamaPengguna)
                print("\n")
                print("Warning! Jangan lupakan nama dan pin dari rekening anda!")
                print("========================================")
                # Kembali ke menu awal.
        mainMenu = input("Tekan enter untuk kembali ke menu awal atau keluar")
    elif PilihNomor == "2":
        j = 0
        print("Penarikan Tunai")
        # Fungsi while loop akan memeriksa nama dan pin akun, bila memasukkan nama/pin yang salah, penarikan tidak akan bekerja.
        while j < 1:
            k = -1
            Nama = input("Masukkan nama: ")
            pin = input("Masukkan pin: ")
            # while loop akan terus bekerja bila variabel k lebih kecil dari panjang daftar NamaPengguna.
            # Daftar NamaPengguna.
            while k < len(NamaPengguna) - 1:
                k = k + 1
                # Hanya akan terjadi bila nama dan pin cocok seperti yang diinput di awal
                if Nama == NamaPengguna[k]:
                    if pin == PinPengguna[k]:
                        j = j + 1
                        # Line di bawah akan menunjukan saldo.
                        print("Saldo saat ini: Rp", end=" ")
                        print(TabunganPengguna[k], end=" ")
                        Jumlah = (TabunganPengguna[k])
                        # Line di bawah akan mengambil jumlah nominal yang ditarik.
                        TarikTunai = eval(input("\nMasukkan nominal penarikan: Rp"))
                        # If akan memeriksa apa nominal penarikan lebih besar atau kecil dari saldo yang dimiliki.
                        if TarikTunai > Jumlah:
                            # Saldo yang dimasukkan akan ditarik.
                            Saldo = eval(input(
                                "Tolong masukkan nominal yang lebih kecil untuk penarikan: "))
                            # Saldo
                            Jumlah = Jumlah + Saldo
                            print("Saldo saat ini: Rp", end=" ")
                            print(Jumlah, end=" ")
                            Jumlah = Jumlah - TarikTunai
                            print("-\n")
                            print("!!!Penarikan Sukses!!!")
                            TabunganPengguna[k] = Jumlah
                            print("Saldo saat ini: Rp", Jumlah, end=" ")
                        else:
                            # Else akan melakukan TarikTunai apabila jumlah saldo awal lebih besar dari pada saldo yang akan ditarik.
                            Jumlah = Jumlah - TarikTunai
                            # Kondisi dan saldo setelah penarikan berhasil.
                            print("\n")
                            print("!!!Penarikan Sukses!!!")
                            TabunganPengguna[k] = Jumlah
                            print("Saldo saat ini: Rp",Jumlah, end=" ")
            if j < 1:
                # Bila user memasukkan nama dan pin yang salah, program akan menolak.
                print("Nama dan pin tidak sesuai!\n")
                break
            # Kembali ke men awal.
        mainMenu = input("\nTekan enter untuk kembali ke menu awal atau keluar")
    elif PilihNomor == "3":
        print("Penyetoran tunai")
        n = 0
        # While loop akan bekerja bila nama dan pin salah.
        while n < 1:
            k = -1
            Nama = input("Masukkan nama: ")
            pin = input("Masukkan pin: ")
            # wWhile loop akan bekerja sampai menemukan pengguna yang benar.
            while k < len(NamaPengguna) - 1:
                k = k + 1
                # Dua fungsi if di bawah adalah untuk menemukan pin dan nama yang benar. 
                if Nama == NamaPengguna[k]:
                    if pin == PinPengguna[k]:
                        n = n + 1
                        # Menunjukkan jumlah saldo.
                        print("Saldo saat ini: Rp", end=" ")
                        print(TabunganPengguna[k], end=" ")
                        Jumlah = (TabunganPengguna[k])
                        # Saldo akan dikurangi.
                        Saldo = eval(input("\nMasukkan nominal penyetoran: "))
                        Jumlah = Jumlah + Saldo
                        TabunganPengguna[k] = Jumlah
                        print("\n")
                        print("!!!Penyetoran sukses!!!")
                        print("Saldo saat ini: Rp", Jumlah, end=" ")
            if n < 1:
                print("Nama dan pin tidak sesuai!\n")
                break
        mainMenu = input("\nTekan enter untuk kembali ke menu awal atau keluar")
    elif PilihNomor == "4":
        j = 0
        print("Transfer Uang")
        while j < 1:
            k = -1
            Nama = input("Masukkan nama: ")
            pin = input("Masukkan pin: ")
            RekeningP = input("Masukkan nomor rekening penerima: ")
            # While loop akan terus bekerja bila variabel k lebih kecil dari panjang daftar NamaPengguna.
            while k < len(NamaPengguna) - 1:
                k = k + 1
                # Jika pin dan nama sesuai.
                if Nama == NamaPengguna[k]:
                    if pin == PinPengguna[k]:
                        j = j + 1
                        print("Saldo saat ini: ", end=" ")
                        print(TabunganPengguna[k], end=" ")
                        Jumlah = (TabunganPengguna[k])
                        Transfer = eval(input("\nMasukkan nominal yang ingin ditransfer: Rp"))
                        # If akan mencari tahu apabila jumlah yang ditrasnfer lebih besar dari saldo awal.
                        if Transfer > Jumlah:
                            Saldo = eval(input(
                                "Tolong masukkan nominal yang lebih besar karena nominal yang Anda masukkan terlalu kecil untuk penarikan: "))

                            Jumlah = Jumlah + Saldo
                            print("Saldo saat ini: Rp", end=" ")
                            print(Jumlah, end=" ")

                            Jumlah = Jumlah - Transfer
                            print("-\n")
                            print("!!!Transfer Sukses!!!")
                            TabunganPengguna[k] = Jumlah
                            print("Saldo saat ini: Rp", Jumlah, end=" ")
                        else:
                            Jumlah = Jumlah - Transfer
                            # Value update.
                            print("\n")
                            print("!!!Transfer Sukses!!!")
                            TabunganPengguna[k] = Jumlah
                            print("Saldo saat ini: Rp", Jumlah, end=" ")
            if j < 1:
                # Kalau nama dan pin tidak sesuai, program akan menolak.
                print("Nama dan pin tidak sesuai!\n")
                break
    elif PilihNomor == "5":
        k = 0
        print("Daftar nama nasabah dan info dicantumkah di daftar di bawah ini: ")
        print("\n")
        while k <= len(NamaPengguna) - 1:
            print("-> Nasabah =", NamaPengguna[k])
            print("-> Jumlah =", TabunganPengguna[k], end=" ")
            print("\n")
            k = k + 1
        mainMenu = input("\nTekan enter untuk kembali ke menu awal atau keluar")
    elif PilihNomor == "6":
        # Akan ditunjukan bila nasabah ingin keluar.
        print("""
    -------------------------------------
   |    Terima kasih telah mempercayai   |
   |             BANK GANESHA            |
    -------------------------------------
        """)
        break
    else:
        # Fungsi else akan bekerja apabila fungsi yang salah dipilih.
        print("Opsi tidak ada!")
        print("Tolong coba lagi!")
        # Kembali ke menu
        mainMenu = input("\nTekan enter untuk kembali ke menu awal atau keluar")
