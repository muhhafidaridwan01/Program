# filename : Camera.py
from db import DBConnection as mydb
class Camera:
    def __init__(self):
        self.__id=None
        self.__kode_kamera=None
        self.__nomor_ktp=None
        self.__nama_pelanggan=None
        self.__tanggal=None
        self.__tarif_perjam=None
        self.__total_bayar=None
        self.__status_bayar=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def kode_kamera(self):
        return self.__kode_kamera
        
    @kode_kamera.setter
    def kode_kamera(self, value):
        self.__kode_kamera = value
    @property
    def nomor_ktp(self):
        return self.__nomor_ktp
        
    @nomor_ktp.setter
    def nomor_ktp(self, value):
        self.__nomor_ktp = value
    @property
    def nama_pelanggan(self):
        return self.__nama_pelanggan
        
    @nama_pelanggan.setter
    def nama_pelanggan(self, value):
        self.__nama_pelanggan = value
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
        val = (self.__kode_kamera,self.__nomor_ktp,self.__nama_pelanggan,self.__tanggal,self.__tarif_perjam,self.__total_bayar,self.__status_bayar)
        sql="INSERT INTO Camera (kode_kamera,nomor_ktp,nama_pelanggan,tanggal,tarif_perjam,total_bayar,status_bayar) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_kamera,self.__nomor_ktp,self.__nama_pelanggan,self.__tanggal,self.__tarif_perjam,self.__total_bayar,self.__status_bayar, id)
        sql="UPDATE camera SET kode_kamera = %s,nomor_ktp = %s,nama_pelanggan = %s,tanggal = %s,tarif_perjam = %s,total_bayar = %s,status_bayar = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateBy(self, ):
        self.conn = mydb()
        val = (self.__kode_kamera,self.__nomor_ktp,self.__nama_pelanggan,self.__tanggal,self.__tarif_perjam,self.__total_bayar,self.__status_bayar, )
        sql="UPDATE camera SET kode_kamera = %s,nomor_ktp = %s,nama_pelanggan = %s,tanggal = %s,tarif_perjam = %s,total_bayar = %sstatus_bayar = %s WHERE =%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM camera WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteBy(self, ):
        self.conn = mydb()
        sql="DELETE FROM camera WHERE ='" + str() + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM camera WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__kode_kamera = self.result[1]
        self.__nomor_ktp = self.result[2]
        self.__nama_pelanggan = self.result[3]
        self.__tanggal = self.result[4]
        self.__tarif_perjam = self.result[5]
        self.__total_bayar = self.result[6]
        self.__status_bayar = self.result[7]
        self.conn.disconnect
        return self.result
    def getBy(self, ):
        a=str()
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM camera WHERE ='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__kode_kamera = self.result[1]
           self.__nomor_ktp = self.result[2]
           self.__nama_pelanggan = self.result[3]
           self.__tanggal = self.result[4]
           self.__tarif_perjam = self.result[5]
           self.__total_bayar = self.result[6]
           self.__status_bayar = self.result[7]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__kode_kamera = ''
           self.__nomor_ktp = ''
           self.__nama_pelanggan = ''
           self.__tanggal = ''
           self.__tarif_perjam = ''
           self.__total_bayar = ''
           self.__status_bayar = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM camera"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,nomor_ktp FROM camera"
        self.result = self.conn.findAll(sql)
        return self.result