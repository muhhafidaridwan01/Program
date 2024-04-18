try:
    a = [1, 2, 3]
    b = int(input ("Masukkan Nomor Index [0,1,2]: "))
    print(a[b])
except IndexError:
    print("Indeks diluar rentang array")
except Exception as e:
    print("Terjadi Kesalahan:", e)