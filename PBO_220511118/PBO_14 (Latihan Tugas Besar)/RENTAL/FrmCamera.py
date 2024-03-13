# filename : FrmCamera.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Camera import Camera
# pip install tkcalendar
from tkcalendar import Calendar, DateEntry
class FormCamera:   
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
         # varchar 
        Label(mainFrame, text='KODE_KAMERA:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox KODE_KAMERA
        self.txtKODE_KAMERA = Entry(mainFrame) 
        self.txtKODE_KAMERA.grid(row=0, column=1, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='NOMOR_KTP:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox NOMOR_KTP
        self.txtNOMOR_KTP = Entry(mainFrame) 
        self.txtNOMOR_KTP.grid(row=1, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='NAMA_PELANGGAN:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA_PELANGGAN
        self.txtNAMA_PELANGGAN = Entry(mainFrame) 
        self.txtNAMA_PELANGGAN.grid(row=2, column=1, padx=5, pady=5)
                
         # date 
        Label(mainFrame, text='TANGGAL:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL
        self.txtTANGGAL = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGAL.grid(row=3, column=1, padx=5, pady=5)
                    
         # int 
        Label(mainFrame, text='TARIF_PERJAM:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        # Textbox TARIF_PERJAM
        self.txtTARIF_PERJAM = Entry(mainFrame) 
        self.txtTARIF_PERJAM.grid(row=4, column=1, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='TOTAL_BAYAR:').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        # Textbox TOTAL_BAYAR
        self.txtTOTAL_BAYAR = Entry(mainFrame) 
        self.txtTOTAL_BAYAR.grid(row=5, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='STATUS_BAYAR:').grid(row=6, column=0, sticky=W, padx=5, pady=5)
        # Textbox STATUS_BAYAR
        self.txtSTATUS_BAYAR = Entry(mainFrame) 
        self.txtSTATUS_BAYAR.grid(row=6, column=1, padx=5, pady=5)
                
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','kode_kamera','nomor_ktp','nama_pelanggan','tanggal','tarif_perjam','total_bayar','status_bayar')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('kode_kamera', text='kode_kamera')
        self.tree.column('kode_kamera', width="100")
        self.tree.heading('nomor_ktp', text='nomor_ktp')
        self.tree.column('nomor_ktp', width="100")
        self.tree.heading('nama_pelanggan', text='nama_pelanggan')
        self.tree.column('nama_pelanggan', width="100")
        self.tree.heading('tanggal', text='tanggal')
        self.tree.column('tanggal', width="100")
        self.tree.heading('tarif_perjam', text='tarif_perjam')
        self.tree.column('tarif_perjam', width="100")
        self.tree.heading('total_bayar', text='total_bayar')
        self.tree.column('total_bayar', width="100")
        self.tree.heading('status_bayar', text='status_bayar')
        self.tree.column('status_bayar', width="100")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtKODE_KAMERA.delete(0,END)
        self.txtKODE_KAMERA.insert(END,"")
                                
        self.txtNOMOR_KTP.delete(0,END)
        self.txtNOMOR_KTP.insert(END,"")
                                
        self.txtNAMA_PELANGGAN.delete(0,END)
        self.txtNAMA_PELANGGAN.insert(END,"")
                                
        self.txtTARIF_PERJAM.delete(0,END)
        self.txtTARIF_PERJAM.insert(END,"")
                                
        self.txtTOTAL_BAYAR.delete(0,END)
        self.txtTOTAL_BAYAR.insert(END,"")
                                
        self.txtSTATUS_BAYAR.delete(0,END)
        self.txtSTATUS_BAYAR.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data camera
        obj = Camera()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        obj = self.txt.get()
        obj = Camera()
        res = obj.getBy()
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def TampilkanData(self, event=None):
        obj = self.txt.get()
        obj = Camera()
        res = obj.getBy()
            
        self.txtKODE_KAMERA.delete(0,END)
        self.txtKODE_KAMERA.insert(END,obj.kode_kamera)
                                
        self.txtNOMOR_KTP.delete(0,END)
        self.txtNOMOR_KTP.insert(END,obj.nomor_ktp)
                                
        self.txtNAMA_PELANGGAN.delete(0,END)
        self.txtNAMA_PELANGGAN.insert(END,obj.nama_pelanggan)
                                
        self.txtTANGGAL.delete(0,END)
        self.txtTANGGAL.insert(END,obj.tanggal)
                                
        self.txtTARIF_PERJAM.delete(0,END)
        self.txtTARIF_PERJAM.insert(END,obj.tarif_perjam)
                                
        self.txtTOTAL_BAYAR.delete(0,END)
        self.txtTOTAL_BAYAR.insert(END,obj.total_bayar)
                                
        self.txtSTATUS_BAYAR.delete(0,END)
        self.txtSTATUS_BAYAR.insert(END,obj.status_bayar)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        kode_kamera = self.txtKODE_KAMERA.get()
        nomor_ktp = self.txtNOMOR_KTP.get()
        nama_pelanggan = self.txtNAMA_PELANGGAN.get()
        tanggal = self.txtTANGGAL.get()
        tarif_perjam = self.txtTARIF_PERJAM.get()
        total_bayar = self.txtTOTAL_BAYAR.get()
        status_bayar = self.txtSTATUS_BAYAR.get()       
        obj = Camera()
        obj.kode_kamera = kode_kamera
        obj.nomor_ktp = nomor_ktp
        obj.nama_pelanggan = nama_pelanggan
        obj.tanggal = tanggal
        obj.tarif_perjam = tarif_perjam
        obj.total_bayar = total_bayar
        obj.status_bayar = status_bayar
        if(self.ditemukan==True):
            res = obj.updateBy()
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        obj = self.txt.get()
        obj = Camera()
        obj = Camera
        if(self.ditemukan==True):
            res = obj.deleteBy()
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
 
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormCamera(root, "Aplikasi Data Camera")
    root.mainloop()