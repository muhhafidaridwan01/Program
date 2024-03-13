
# filename : FrmPelanggan.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Pelanggan import Pelanggan
class FormPelanggan:   
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("515x400")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
         # varchar 
        Label(mainFrame, text='NAMA_PELANGGAN:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA_PELANGGAN
        self.txtNAMA_PELANGGAN = Entry(mainFrame) 
        self.txtNAMA_PELANGGAN.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNAMA_PELANGGAN.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # enum 
        Label(mainFrame, text='JK:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtJK = StringVar()
        CboJK = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJK) 
        CboJK.grid(row=1, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboJK['values'] = ('Laki-laki','Perempuan')
        CboJK.current()
        
         # int 
        Label(mainFrame, text='NOMOR_KTP:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Textbox NOMOR_KTP
        self.txtNOMOR_KTP = Entry(mainFrame) 
        self.txtNOMOR_KTP.grid(row=2, column=1, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='NOMOR_HP:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Textbox NOMOR_HP
        self.txtNOMOR_HP = Entry(mainFrame) 
        self.txtNOMOR_HP.grid(row=3, column=1, padx=5, pady=5)
                
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','nama_pelanggan','jk','nomor_ktp','nomor_hp')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='Id')
        self.tree.column('id', width="30")
        self.tree.heading('nama_pelanggan', text='Nama Pelanggan')
        self.tree.column('nama_pelanggan', width="120")
        self.tree.heading('jk', text='Jenis Kelamin')
        self.tree.column('jk', width="100")
        self.tree.heading('nomor_ktp', text='Nomor Ktp')
        self.tree.column('nomor_ktp', width="120")
        self.tree.heading('nomor_hp', text='Nomor Hp')
        self.tree.column('nomor_hp', width="120")
        # set tree position
        self.tree.place(x=0, y=150)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNAMA_PELANGGAN.delete(0,END)
        self.txtNAMA_PELANGGAN.insert(END,"")
                                
        self.txtJK.set("")
            
        self.txtNOMOR_KTP.delete(0,END)
        self.txtNOMOR_KTP.insert(END,"")
                                
        self.txtNOMOR_HP.delete(0,END)
        self.txtNOMOR_HP.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data pelanggan
        obj = Pelanggan()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        nama_pelanggan = self.txtNAMA_PELANGGAN.get()
        obj = Pelanggan()
        res = obj.getByNAMA_PELANGGAN(nama_pelanggan)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("Pemberitahuan", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("Peringatan", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def TampilkanData(self, event=None):
        nama_pelanggan = self.txtNAMA_PELANGGAN.get()
        obj = Pelanggan()
        res = obj.getByNAMA_PELANGGAN(nama_pelanggan)
            
        self.txtJK.set(obj.jk)
            
        self.txtNOMOR_KTP.delete(0,END)
        self.txtNOMOR_KTP.insert(END,obj.nomor_ktp)
                                
        self.txtNOMOR_HP.delete(0,END)
        self.txtNOMOR_HP.insert(END,obj.nomor_hp)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        nama_pelanggan = self.txtNAMA_PELANGGAN.get()
        jk = self.txtJK.get()
        nomor_ktp = self.txtNOMOR_KTP.get()
        nomor_hp = self.txtNOMOR_HP.get()       
        obj = Pelanggan()
        obj.nama_pelanggan = nama_pelanggan
        obj.jk = jk
        obj.nomor_ktp = nomor_ktp
        obj.nomor_hp = nomor_hp
        if(self.ditemukan==True):
            res = obj.updateByNAMA_PELANGGAN(nama_pelanggan)
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("Pemberitahuan", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("Peringatan", "Data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        nama_pelanggan = self.txtNAMA_PELANGGAN.get()
        obj = Pelanggan()
        obj.nama_pelanggan = nama_pelanggan
        if(self.ditemukan==True):
            res = obj.deleteByNAMA_PELANGGAN(nama_pelanggan)
            rec = obj.affected
        else:
            messagebox.showinfo("Peringatan", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("Pemberitahuan", "Data Berhasil dihapus")
        
        self.onClear()
 
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormPelanggan(root, "Form Data Pelanggan")
    
    icon = tk.PhotoImage(file="iconpelanggan.png")  
    root.iconphoto(True, icon)
    
    root.mainloop() 