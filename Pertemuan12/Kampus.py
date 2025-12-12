from Mahasiswa import *
from Dosen import *
#ciptakan object
m1 = Mahasiswa('Siti Aminah','Wanita',20,'SI',3,3.75)
m2 = Mahasiswa('Budi Santoso','Pria',23,'TI',5,3.35)
d1 = Dosen('Sirojul Munir','Pria',43,'Dr, S.Si, M.Kom','LPMI')
d2 = Dosen('Henry Saptono','Pria',44,'S.Si, M.Kom','Ketua BTSI')
#gunakan fungsi2 yg ada di class
d1.setGaji(17000000)
d2.setGaji(15000000)
m1.cetak()
m2.cetak()
d1.cetak()
d2.cetak()