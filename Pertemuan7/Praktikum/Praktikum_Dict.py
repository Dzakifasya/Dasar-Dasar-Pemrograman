# Membuat dictionanry berisi nama (key) dan nilai (value)
nilai = { 
    'Firda':89, 
    'Inaya':100,
    'Deden':59,
    'Fawwaz':95
    }
print("Data nilai : ",nilai)

#Mengubah nilai di dictionary
nilai["Firda"] = 80
print("Data nilai Firda setelah setelah diubah : ", nilai['Firda'])

#menghapus item dalam dictionary
del nilai['Inaya']
print('Data nilai setelah Inaya dihapus : ', nilai)


# Nested dictionary
siswa = {
    "S1": {"nama" : "Dzakwan", "nilai": 85},
    "S2": {"nama" : "Mumtaz", "nilai": 90},
    "S3": {"nama" : "Aji", "nilai": 79},
    "S4": {"nama" : "Fasya", "nilai": 100},
}

hasil = []

print("ID\tNama\t\tNilai")
for id, data in siswa.items():
    nama = data['nama']
    nilai = data["nilai"]
    print(f'{id}\t{nama}\t\t{nilai}')

#Proses penilaian dan status
for id, data in siswa.items():
    nama = data['nama']
    nilai = data['nilai']

    status = ('Gagal', 'Lulus') [nilai >-80]

    #Menentukan grape berdassarkan nilai
    if 90 <= nilai <= 100:
        grade = 'A'
    elif 80 <= nilai <= 90:
        grade = 'B'
    elif 70 <= nilai <= 80:
        grade = 'c'
    elif 60 <= nilai <= 70:
        grade = 'D'
    else:
        grade = 'E'

    #Menentukan predikat berdasarkan grade
    match grade:
        case 'A': predikat = 'Sangat Baik'
        case 'B': predikat = 'Baik'
        case 'C': predikat = 'Cukup'
        case 'D': predikat = 'Kurang'
        case 'E': predikat = 'Bodoh'

    hasil.append((id, nama,nilai, status, grade, predikat))

# Menampilkan Hasil
print('\nHasil Evaluasi Nilai Siswa')
print("================================================")
print("ID\tNama\t\tNilai\tStatus\tGrade\tPredikat")
print("================================================")

for data in hasil:
    id, nama, nilai, status, grade, predikat = data
    print(f"{id}\t{nama}\t\t{nilai}\t{grade}\t{predikat}")