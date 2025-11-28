import math

def tambah(bil1, bil2):
    hasil = bil1 + bil2
    print("Penjumlahan %i + %i = %i" % (bil1, bil2, hasil))

def kurang(bil1, bil2):
    hasil = bil1 - bil2
    print("Pengurangan %i - %i = %i" % (bil1, bil2, hasil))

def kali(bil1, bil2):
    hasil = bil1 * bil2
    print("Perkalian %i * %i = %i" % (bil1, bil2, hasil))

def bagi(bil1, bil2):
    hasil = bil1 / bil2
    print("Pembagian %i / %i = %.2f" % (bil1, bil2, hasil))

def pangkat(bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print("Pemangkatan %i ^ %i = %i" % (bil1, bil2, hasil))

pangkat(2,3)

