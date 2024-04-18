def hitung_volume_balok(panjang, lebar, tinggi):
    try:
        if panjang <= 0 or lebar <= 0 or tinggi <= 0:
            raise ValueError("Panjang, lebar, dan tinggi harus lebih besar dari 0")
        else:
            volume = panjang * lebar * tinggi
            return volume
    except ValueError as ve:
        return str(ve)

panjang = float(input("Masukkan panjang balok: "))
lebar = float(input("Masukkan lebar balok: "))
tinggi = float(input("Masukkan tinggi balok: "))

hasil = hitung_volume_balok(panjang, lebar, tinggi)
print("Volume balok:", hasil)
