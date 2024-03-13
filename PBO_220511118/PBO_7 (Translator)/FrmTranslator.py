import tkinter as tk
from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W, StringVar, OptionMenu
from googletrans import Translator

class FrmTranslator:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("505x250")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, bg='lightgray')  # Set background color for the mainFrame
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # pasang Label
        Label(mainFrame, text='Masukkan teks:', bg='lightgray').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text='Bahasa Asal:', bg='lightgray').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text='Hasil Terjemahan (English):', bg='lightgray').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text='Hasil Terjemahan (Sundanese):', bg='lightgray').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text='Hasil Terjemahan (Japanese):', bg='lightgray').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        
        # pasang textbox
        self.txtSumber = Entry(mainFrame, width=50) 
        self.txtSumber.grid(row=0, column=1, padx=5, pady=5)

        # Dropdown menu untuk bahasa asal
        self.selected_source_lang = StringVar()
        self.selected_source_lang.set("id")  # Default language: Indonesian
        source_lang_options = ["id", "en", "su", "ja"]  # Indonesian, English, Sundanese, Japanese
        self.source_lang_menu = OptionMenu(mainFrame, self.selected_source_lang, *source_lang_options)
        self.source_lang_menu.grid(row=1, column=1, padx=5, pady=5)

        self.txtHasilEnglish = Entry(mainFrame, width=50) 
        self.txtHasilEnglish.grid(row=3, column=1, padx=5, pady=5)

        self.txtHasilSundanese = Entry(mainFrame, width=50) 
        self.txtHasilSundanese.grid(row=4, column=1, padx=5, pady=5)

        self.txtHasilJapanese = Entry(mainFrame, width=50) 
        self.txtHasilJapanese.grid(row=5, column=1, padx=5, pady=5)

        # Pasang Button
        self.btnTranslate = Button(mainFrame, text='Translate!',
            command=self.onTranslate)
        self.btnTranslate.grid(row=2, column=1, padx=5, pady=5) 

    def onTranslate(self):
        # membuat instance object
        penterjemah = Translator()

        # menterjemahkan ke bahasa Inggris
        hasil_english = penterjemah.translate(self.txtSumber.get(), src=self.selected_source_lang.get(), dest='en') 
       
        # menterjemahkan ke bahasa Sunda
        hasil_sundanese = penterjemah.translate(self.txtSumber.get(), src=self.selected_source_lang.get(), dest='su') 

        # menterjemahkan ke bahasa Jepang
        hasil_japanese = penterjemah.translate(self.txtSumber.get(), src=self.selected_source_lang.get(), dest='ja') 

        # membersihkan textbox hasil sebelum menampilkan hasil terjemahan
        self.txtHasilEnglish.delete(0, END)
        self.txtHasilSundanese.delete(0, END)
        self.txtHasilJapanese.delete(0, END)

        # menampilkan hasil terjemahan
        self.txtHasilEnglish.insert(END, hasil_english.text)
        self.txtHasilSundanese.insert(END, hasil_sundanese.text)
        self.txtHasilJapanese.insert(END, hasil_japanese.text)

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTranslator(root, "Program Translator | 220511118")
    
root.mainloop()
