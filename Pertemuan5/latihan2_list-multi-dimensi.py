# List makanan dengan 2 dimensi
list_makanan = [
["Bakwan", "Combro", "Misro"],
["Sop Iga", "Sop Buntut", "Sop Kaki"],
["Nasi Uduk", "Nasi Goreng", "Nasi Rames"]
]
print('------cetak per item------')
print(list_makanan[0][0])
print(list_makanan[1][2])
print(list_makanan[2][2])
print('------cetak semuanya dengan nestedLoop------')
for menu in list_makanan:
    for makanan in menu:
        print(makanan)