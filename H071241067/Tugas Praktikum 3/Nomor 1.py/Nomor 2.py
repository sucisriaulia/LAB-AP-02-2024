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