# Soal 1
n = int(input('Masukkan Jumlah Baris :'))

#Mencetak Bagian Atas Segitiga
for i in range(n // 2) if n % 2 == 0 else range(n // 2 + 1) :
    print('  ' * (n // 2 - i - (n % 2 == 0)) + ' *' * (2 * i + 1))

#Mencetak Bagian Bawah Segitiga
for i in range(n // 2 - 1, -1, -1):
    print('  ' * (n // 2 - i - (n % 2 == 0)) + ' *' * (2 * i + 1))


# Soal 2
import random
angka_rahasia = random.randint(1, 100)
for i in range(5):
    tebakan = int(input("Masukkan tebakan anda (0 untuk berhenti): "))
    if tebakan == 0:
        break
    elif tebakan < angka_rahasia:
        print("Angka terlalu kecil")
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar")
    else:
        print("Selamat, anda menebak angka dengan benar!")
        break 
if i == 4:
    print(f"Sayang, anda tidak menebak angka dengan benar. Angka rahasianya adalah {angka_rahasia}.")


# Soal 3
N = int(input('N = '))
M = int(input('M = '))

for i in range(N):
    if i % 2 == 0:
        for j in range(M):
            print(f"MOVE to ({i},{j})")
    else:
        for j in range(M - 1, -1, -1):
            print(f"MOVE to ({i},{j})")


            # Soal 4
total_harga = int(input("Masukkan total harga: "))
uang_diberikan = int(input("Masukkan uang yang diberikan: "))

kembalian = uang_diberikan - total_harga

pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

for pecahan in pecahan_uang:
  jumlah_lembar = kembalian // pecahan
  if jumlah_lembar > 0: 
    print(f"{jumlah_lembar} lembar Rp {pecahan:,}")
    kembalian %= pecahan



# Soal 5
serangga_A = int(input("Masukkan populasi awal Serangga A : "))
serangga_B = int(input("Masukkan populasi awal Serangga B : "))
hari = int(input("Masukkan jumlah hari : "))

for hari in range(1, hari + 1) :
    if hari % 2 == 1 :
#hari ganjil
        serangga_A = int(serangga_A * 1.3)
        serangga_B = int(serangga_B * 1.5)
#hari genap
    else: 
        serangga_A = int(serangga_A * 0.8)
        serangga_B =int(serangga_B * 0.6)

    if hari % 5 == 0:
        serangga_A = int(serangga_A * 0.9)
        serangga_B = int(serangga_B * 0.9)
        print(f'Hari {hari} : Predator memakan 10% populasi. ')
    print(f'Hari {hari} : Serangga A = {serangga_A}, Serangga B = {serangga_B}')

