class Person:
    nama = ""
    gender = ""
    umur = 0

    def __init__(self,nama,gender,umur):
        self.nama = nama
        self.gender = gender
        self.umur = umur
    
    def cetak(self):
        print("--------------------------"
              "\nNama\t: %s"
              "\nGender\t: %s"
              "\nUmur\t: %i tahun"
              %(self.nama,self.gender,self.umur))
