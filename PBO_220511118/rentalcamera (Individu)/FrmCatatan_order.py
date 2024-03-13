
# filename : FrmCatatan_order.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Catatan_order import Catatan_order
class FormCatatan_order:   
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("778x480")
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
        # Textbox NAMAPELANGGAN
        self.txtNAMAPELANGGAN = Entry(mainFrame) 
        self.txtNAMAPELANGGAN.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNAMAPELANGGAN.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # int 
        Label(mainFrame, text='NO.KTP:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox NOKTP
        self.txtNOKTP = Entry(mainFrame) 
        self.txtNOKTP.grid(row=1, column=1, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='KODE CAMERA:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Textbox KODECAMERA
        self.txtKODECAMERA = Entry(mainFrame) 
        self.txtKODECAMERA.grid(row=2, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='MEREK CAMERA:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Textbox MEREKCAMERA
        self.txtMEREKCAMERA = Entry(mainFrame) 
        self.txtMEREKCAMERA.grid(row=3, column=1, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='BANYAK CAMERA:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        # Textbox BANYAKCAMERA
        self.txtBANYAKCAMERA = Entry(mainFrame) 
        self.txtBANYAKCAMERA.grid(row=4, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='STATUS BAYAR:').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        # Textbox STATUSBAYAR
        self.txtSTATUSBAYAR = Entry(mainFrame) 
        self.txtSTATUSBAYAR.grid(row=5, column=1, padx=5, pady=5)
                
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','namapelanggan','noktp','kodecamera','merekcamera','banyakcamera','statusbayar')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='Id')
        self.tree.column('id', width="30")
        self.tree.heading('namapelanggan', text='Nama Pelanggan')
        self.tree.column('namapelanggan', width="120")
        self.tree.heading('noktp', text='No Ktp')
        self.tree.column('noktp', width="120")
        self.tree.heading('kodecamera', text='Kode Camera')
        self.tree.column('kodecamera', width="120")
        self.tree.heading('merekcamera', text='Merek Camera')
        self.tree.column('merekcamera', width="120")
        self.tree.heading('banyakcamera', text='Banyak Camera')
        self.tree.column('banyakcamera', width="120")
        self.tree.heading('statusbayar', text='Status Bayar')
        self.tree.column('statusbayar', width="120")
        # set tree position
        self.tree.place(x=0, y=225)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNAMAPELANGGAN.delete(0,END)
        self.txtNAMAPELANGGAN.insert(END,"")
                                
        self.txtNOKTP.delete(0,END)
        self.txtNOKTP.insert(END,"")
                                
        self.txtKODECAMERA.delete(0,END)
        self.txtKODECAMERA.insert(END,"")
                                
        self.txtMEREKCAMERA.delete(0,END)
        self.txtMEREKCAMERA.insert(END,"")
                                
        self.txtBANYAKCAMERA.delete(0,END)
        self.txtBANYAKCAMERA.insert(END,"")
                                
        self.txtSTATUSBAYAR.delete(0,END)
        self.txtSTATUSBAYAR.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data catatan_order
        obj = Catatan_order()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        namapelanggan = self.txtNAMAPELANGGAN.get()
        obj = Catatan_order()
        res = obj.getByNAMAPELANGGAN(namapelanggan)
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
        namapelanggan = self.txtNAMAPELANGGAN.get()
        obj = Catatan_order()
        res = obj.getByNAMAPELANGGAN(namapelanggan)
            
        self.txtNOKTP.delete(0,END)
        self.txtNOKTP.insert(END,obj.noktp)
                                
        self.txtKODECAMERA.delete(0,END)
        self.txtKODECAMERA.insert(END,obj.kodecamera)
                                
        self.txtMEREKCAMERA.delete(0,END)
        self.txtMEREKCAMERA.insert(END,obj.merekcamera)
                                
        self.txtBANYAKCAMERA.delete(0,END)
        self.txtBANYAKCAMERA.insert(END,obj.banyakcamera)
                                
        self.txtSTATUSBAYAR.delete(0,END)
        self.txtSTATUSBAYAR.insert(END,obj.statusbayar)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        namapelanggan = self.txtNAMAPELANGGAN.get()
        noktp = self.txtNOKTP.get()
        kodecamera = self.txtKODECAMERA.get()
        merekcamera = self.txtMEREKCAMERA.get()
        banyakcamera = self.txtBANYAKCAMERA.get()
        statusbayar = self.txtSTATUSBAYAR.get()       
        obj = Catatan_order()
        obj.namapelanggan = namapelanggan
        obj.noktp = noktp
        obj.kodecamera = kodecamera
        obj.merekcamera = merekcamera
        obj.banyakcamera = banyakcamera
        obj.statusbayar = statusbayar
        if(self.ditemukan==True):
            res = obj.updateByNAMAPELANGGAN(namapelanggan)
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
        namapelanggan = self.txtNAMAPELANGGAN.get()
        obj = Catatan_order()
        obj.namapelanggan = namapelanggan
        if(self.ditemukan==True):
            res = obj.deleteByNAMAPELANGGAN(namapelanggan)
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
    aplikasi = FormCatatan_order(root, "Form Data Order")
    icon = tk.PhotoImage(file="iconorder.png")  
    root.iconphoto(True, icon)
    
    root.mainloop() 