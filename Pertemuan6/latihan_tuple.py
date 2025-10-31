#tuple index/keynya dimulai dari 0
ar_buah = ('Pepaya'
,'Mangga','Pisang',
'Jambu','Belimbing')
ar_buah = ('Manggis',
'Markisa') + ar_buah
#cetak
print('Buah index 2:',ar_buah[2])
print('Buah index 4:',ar_buah[4])
#len = jumlah elemen
print('Jumlah Buah :',len(ar_buah))
print('-----cetak all buah------')
for buah in ar_buah:
    print('Buah'
,buah)
#memotong list
print('Memotong tuple 1 - 4', ar_buah[1:4])