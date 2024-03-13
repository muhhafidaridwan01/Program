import tkinter as tk
from tkinter import *
from googletrans import Translator

class TranslatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Translator-Qu")

        # ICON
        image_icon = PhotoImage(file="b_icontranslator.png")
        self.master.iconphoto(True, image_icon)

        self.create_widgets()

    def create_widgets(self):
        # Frame utama
        frame = tk.Frame(self.master, padx=20, pady=20)
        frame.pack(padx=10, pady=10)

        # Label judul
        title_label = tk.Label(frame, text="Translator-Qu", font=('Helvetica', 16))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Label dan Entry untuk input teks
        label_entry = tk.Label(frame, text="Masukkan Teks ->")
        label_entry.grid(row=1, column=0, pady=10, sticky="w")

        self.input_entry = tk.Entry(frame, width=50)
        self.input_entry.grid(row=1, column=1, pady=10, padx=10)

        # Tombol untuk memulai terjemahan
        translate_button = tk.Button(frame, text="Terjemahkan", command=self.translate_text)
        translate_button.grid(row=2, column=1, pady=10, sticky="n")

        # Entry untuk menampilkan hasil terjemahan
        self.entry_en = tk.Entry(frame, width=50, state="readonly")
        self.entry_ja = tk.Entry(frame, width=50, state="readonly")
        self.entry_ko = tk.Entry(frame, width=50, state="readonly")

        self.entry_en.grid(row=3, column=1, pady=10, padx=10)
        self.entry_ja.grid(row=4, column=1, pady=10, padx=10)
        self.entry_ko.grid(row=5, column=1, pady=10, padx=10)

    def translate_text(self):
        text_to_translate = self.input_entry.get()

        if not text_to_translate:
            return

        translator = Translator()

        try:
            translation_en = translator.translate(text_to_translate, dest='en').text
            translation_ja = translator.translate(text_to_translate, dest='ja').text
            translation_ko = translator.translate(text_to_translate, dest='ko').text

            self.entry_en.config(state="normal")
            self.entry_en.delete(0, END)
            self.entry_en.insert(0, f"Inggris -> {translation_en}")
            self.entry_en.config(state="readonly")

            self.entry_ja.config(state="normal")
            self.entry_ja.delete(0, END)
            self.entry_ja.insert(0, f"Jepang -> {translation_ja}")
            self.entry_ja.config(state="readonly")

            self.entry_ko.config(state="normal")
            self.entry_ko.delete(0, END)
            self.entry_ko.insert(0, f"Korea -> {translation_ko}")
            self.entry_ko.config(state="readonly")

        except Exception as e:
            print(f"Error during translation: {e}")

def main():
    root = tk.Tk()
    app = TranslatorApp(root)

    # Menambahkan geometry
    root.geometry("500x300+100+100")

    root.mainloop()

if __name__ == "__main__":
    main()
