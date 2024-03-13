print("===Konversi Suhu Reamur===")

# Entry
suhu = input("Masukkan suhu dalam Reamur: ")

# Rumus
K = 5/4 * float(suhu) + 273
C =  5/4 * float(suhu) 
F =  (9/4 * float(suhu)) + 32

# Output
print(suhu + " Reamur sama dengan")
print(str(K) + " Kelvin")
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")