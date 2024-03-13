# Study Kasus : Menganalisis Kata Dalam Kalimat

# Meminta pengguna untuk memasukkan sebuah kalimat
kalimat = input("Masukkan sebuah kalimat : ")

# Memecah kalimat menjadi kata-kata
kata_kata = kalimat.split()

# Menghitung jumlah kata dalam kalimat
jumlah_kata = len(kata_kata)

# Menampilkan hasil analisis
print("Kalimat yang Anda masukkan memiliki", jumlah_kata, "kata.")
print("Kata-kata dalam kalimat:")
for kata in kata_kata:
    print(kata)