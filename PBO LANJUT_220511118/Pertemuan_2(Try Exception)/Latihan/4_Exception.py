def hitung_luas_persegi_panjang(panjang, lebar):
    try:
        if panjang <= 0 or lebar <= 0:
            raise ValueError("Panjang dan lebar harus lebih besar dari 0")
        else:
            luas = panjang * lebar
            return luas
    except ValueError as ve:
        return str(ve)

panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

hasil = hitung_luas_persegi_panjang(panjang, lebar)
print("Luas persegi panjang:", hasil)
