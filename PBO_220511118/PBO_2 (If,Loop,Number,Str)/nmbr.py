# Menentukan Bilangan Ganjil dan Genap

awal_banget = int(input("Masukkan angka awal: "))
akhir_banget = int(input("Masukkan angka akhir: "))

x = []
y = []
for i in range(awal_banget, akhir_banget+1):
    if i%2 == 0:
        x.append(i)
    if i%2 == 1:   
        y.append(i)
print("Angka genap: ", x)
print("Angka ganjil: ", y)
