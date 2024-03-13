# filename : FrmCamera.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Camera import Camera
class FormCamera:   
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("415x370")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # varchar 
        Label(mainFrame, text='KODE_CAMERA:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox KODE_CAMERA
        self.txtKODE_CAMERA = Entry(mainFrame) 
        self.txtKODE_CAMERA.grid(row=0, column=1, padx=5, pady=5) 
        self.txtKODE_CAMERA.bind ("<Return>",self.onCari) # menambahkan event Enter key
                
        # varchar 
        Label(mainFrame, text='MEREK_CAMERA:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox MEREK_CAMERA
        self.txtMEREK_CAMERA = Entry(mainFrame) 
        self.txtMEREK_CAMERA.grid(row=1, column=1, padx=5, pady=5)
                
        # int 
        Label(mainFrame, text='TAHUN_RILIS:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Textbox TAHUN_RILIS
        self.txtTAHUN_RILIS = Entry(mainFrame) 
        self.txtTAHUN_RILIS.grid(row=2, column=1, padx=5, pady=5)
                
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','kode_camera','merek_camera','tahun_rilis')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='Id')
        self.tree.column('id', width="30")
        self.tree.heading('kode_camera', text='Kode Camera')
        self.tree.column('kode_camera', width="120")
        self.tree.heading('merek_camera', text='Merek Camera')
        self.tree.column('merek_camera', width="120")
        self.tree.heading('tahun_rilis', text='Tahun Rilis')
        self.tree.column('tahun_rilis', width="120")
        # set tree position
        self.tree.place(x=0, y=120)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtKODE_CAMERA.delete(0,END)
        self.txtKODE_CAMERA.insert(END,"")
                                
        self.txtMEREK_CAMERA.delete(0,END)
        self.txtMEREK_CAMERA.insert(END,"")
                                
        self.txtTAHUN_RILIS.delete(0,END)
        self.txtTAHUN_RILIS.insert(END,"")
                                
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
        kode_camera = self.txtKODE_CAMERA.get()
        obj = Camera()
        res = obj.getByKODE_CAMERA(kode_camera)
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
        kode_camera = self.txtKODE_CAMERA.get()
        obj = Camera()
        res = obj.getByKODE_CAMERA(kode_camera)
            
        self.txtMEREK_CAMERA.delete(0,END)
        self.txtMEREK_CAMERA.insert(END,obj.merek_camera)
                                
        self.txtTAHUN_RILIS.delete(0,END)
        self.txtTAHUN_RILIS.insert(END,obj.tahun_rilis)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        kode_camera = self.txtKODE_CAMERA.get()
        merek_camera = self.txtMEREK_CAMERA.get()
        tahun_rilis = self.txtTAHUN_RILIS.get()       
        obj = Camera()
        obj.kode_camera = kode_camera
        obj.merek_camera = merek_camera
        obj.tahun_rilis = tahun_rilis
        if(self.ditemukan==True):
            res = obj.updateByKODE_CAMERA(kode_camera)
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
        kode_camera = self.txtKODE_CAMERA.get()
        obj = Camera()
        obj.kode_camera = kode_camera
        if(self.ditemukan==True):
            res = obj.deleteByKODE_CAMERA(kode_camera)
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
    aplikasi = FormCamera(root, "Form Data Camera")
    
    icon = tk.PhotoImage(file="iconcamera.png")  
    root.iconphoto(True, icon)
    root.mainloop()