nama = input("Nama Siswa\t: ")
mata_kuliah = str(input("Mata Kuliah\t: "))
nilai = float(input("Nilai\t\t: "))
#tuple & list
keterangan = ("Gagal","Lulus") [nilai >= 60]
#cetak
print("----------Data Nilai Siswa----------"
      "\nNama Siswa\t: %s"
      "\nMata Kuliah\t: %s"
      "\nNilai\t\t: %.2f"
      "\nKeterangan\t: %s"
      % (nama, mata_kuliah, nilai, keterangan))
