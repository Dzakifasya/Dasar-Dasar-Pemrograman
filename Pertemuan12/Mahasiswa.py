from Person import *

class Mahasiswa (Person):
    prodi = ""
    semester = 0
    ipk = 0

    def __init__(self,nama,gender,umur,prodi,semester,ipk):
        super().__init__(nama,gender,umur)
        self.prodi = prodi
        self.semester = semester
        self.ipk = ipk
    
    def cetak(self):
        super().cetak()
        print("\nProdi\t: %s"
              "\nSemester\t: %s"
              "\nIPK\t: %.2f"
              %(self.prodi,self.semester,self.ipk))
