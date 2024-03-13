# filename : Transaksi.py
from db import DBConnection as mydb
class Transaksi:
    def __init__(self):
        self.__id=None
        self.__namepelanggan=None
        self.__banyak_camera=None
        self.__tanggal=None
        self.__tarif_perjam=None
        self.__jam_peminjaman=None
        self.__jam_pengembalian=None
        self.__durasi_waktu=None
        self.__total_bayar=None
        self.__status_bayar=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def namepelanggan(self):
        return self.__namepelanggan
        
    @namepelanggan.setter
    def namepelanggan(self, value):
        self.__namepelanggan = value
    @property
    def banyak_camera(self):
        return self.__banyak_camera
        
    @banyak_camera.setter
    def banyak_camera(self, value):
        self.__banyak_camera = value
    @property
    def tanggal(self):
        return self.__tanggal
        
    @tanggal.setter
    def tanggal(self, value):
        self.__tanggal = value
    @property
    def tarif_perjam(self):
        return self.__tarif_perjam
        
    @tarif_perjam.setter
    def tarif_perjam(self, value):
        self.__tarif_perjam = value
    @property
    def jam_peminjaman(self):
        return self.__jam_peminjaman
        
    @jam_peminjaman.setter
    def jam_peminjaman(self, value):
        self.__jam_peminjaman = value
    @property
    def jam_pengembalian(self):
        return self.__jam_pengembalian
        
    @jam_pengembalian.setter
    def jam_pengembalian(self, value):
        self.__jam_pengembalian = value
    @property
    def durasi_waktu(self):
        return self.__durasi_waktu
        
    @durasi_waktu.setter
    def durasi_waktu(self, value):
        self.__durasi_waktu = value
    @property
    def total_bayar(self):
        return self.__total_bayar
        
    @total_bayar.setter
    def total_bayar(self, value):
        self.__total_bayar = value
    @property
    def status_bayar(self):
        return self.__status_bayar
        
    @status_bayar.setter
    def status_bayar(self, value):
        self.__status_bayar = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__namepelanggan,self.__banyak_camera,self.__tanggal,self.__tarif_perjam,self.__jam_peminjaman,self.__jam_pengembalian,self.__durasi_waktu,self.__total_bayar,self.__status_bayar)
        sql="INSERT INTO transaksi (namepelanggan,banyak_camera,tanggal,tarif_perjam,jam_peminjaman,jam_pengembalian,durasi_waktu,total_bayar,status_bayar) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__namepelanggan,self.__banyak_camera,self.__tanggal,self.__tarif_perjam,self.__jam_peminjaman,self.__jam_pengembalian,self.__durasi_waktu,self.__total_bayar,self.__status_bayar, id)
        sql="UPDATE transaksi SET namepelanggan = %s,banyak_camera = %s,tanggal = %s,tarif_perjam = %s,jam_peminjaman = %s,jam_pengembalian = %s,durasi_waktu = %s,total_bayar = %s,status_bayar = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNAMEPELANGGAN(self, namepelanggan):
        self.conn = mydb()
        val = (self.__banyak_camera,self.__tanggal,self.__tarif_perjam,self.__jam_peminjaman,self.__jam_pengembalian,self.__durasi_waktu,self.__total_bayar,self.__status_bayar, namepelanggan)
        sql="UPDATE transaksi SET banyak_camera = %s,tanggal = %s,tarif_perjam = %s,jam_peminjaman = %s,jam_pengembalian = %s,durasi_waktu = %s,total_bayar = %s,status_bayar = %s WHERE namepelanggan=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM transaksi WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNAMEPELANGGAN(self, namepelanggan):
        self.conn = mydb()
        sql="DELETE FROM transaksi WHERE namepelanggan='" + str(namepelanggan) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM transaksi WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__namepelanggan = self.result[1]
        self.__banyak_camera = self.result[2]
        self.__tanggal = self.result[3]
        self.__tarif_perjam = self.result[4]
        self.__jam_peminjaman = self.result[5]
        self.__jam_pengembalian = self.result[6]
        self.__durasi_waktu = self.result[7]
        self.__total_bayar = self.result[8]
        self.__status_bayar = self.result[9]
        self.conn.disconnect
        return self.result
    def getByNAMEPELANGGAN(self, namepelanggan):
        a=str(namepelanggan)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM transaksi WHERE namepelanggan='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__namepelanggan = self.result[1]
           self.__banyak_camera = self.result[2]
           self.__tanggal = self.result[3]
           self.__tarif_perjam = self.result[4]
           self.__jam_peminjaman = self.result[5]
           self.__jam_pengembalian = self.result[6]
           self.__durasi_waktu = self.result[7]
           self.__total_bayar = self.result[8]
           self.__status_bayar = self.result[9]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__namepelanggan = ''
           self.__banyak_camera = ''
           self.__tanggal = ''
           self.__tarif_perjam = ''
           self.__jam_peminjaman = ''
           self.__jam_pengembalian = ''
           self.__durasi_waktu = ''
           self.__total_bayar = ''
           self.__status_bayar = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM transaksi"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,banyak_camera FROM transaksi"
        self.result = self.conn.findAll(sql)
        return self.result