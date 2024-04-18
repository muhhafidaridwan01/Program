def kali_angka():
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Maaf, input yang Anda masukkan bukan angka.")
    else:
        hasil = angka1 * angka2
        print("Hasil perkalian:", hasil)

kali_angka()
