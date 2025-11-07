nilai = { 'Firda':89, 'Inaya':100, 'Deden':59,'Fawwaz':95}
print("Data nilai : ",nilai)

print("\n-----Cetak Key.indexnya Saja-----\n")
for nama in nilai.keys():
    print("Nanam Siswa : ",nama)

print("\n-----Cetak Value Saja-----\n")
for skor in nilai.values():
    print("Nilai : ",skor)

print("\n-----Cetak Key & Value -----\n")
for nama,skor in nilai.items():
    print("Nama Siswa : %s \t Nilai : %i" % (nama,skor))

