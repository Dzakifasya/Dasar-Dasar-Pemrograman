import mymodul
import mymodul as hitung
from mymodul import tambah, pangkat
from mymodul import *
from mymodul import tambah as t, pangkat as p, kurang as k, kali as x, bagi as b

print('--------mengunakan import modul sendiri--------')
mymodul.tambah(2,3)
mymodul.pangkat(2,3)

print('--------cara import dengan alias--------')
hitung.kali(4,5)
hitung.bagi(10,2)

print('--------cara import fungsi tertentu--------')
tambah(7,8)
pangkat(3,4)

print('--------cara import semua fungsi--------')
kurang(15,5)
kali(6,7)
bagi(20,4)
pangkat(5,2)

print('--------cara import dengan alias pada fungsi tertentu--------')
t(9,1)
p(2,5)
k(10,3)
x(3,3)
b(18,6)



