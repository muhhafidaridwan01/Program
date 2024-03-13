# filename : Pelanggan.py
from db import DBConnection as mydb
class Pelanggan:
    def __init__(self):
        self.__id=None
        self.__nama_pelanggan=None
        self.__jk=None
        self.__nomor_ktp=None
        self.__nomor_hp=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def nama_pelanggan(self):
        return self.__nama_pelanggan
        
    @nama_pelanggan.setter
    def nama_pelanggan(self, value):
        self.__nama_pelanggan = value
    @property
    def jk(self):
        return self.__jk
        
    @jk.setter
    def jk(self, value):
        self.__jk = value
    @property
    def nomor_ktp(self):
        return self.__nomor_ktp
        
    @nomor_ktp.setter
    def nomor_ktp(self, value):
        self.__nomor_ktp = value
    @property
    def nomor_hp(self):
        return self.__nomor_hp
        
    @nomor_hp.setter
    def nomor_hp(self, value):
        self.__nomor_hp = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__nama_pelanggan,self.__jk,self.__nomor_ktp,self.__nomor_hp)
        sql="INSERT INTO pelanggan (nama_pelanggan,jk,nomor_ktp,nomor_hp) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__nama_pelanggan,self.__jk,self.__nomor_ktp,self.__nomor_hp, id)
        sql="UPDATE pelanggan SET nama_pelanggan = %s,jk = %s,nomor_ktp = %s,nomor_hp = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNAMA_PELANGGAN(self, nama_pelanggan):
        self.conn = mydb()
        val = (self.__jk,self.__nomor_ktp,self.__nomor_hp, nama_pelanggan)
        sql="UPDATE pelanggan SET jk = %s,nomor_ktp = %s,nomor_hp = %s WHERE nama_pelanggan=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM pelanggan WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNAMA_PELANGGAN(self, nama_pelanggan):
        self.conn = mydb()
        sql="DELETE FROM pelanggan WHERE nama_pelanggan='" + str(nama_pelanggan) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM pelanggan WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__nama_pelanggan = self.result[1]
        self.__jk = self.result[2]
        self.__nomor_ktp = self.result[3]
        self.__nomor_hp = self.result[4]
        self.conn.disconnect
        return self.result
    def getByNAMA_PELANGGAN(self, nama_pelanggan):
        a=str(nama_pelanggan)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM pelanggan WHERE nama_pelanggan='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__nama_pelanggan = self.result[1]
           self.__jk = self.result[2]
           self.__nomor_ktp = self.result[3]
           self.__nomor_hp = self.result[4]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__nama_pelanggan = ''
           self.__jk = ''
           self.__nomor_ktp = ''
           self.__nomor_hp = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM pelanggan"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,jk FROM pelanggan"
        self.result = self.conn.findAll(sql)
        return self.result     