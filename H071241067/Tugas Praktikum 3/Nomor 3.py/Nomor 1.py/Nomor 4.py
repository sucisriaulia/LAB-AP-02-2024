# Soal 4
total_harga = int(input("Masukkan total harga: "))
uang_diberikan = int(input("Masukkan uang yang diberikan: "))

kembalian = uang_diberikan - total_harga

pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

for pecahan in pecahan_uang:
  jumlah_lembar = kembalian / pecahan
  if jumlah_lembar > 0: 
    print(f"{int(jumlah_lembar)} lembar Rp {pecahan:,}")
    kembalian %= pecahan
