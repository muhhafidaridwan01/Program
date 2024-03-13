
# filename : Catatan_order.py
from db import DBConnection as mydb
class Catatan_order:
    def __init__(self):
        self.__id=None
        self.__namapelanggan=None
        self.__noktp=None
        self.__kodecamera=None
        self.__merekcamera=None
        self.__banyakcamera=None
        self.__statusbayar=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def namapelanggan(self):
        return self.__namapelanggan
        
    @namapelanggan.setter
    def namapelanggan(self, value):
        self.__namapelanggan = value
    @property
    def noktp(self):
        return self.__noktp
        
    @noktp.setter
    def noktp(self, value):
        self.__noktp = value
    @property
    def kodecamera(self):
        return self.__kodecamera
        
    @kodecamera.setter
    def kodecamera(self, value):
        self.__kodecamera = value
    @property
    def merekcamera(self):
        return self.__merekcamera
        
    @merekcamera.setter
    def merekcamera(self, value):
        self.__merekcamera = value
    @property
    def banyakcamera(self):
        return self.__banyakcamera
        
    @banyakcamera.setter
    def banyakcamera(self, value):
        self.__banyakcamera = value
    @property
    def statusbayar(self):
        return self.__statusbayar
        
    @statusbayar.setter
    def statusbayar(self, value):
        self.__statusbayar = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__namapelanggan,self.__noktp,self.__kodecamera,self.__merekcamera,self.__banyakcamera,self.__statusbayar)
        sql="INSERT INTO catatan_order (namapelanggan,noktp,kodecamera,merekcamera,banyakcamera,statusbayar) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__namapelanggan,self.__noktp,self.__kodecamera,self.__merekcamera,self.__banyakcamera,self.__statusbayar, id)
        sql="UPDATE catatan_order SET namapelanggan = %s,noktp = %s,kodecamera = %s,merekcamera = %s,banyakcamera = %s,statusbayar = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNAMAPELANGGAN(self, namapelanggan):
        self.conn = mydb()
        val = (self.__noktp,self.__kodecamera,self.__merekcamera,self.__banyakcamera,self.__statusbayar, namapelanggan)
        sql="UPDATE catatan_order SET noktp = %s,kodecamera = %s,merekcamera = %s,banyakcamera = %s,statusbayar = %s WHERE namapelanggan=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM catatan_order WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNAMAPELANGGAN(self, namapelanggan):
        self.conn = mydb()
        sql="DELETE FROM catatan_order WHERE namapelanggan='" + str(namapelanggan) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM catatan_order WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__namapelanggan = self.result[1]
        self.__noktp = self.result[2]
        self.__kodecamera = self.result[3]
        self.__merekcamera = self.result[4]
        self.__banyakcamera = self.result[5]
        self.__statusbayar = self.result[6]
        self.conn.disconnect
        return self.result
    def getByNAMAPELANGGAN(self, namapelanggan):
        a=str(namapelanggan)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM catatan_order WHERE namapelanggan='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__namapelanggan = self.result[1]
           self.__noktp = self.result[2]
           self.__kodecamera = self.result[3]
           self.__merekcamera = self.result[4]
           self.__banyakcamera = self.result[5]
           self.__statusbayar = self.result[6]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__namapelanggan = ''
           self.__noktp = ''
           self.__kodecamera = ''
           self.__merekcamera = ''
           self.__banyakcamera = ''
           self.__statusbayar = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM catatan_order"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,noktp FROM catatan_order"
        self.result = self.conn.findAll(sql)
        return self.result