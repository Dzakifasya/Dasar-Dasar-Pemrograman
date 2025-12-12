from Person import *

class Dosen (Person):
    gelar = ""
    jabatan = ""
    gaji = 0

    def __init__(self,nama,gender,umur,gelar,jabatan):
        super().__init__(nama,gender,umur)
        self.gelar = gelar
        self.jabatan = jabatan
    
    def setGaji(self,uang):
        self.gaji += uang
    
    def cetak(self):
        super().cetak()
        print("\nGelar\t: %s"
              "\nJabatan\t: %s"
              "\nGaji\t: Rp.%i"
              %(self.gelar,self.jabatan,self.gaji))
