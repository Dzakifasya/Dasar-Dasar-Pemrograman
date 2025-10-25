pw = "python123"
percobaan = 1

while percobaan <= 3:
    password = input("Masukkan password: ")
    if password == pw:
        print("Login Berhasil")
        break
    else:
        print("Password Salah, silahkan coba lagi.\n")
        percobaan += 1
    if percobaan > 3:
        print("Maaf, percobaan login anda sudah melebihi batas.")
 
