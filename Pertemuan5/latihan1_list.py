buah2an = ['Pepaya','Mangga','Pisang','Jambu','Belimbing']
buah2an[2] = 'Apel'
print('Buah index 2', buah2an[2])
del buah2an[4]
#print('Buah index 3', buah2an[3])

buah2an.insert(1,'Durian')
buah2an.append('Jeruk')
print('--------------------------------cetak all data--------------------------------')
for buah in buah2an:
    print("Buah",buah)


print("Potong List",buah2an[1:5])