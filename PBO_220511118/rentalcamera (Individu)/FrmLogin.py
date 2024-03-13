import tkinter as tk
from tkinter import Frame, Label, Entry, Button, messagebox
from Users import Users

class FormLogin:
    
    def __init__(self, parent, title, update_main_window):
        self.parent = parent       
        self.update_main_window = update_main_window 
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack()

        # diatur agar tampil di tengah layar
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()
        x = (screen_width - 250) // 2
        y = (screen_height - 150) // 2
        width = 250
        height = 150
        self.parent.geometry(f"{width}x{height}+{x}+{y}")

        # Label
        Label(mainFrame, text='Email:').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtEmail = Entry(mainFrame) 
        self.txtEmail.grid(row=0, column=1, padx=5, pady=5) 
        

        Label(mainFrame, text='Password:').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtPassword = Entry(mainFrame, show='*') 
        self.txtPassword.grid(row=1, column=1, padx=5, pady=5) 

        # Button
        self.btnSubmit = Button(mainFrame, text='Submit', command=self.onSubmit, width=10)
        self.btnSubmit.grid(row=2, column=0, padx=10, pady=5)
        self.btnCancel = Button(mainFrame, text='Cancel', command=self.onKeluar, width=10)
        self.btnCancel.grid(row=2, column=1, padx=10, pady=10)
      
                 
    def onSubmit(self, event=None):
        email = self.txtEmail.get()
        password = self.txtPassword.get()
                
        obj = Users()
        val = obj.Validasi(email, password)
        C = val[1]
        if C:
            self.update_main_window(val)
            messagebox.showinfo("Login", "Login Berhasil!")
            self.parent.destroy()
        else:
            messagebox.showwarning("Login Gagal", "Email atau password salah.")
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    def update_main_window(result):
        print(result)

    root = tk.Tk()
    aplikasi = FormLogin(root, "Form Login", update_main_window)
    icon = tk.PhotoImage(file="iconlogin.png")  
    root.iconphoto(True, icon)
    root.mainloop()
