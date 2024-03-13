# Study Kasus ; Membuat Kalkulator Sederhana
# Melakukan operasi penjumlahan, pengurangan, perkalian, dan Pembagian berdasarkan masukan dari user
# Kalkulator ini akan menggunakan kondisi untuk memutuskan operasi apa yang harus dilakukan.

print ("===KALKULATOR SEDERHANA ALA HAFID===")
# Meminta pengguna untuk memilih operasi
print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
pilihan = int(input("Masukkan nomor operasi yang dipilih: "))

# Meminta pengguna untuk memasukkan dua bilangan
bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))

# Memproses operasi sesuai dengan pilihan pengguna
if pilihan == 1:
    hasil = bilangan1 + bilangan2
    operasi = "Penjumlahan"
elif pilihan == 2:
    hasil = bilangan1 - bilangan2
    operasi = "Pengurangan"
elif pilihan == 3:
    hasil = bilangan1 * bilangan2
    operasi = "Perkalian"
elif pilihan == 4:
    if bilangan2 == 0:
        hasil = "Tidak dapat membagi dengan nol."
    else:
        hasil = bilangan1 / bilangan2
    operasi = "Pembagian"
else:
    hasil = "Pilihan operasi tidak valid"
    operasi = "Tidak Diketahui"

# Menampilkan hasil operasi
print(f"Hasil {operasi}: {hasil}")