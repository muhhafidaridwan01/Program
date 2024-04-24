from db import DBConnection as mydb

class Bidan:

    def __init__(self):
        self.__id=None
        self.__nip=None
        self.__nama=None
        self.__jk=None
        self.__tempat_tugas=None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def id(self):
        return self.__id

    @property
    def nip(self):
        return self.__nip

    @nip.setter
    def nip(self, value):
        self.__nip = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    @property
    def tempat_tugas(self):
        return self.__tempat_tugas

    @tempat_tugas.setter
    def tempat_tugas(self, value):
        self.__tempat_tugas = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nip, self.__nama, self.__jk, self.__tempat_tugas)
        sql="INSERT INTO bidan (nip, nama, jk, tempat_tugas) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nip, self.__nama, self.__jk, self.__tempat_tugas, id)
        sql="UPDATE bidan SET nip = %s, nama = %s, jk=%s, tempat_tugas=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNIP(self, nip):
        self.conn = mydb()
        val = (self.__nama, self.__jk, self.__tempat_tugas, nip)
        sql="UPDATE bidan SET nama = %s, jk=%s, tempat_tugas=%s WHERE nip=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM bidan WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNIP(self, nip):
        self.conn = mydb()
        sql="DELETE FROM bidan WHERE nip='" + str(nip) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM bidan WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nip = self.result[1]
        self.__nama = self.result[2]
        self.__jk = self.result[3]
        self.__tempat_tugas = self.result[4]
        self.conn.disconnect
        return self.result

    def getByNIP(self, nip):
        a=str(nip)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM bidan WHERE nip='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nip = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.__tempat_tugas = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nip = ''
            self.__nama = ''
            self.__jk = ''
            self.__tempat_tugas = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM bidan"
        self.result = self.conn.findAll(sql)
        return self.result

# delete Data
A = Bidan()
B = A.getAllData()
print(B)