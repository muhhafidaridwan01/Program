import pygame
from tkinter import *
from tkinter import filedialog

class MP3Player:
    def __init__(self, master):
        self.master = master
        self.master.title("Musik-Qu")
        self.master.geometry("300x200")
        
        image_icon = PhotoImage(file="b_iconmp3.png")
        self.master.iconphoto(True, image_icon)

        self.load_button = Button(self.master, text="Pilih & Putar Musiknya", command=self.load_file, height=1)
        self.load_button.pack(pady=20)

        self.play_button = Button(self.master, text="Mainkan & Bergoyanglah", command=self.play_music, state=DISABLED, height=1)
        self.play_button.pack(pady=20)

        self.stop_button = Button(self.master, text="Berhenti & Matikan Musiknya", command=self.stop_music, state=DISABLED, height=1)
        self.stop_button.pack(pady=20)

        self.music_file = None

    def load_file(self):
        self.music_file = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])

        if self.music_file:
            self.play_button.config(state=NORMAL)
            self.stop_button.config(state=NORMAL)

    def play_music(self):
        if self.music_file:
            pygame.mixer.init()
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = Tk()
    mp3_player = MP3Player(root)
    root.mainloop()
