import tkinter as tk
from tkinter import Frame, Label, Button, Menu, messagebox
from FrmLogin import FormLogin
from FrmPelanggan import *
from FrmCamera import *
from FrmTransaksi import *
from FrmCatatan_order import *
from PIL import Image, ImageTk

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x680")
        self.root.title("Camera-Qu")
        self.root.configure(bg='light grey')
        self.logged_in = False

        # Creating a menu bar
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)
        
        # Users menu
        self.login_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.login_menu.add_command(label="Login", command=self.open_login_form)
        self.menu_bar.add_cascade(label="Login", menu=self.login_menu)

        # Image Label
        self.image_label = Label(root)
        self.image_label.pack(fill="both", expand=True)
        self.image_label.bind("<Configure>", self.update_image)  # Call function when window is resized

    def open_login_form(self):
        top_level = tk.Toplevel(self.root)
        login_form = FormLogin(top_level, "Form Login ", self.login_callback)

    def open_pelanggan_form(self):
        if self.logged_in:
            top_level = tk.Toplevel(self.root)
            open_pelanggan_form = FormPelanggan(top_level, "Form Pelanggan")  # Pass the title
        else:
            messagebox.showerror("Access Denied", "Please log in first.")
            
    def open_camera_form(self):
        if self.logged_in:
            top_level = tk.Toplevel(self.root)
            open_camera_form = FormCamera(top_level, "Form Camera")  # Pass the title
        else:
            messagebox.showerror("Access Denied", "Please log in first.")
            
    def open_transaksi_form(self):
        if self.logged_in:
            top_level = tk.Toplevel(self.root)
            open_transaksi_form = FormTransaksi(top_level, "Form Transaksi")  # Pass the title
        else:
            messagebox.showerror("Access Denied", "Please log in first.")

    def open_catatan_order_form(self):
        if self.logged_in:
            top_level = tk.Toplevel(self.root)
            open_catatan_order_form = FormCatatan_order(top_level, "Form Catatan Order")  # Pass the title
        else:
            messagebox.showerror("Access Denied", "Please log in first.")
        
    def login_callback(self, result):
        if result:  # If login successful
            # messagebox.showinfo("Login Successful", "Welcome!")
            self.logged_in = True
            self.login_menu.entryconfig("Login", state="disabled")  # Disable login menu after successful login
            self.create_file_menu()  # Create the "File" menu after login
        else:
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

    def create_file_menu(self):
        # Create the "File" menu after successful login
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Form Data Pelanggan", command=self.open_pelanggan_form)
        self.file_menu.add_command(label="Form Data Camera", command=self.open_camera_form)
        self.file_menu.add_command(label="Form Data Transaksi", command=self.open_transaksi_form)
        self.file_menu.add_command(label="Form Catatan Order", command=self.open_catatan_order_form)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

    def update_image(self, event):
        # Function to update image display
        window_width = event.width
        window_height = event.height
        image = Image.open('bgcamera.jpeg')  # Replace with your image path
        resized_image = image.resize((window_width, window_height), Image.BILINEAR)  # Using BILINEAR for interpolation
        photo = ImageTk.PhotoImage(resized_image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    dashboard = Dashboard(root)
    icon = tk.PhotoImage(file="iconcamera.png")  
    root.iconphoto(True, icon)
    root.mainloop() 