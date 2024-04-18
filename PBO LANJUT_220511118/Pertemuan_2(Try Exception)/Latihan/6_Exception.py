import math

def hitung_luas_lingkaran(jari_jari):
    try:
        if jari_jari <= 0:
            raise ValueError("Jari-jari harus lebih besar dari 0")
        else:
            luas = math.pi * (jari_jari ** 2)
            return luas
    except ValueError as ve:
        return str(ve)

jari_jari = float(input("Masukkan jari-jari lingkaran: "))

hasil = hitung_luas_lingkaran(jari_jari)
print("Luas lingkaran:", hasil)
