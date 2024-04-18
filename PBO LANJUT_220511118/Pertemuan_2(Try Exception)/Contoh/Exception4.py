try:
    f = open("file.txt", "r")
    
except FileNotFoundError:
    print("File tidak ditemukan")