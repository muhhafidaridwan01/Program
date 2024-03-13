print("===Konversi Suhu Reamur===")
def get_kelvin(suhu):
    K = 5/4 * float(suhu) + 273
    return K

def get_celcius(suhu):
    C = 5/4 * float(suhu) 
    return C

def get_fahrenheit(suhu):
    F = (9/4 * float(suhu)) + 32
    return F

# Entry
suhu = input("Masukkan suhu Fahrenheit: ")

# Rumus
K = get_kelvin(suhu)
C = get_celcius(suhu)
F = get_fahrenheit(suhu)