def tambah_angka():
    try:
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))
    except ValueError:
        print("Maaf, input yang Anda masukkan bukan angka.")
    else:
        hasil = angka1 + angka2
        print("Hasil penjumlahan:", hasil)

tambah_angka()
