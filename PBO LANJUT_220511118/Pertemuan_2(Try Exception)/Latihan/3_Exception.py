def bagi_angka():
    try:
        angka1 = float(input("Masukkan angka pembilang: "))
        angka2 = float(input("Masukkan angka penyebut: "))
        hasil = angka1 / angka2
    except ValueError:
        print("Maaf, input yang Anda masukkan bukan angka.")
    except ZeroDivisionError:
        print("Maaf, tidak dapat membagi dengan angka nol.")
    else:
        print("Hasil pembagian:", hasil)

bagi_angka()
