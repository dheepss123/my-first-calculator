# Definisi fungsi
def kalkulator():
    while True:
        print("Pilihan operasi matematika yang tersedia: ")
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian (*)")
        print("4. Pembagian (/)")
        print("Jika mau keluar dari aplikasi tulis perintah dbawah ini: ")
        print("stop")

        # Meminta user memilih operasi perhitungan
        pilihan = input("Masukkan bilangan operasi yang anda inginkan (1/2/3/4/5): ")

        if pilihan == 'stop':
            print("Terima kasih telah menggunakan kalkulator.")
            break  # Keluar dari loop jika pengguna memilih keluar

        if pilihan in ('1', '2', '3', '4'):
            angka1 = int(input("Masukkan angka pertama: "))
            angka2 = int(input("Masukkan angka kedua: "))

            if pilihan == '1':
                hasil = angka1 + angka2
            elif pilihan == '2':
                hasil = angka1 - angka2
            elif pilihan == '3':
                hasil = angka1 * angka2
            elif pilihan == '4':
                # Memeriksa pembagian dengan nol
                if angka2 != 0:
                    hasil = angka1 / angka2
                else:
                    hasil = "Tidak dapat membagi oleh nol"

            # Menampilkan hasil
            print("Hasil: ", hasil)
            
        else:
            print("Pilihan operasi tidak valid")

# Memanggil fungsi kalkulator
kalkulator()
