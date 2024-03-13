import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
from pytesseract import pytesseract

class ImageTextExtractorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Convert Image - Qu")

        # Define path to Tesseract executable
        path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pytesseract.tesseract_cmd = path_to_tesseract

        # Define path to image (replace with your image path)
        path_to_image = 'd_imageconvert.jpg'

        # Open image with PIL
        img = Image.open(path_to_image)

        # Extract text from image
        text = pytesseract.image_to_string(img)

        # Create a Text widget to display the extracted text
        self.text_widget = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=20)
        self.text_widget.pack(padx=10, pady=10)
        self.text_widget.insert(tk.END, text)

def main():
    root = tk.Tk()
    app = ImageTextExtractorApp(root)

    # ICON
    image_icon = tk.PhotoImage(file="b_iconconvertimage.png")
    root.iconphoto(True, image_icon)

    root.mainloop()

if __name__ == "__main__":
    main()
