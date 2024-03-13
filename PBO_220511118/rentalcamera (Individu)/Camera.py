# filename : Camera.py
from db import DBConnection as mydb
class Camera:
    def __init__(self):
        self.__id=None
        self.__kode_camera=None
        self.__merek_camera=None
        self.__tahun_rilis=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def kode_camera(self):
        return self.__kode_camera
        
    @kode_camera.setter
    def kode_camera(self, value):
        self.__kode_camera = value
    @property
    def merek_camera(self):
        return self.__merek_camera
        
    @merek_camera.setter
    def merek_camera(self, value):
        self.__merek_camera = value
    @property
    def tahun_rilis(self):
        return self.__tahun_rilis
        
    @tahun_rilis.setter
    def tahun_rilis(self, value):
        self.__tahun_rilis = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_camera,self.__merek_camera,self.__tahun_rilis)
        sql="INSERT INTO camera (kode_camera,merek_camera,tahun_rilis) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_camera,self.__merek_camera,self.__tahun_rilis, id)
        sql="UPDATE camera SET kode_camera = %s,merek_camera = %s,tahun_rilis = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByKODE_CAMERA(self, kode_camera):
        self.conn = mydb()
        val = (self.__merek_camera,self.__tahun_rilis, kode_camera)
        sql="UPDATE camera SET merek_camera = %s,tahun_rilis = %s WHERE kode_camera=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM camera WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByKODE_CAMERA(self, kode_camera):
        self.conn = mydb()
        sql="DELETE FROM camera WHERE kode_camera='" + str(kode_camera) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM camera WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__kode_camera = self.result[1]
        self.__merek_camera = self.result[2]
        self.__tahun_rilis = self.result[3]
        self.conn.disconnect
        return self.result
    def getByKODE_CAMERA(self, kode_camera):
        a=str(kode_camera)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM camera WHERE kode_camera='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__kode_camera = self.result[1]
           self.__merek_camera = self.result[2]
           self.__tahun_rilis = self.result[3]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__kode_camera = ''
           self.__merek_camera = ''
           self.__tahun_rilis = ''
        
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
        sql="SELECT id,merek_camera FROM camera"
        self.result = self.conn.findAll(sql)
        return self.result