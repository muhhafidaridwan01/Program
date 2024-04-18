def tambah():
    try:
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Input harus berupa angka.")
    else:
        if num1 == "" or num2 == "":
            print("Error: Input tidak boleh kosong.")
        else:
            hasil = num1 + num2
            print("Hasil penjumlahan:", hasil)

tambah()
