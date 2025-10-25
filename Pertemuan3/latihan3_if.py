pelangan = "Zackpass"
total_belanja = 150000
''''
if total_belanja > 100000:
    keterangan = "Selamat Anda Dapat Piring Gratis"
else:
    keterangan = "Terima Kasih sudah Berbelanja"
'''
keterangan = "Selamat Anda Dapat Piring Gratis" if total_belanja > 100000 else "Terima Kasih sudah Berbelanja"
print("Pelangan",pelangan,"\nTotal Belanja Anda Rp.",total_belanja,
    "\n",keterangan)