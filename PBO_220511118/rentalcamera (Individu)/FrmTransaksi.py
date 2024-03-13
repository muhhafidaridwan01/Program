
# filename : FrmTransaksi.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Transaksi import Transaksi
# pip install tkcalendar
from tkcalendar import Calendar, DateEntry
class FormTransaksi:   
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("1005x555")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # varchar 
        Label(mainFrame, text='NAMA PELANGGAN:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMEPELANGGAN
        self.txtNAMEPELANGGAN = Entry(mainFrame) 
        self.txtNAMEPELANGGAN.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNAMEPELANGGAN.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # enum 
        Label(mainFrame, text='BANYAK CAMERA:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtBANYAK_CAMERA = StringVar()
        CboBANYAK_CAMERA = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtBANYAK_CAMERA) 
        CboBANYAK_CAMERA.grid(row=1, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboBANYAK_CAMERA['values'] = ('1','2','3','4','5')
        CboBANYAK_CAMERA.current()
        
         # date 
        Label(mainFrame, text='TANGGAL:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL
        self.txtTANGGAL = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGAL.grid(row=2, column=1, padx=5, pady=5)
                    
         # enum 
        Label(mainFrame, text='TARIF PERJAM:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtTARIF_PERJAM = StringVar()
        CboTARIF_PERJAM = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtTARIF_PERJAM) 
        CboTARIF_PERJAM.grid(row=3, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboTARIF_PERJAM['values'] = ('10000','20000','30000','40000','50000')
        CboTARIF_PERJAM.current()
        
         # varchar 
        Label(mainFrame, text='JAM PEMINJAMAN:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        # Textbox JAM_PEMINJAMAN
        self.txtJAM_PEMINJAMAN = Entry(mainFrame) 
        self.txtJAM_PEMINJAMAN.grid(row=4, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='JAM PENGEMBALIAN:').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        # Textbox JAM_PENGEMBALIAN
        self.txtJAM_PENGEMBALIAN = Entry(mainFrame) 
        self.txtJAM_PENGEMBALIAN.grid(row=5, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='DURASI WAKTU (Menit):').grid(row=6, column=0, sticky=W, padx=5, pady=5)
        # Textbox DURASI_WAKTU
        self.txtDURASI_WAKTU = Entry(mainFrame) 
        self.txtDURASI_WAKTU.grid(row=6, column=1, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='TOTAL BAYAR:').grid(row=7, column=0, sticky=W, padx=5, pady=5)
        # Textbox TOTAL_BAYAR
        self.txtTOTAL_BAYAR = Entry(mainFrame) 
        self.txtTOTAL_BAYAR.grid(row=7, column=1, padx=5, pady=5)
                
        # varchar 
        Label(mainFrame, text='STATUS BAYAR:').grid(row=8, column=0, sticky=W, padx=5, pady=5)
        # Textbox STATUS_BAYAR
        self.txtSTATUS_BAYAR = Entry(mainFrame) 
        self.txtSTATUS_BAYAR.grid(row=8, column=1, padx=5, pady=5)
                
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','namepelanggan','banyak_camera','tanggal','tarif_perjam','jam_peminjaman','jam_pengembalian','durasi_waktu','total_bayar','status_bayar')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='Id')
        self.tree.column('id', width="30")
        self.tree.heading('namepelanggan', text='Nama Pelanggan')
        self.tree.column('namepelanggan', width="100")
        self.tree.heading('banyak_camera', text='Banyak Camera')
        self.tree.column('banyak_camera', width="100")
        self.tree.heading('tanggal', text='Tanggal')
        self.tree.column('tanggal', width="100")
        self.tree.heading('tarif_perjam', text='Tarif Perjam')
        self.tree.column('tarif_perjam', width="100")
        self.tree.heading('jam_peminjaman', text='Jam Peminjaman')
        self.tree.column('jam_peminjaman', width="100")
        self.tree.heading('jam_pengembalian', text='Jam Pengembalian')
        self.tree.column('jam_pengembalian', width="120")
        self.tree.heading('durasi_waktu', text='Durasi Waktu (Menit)')
        self.tree.column('durasi_waktu', width="130")
        self.tree.heading('total_bayar', text='Total Bayar')
        self.tree.column('total_bayar', width="100")
        self.tree.heading('status_bayar', text='Status Bayar')
        self.tree.column('status_bayar', width="100")
        # set tree position
        self.tree.place(x=0, y=305)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNAMEPELANGGAN.delete(0,END)
        self.txtNAMEPELANGGAN.insert(END,"")
                                
        self.txtBANYAK_CAMERA.set("")
            
        self.txtTARIF_PERJAM.set("")
            
        self.txtJAM_PEMINJAMAN.delete(0,END)
        self.txtJAM_PEMINJAMAN.insert(END,"")
                                
        self.txtJAM_PENGEMBALIAN.delete(0,END)
        self.txtJAM_PENGEMBALIAN.insert(END,"")
                                
        self.txtDURASI_WAKTU.delete(0,END)
        self.txtDURASI_WAKTU.insert(END,"")
                                
        self.txtTOTAL_BAYAR.delete(0,END)
        self.txtTOTAL_BAYAR.insert(END,"")
                                
        self.txtSTATUS_BAYAR.delete(0,END)
        self.txtSTATUS_BAYAR.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data transaksi
        obj = Transaksi()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        namepelanggan = self.txtNAMEPELANGGAN.get()
        obj = Transaksi()
        res = obj.getByNAMEPELANGGAN(namepelanggan)
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
        namepelanggan = self.txtNAMEPELANGGAN.get()
        obj = Transaksi()
        res = obj.getByNAMEPELANGGAN(namepelanggan)
            
        self.txtBANYAK_CAMERA.set(obj.banyak_camera)
            
        self.txtTANGGAL.delete(0,END)
        self.txtTANGGAL.insert(END,obj.tanggal)
                                
        self.txtTARIF_PERJAM.set(obj.tarif_perjam)
            
        self.txtJAM_PEMINJAMAN.delete(0,END)
        self.txtJAM_PEMINJAMAN.insert(END,obj.jam_peminjaman)
                                
        self.txtJAM_PENGEMBALIAN.delete(0,END)
        self.txtJAM_PENGEMBALIAN.insert(END,obj.jam_pengembalian)
                                
        self.txtDURASI_WAKTU.delete(0,END)
        self.txtDURASI_WAKTU.insert(END,obj.durasi_waktu)
                                
        self.txtTOTAL_BAYAR.delete(0,END)
        self.txtTOTAL_BAYAR.insert(END,obj.total_bayar)
                                
        self.txtSTATUS_BAYAR.delete(0,END)
        self.txtSTATUS_BAYAR.insert(END,obj.status_bayar)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        namepelanggan = self.txtNAMEPELANGGAN.get()
        banyak_camera = self.txtBANYAK_CAMERA.get()
        tanggal = self.txtTANGGAL.get()
        tarif_perjam = self.txtTARIF_PERJAM.get()
        jam_peminjaman = self.txtJAM_PEMINJAMAN.get()
        jam_pengembalian = self.txtJAM_PENGEMBALIAN.get()
        durasi_waktu = self.txtDURASI_WAKTU.get()
        total_bayar = self.txtTOTAL_BAYAR.get()
        status_bayar = self.txtSTATUS_BAYAR.get()       
        obj = Transaksi()
        obj.namepelanggan = namepelanggan
        obj.banyak_camera = banyak_camera
        obj.tanggal = tanggal
        obj.tarif_perjam = tarif_perjam
        obj.jam_peminjaman = jam_peminjaman
        obj.jam_pengembalian = jam_pengembalian
        obj.durasi_waktu = durasi_waktu
        obj.total_bayar = total_bayar
        obj.status_bayar = status_bayar
        if(self.ditemukan==True):
            res = obj.updateByNAMEPELANGGAN(namepelanggan)
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
        namepelanggan = self.txtNAMEPELANGGAN.get()
        obj = Transaksi()
        obj.namepelanggan = namepelanggan
        if(self.ditemukan==True):
            res = obj.deleteByNAMEPELANGGAN(namepelanggan)
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
    aplikasi = FormTransaksi(root, "Formulir Data Transaksi")
    
    icon = tk.PhotoImage(file="icontransaksi.png")  
    root.iconphoto(True, icon)
    root.mainloop()