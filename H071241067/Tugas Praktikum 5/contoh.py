# Soal 1
# Input jarak tempuh
jarak = float(input("Masukkan jarak tempuh (km): "))

# Menghitung biaya berdasarkan jarak
if jarak < 0:
    print("Jarak tidak bisa negatif.")
elif jarak <= 10:
    biaya = 10000
elif jarak <= 20:
    biaya = 10000 + (jarak - 10) * 2500
elif jarak <= 35:
    biaya = 10000 + 10 * 2500 + (jarak - 20) * 1000
elif jarak <= 40:
    biaya = 50000
else:
    print("Transportasi Supriamir Groups tidak dapat melayani karena di luar jangkauan.")
    biaya = None

# Menampilkan hasil jika biaya telah dihitung
if biaya is not None:
    print("Biaya yang harus dibayar: Rp", biaya)


# Soal 2
# Input nilai n
n = int(input("Masukkan nilai n: "))

# Daftar untuk menyimpan elemen
fib_sequence = []

# Menghitung deret Fibonacci
for i in range(n):
    if i == 0:
        fib_sequence.append(0)
    elif i == 1:
        fib_sequence.append(1)
    else:
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)

# Format output
print("Elemen pertama hingga elemen ke-n dalam A adalah:", fib_sequence)


# Soal 3
# Input jenis-jenis koin
koin = input("Masukkan 8 jenis koin (A-Z): ")

# Memastikan input terdiri dari 8 karakter
if len(koin) != 8:
    print("Input harus terdiri dari 8 karakter.")
else:
    # Menghitung frekuensi setiap jenis koin
    frekuensi = {}
    for i, jenis in enumerate(koin):
        if jenis in frekuensi:
            frekuensi[jenis].append(i + 1)  # Menyimpan nomor koin (1-8)
        else:
            frekuensi[jenis] = [i + 1]

    # Mencari jenis koin yang muncul satu kali
    for jenis, nomor in frekuensi.items():
        if len(nomor) == 1:
            print("Koin yang berbeda jenis berada di nomor:", nomor[0])
            break