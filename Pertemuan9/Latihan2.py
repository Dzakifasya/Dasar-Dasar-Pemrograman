nama = input("Nama lu Siapa ?")
alamat = input("Rumah lu dimana ?")
agama = input("""Agama lu apa ? Islam/Kristen/Budha/Atheis
jawabanmu = """)
jabatan = input("Apa Jabatan lu\n Manager/Asisten Manager/Superpisor/Staff\n jawabanmu = ")


def getGajiPokok(jabatan):
    return {
        "Manager" : 15000000,
        "Asisten Manager" : 1000000,
        "Supervisor" : 7000000,
        "Staff" : 4000000
    }[jabatan]

tunjanganjabatan = 0.3 * getGajiPokok(jabatan)
bpjs = 0.1 * getGajiPokok(jabatan)
status = input("Apa Status lu ? Menikah/Belum\n jawabanmu = ")

def gettunjangankeluarga():
    if status == "Menikah":
        return 0.1 * getGajiPokok(jabatan)
    else:
        return 0
    
GajiKotor = getGajiPokok(jabatan) + tunjanganjabatan + bpjs + gettunjangankeluarga()

def hitungzakat():
    if agama == "Islam" and GajiKotor >= 7000000:
        return 0.025 * GajiKotor
    else:
        return 0
Gajibersama = GajiKotor - hitungzakat()

print(f""""Nama Pegawai \t\t: {nama}
Alamat \t\t\t: {alamat}
Agama \t\t\t: {agama}
Jabatan \t\t: {jabatan}
Status \t\t\t: {status}
Gaji Pokok \t\t: {getGajiPokok(jabatan)}
Tunjangan \t\t: {tunjanganjabatan}
BPJS \t\t\t: {bpjs}
Tunjangan Keluarga\t : {gettunjangankeluarga()}
Gaji Kotor \t\t: {GajiKotor}
Zakat \t\t\t: {hitungzakat()}
Gaji Bersih \t\t: {Gajibersama}
""")
    