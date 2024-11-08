usia = int(input("Masukkan usia "))
if usia < 0 : 
    print("Harganya tidak valid")
    exit()   
if usia < 3 :
    print("Harganya gratis")
    exit()
   
elif usia < 5 : 
    harga_tiket = 0
elif usia <= 12:
    harga_tiket = 50000
elif usia >=13 or usia <= 59:
    harga_tiket = 100000
else :
    harga_tiket = 70000

keanggotaan = input("Apakah anda anggota? (ya/tidak) :")
if keanggotaan == "ya":
    diskon = harga_tiket * (20/100)
    harga_tiket = harga_tiket - diskon

print(f"Harga tiket: Rp.{int(harga_tiket)}")

