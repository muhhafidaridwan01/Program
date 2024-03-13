import tkinter as tk
from tkinter import messagebox

def save_schedule():
    schedule_data = entry_schedule.get()
    with open("jadwal_kuliah.txt", "a") as file:
        file.write(schedule_data + "\n")
    entry_schedule.delete(0, "end")
    messagebox.showinfo("Mantap boss", "Jadwal berhasil disimpan!")
    

def load_schedule():
    try:
        with open("jadwal_kuliah.txt", "r") as file:
            schedule_list = file.readlines()
            schedule_text.config(state="normal")
            schedule_text.delete(1.0, "end")
            for schedule in schedule_list:
                schedule_text.insert("end", schedule)
            schedule_text.config(state="disabled")
    except FileNotFoundError:
        messagebox.showinfo("Info", "Tidak ada jadwal yang tersimpan.")

app = tk.Tk()
app.title("Aplikasi Jadwal Kuliah Hafid ")

# Membuat label
label_nama = tk.Label(app, text="220511118 - MUHAMMAD HAFID ARIDWAN")
label_nama.pack(pady=10)

label_schedule = tk.Label(app, text="Masukkan Jadwal Kuliah:")
label_schedule.pack()

entry_schedule = tk.Entry(app, width=53)
entry_schedule.pack()

save_button = tk.Button(app, text="Simpan Jadwal", command=save_schedule)
save_button.pack(pady=10)

load_button = tk.Button(app, text="Muat Jadwal", command=load_schedule)
load_button.pack(pady=10)

schedule_text = tk.Text(app, height=10, width=40)
schedule_text.config(state="disable")
schedule_text.pack()

app.mainloop()