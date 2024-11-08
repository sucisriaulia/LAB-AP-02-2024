# def caesar_cipher(teks, pergeseran):
#     hasil = ""

#     for karakter in teks:
#         if karakter.islower():
#             geser = chr((ord(karakter) - ord('a') + pergeseran) % 26 + ord('a'))
#             hasil += geser
#         elif karakter.isupper():
#             geser = chr((ord(karakter) - ord('A') + pergeseran) % 26 + ord('A'))
#             hasil += geser
#         else:
#             hasil += karakter

#     return hasil

# input_teks = input("Masukkan string : ")
# nilai_pergeseran = int(input("Masukkan jumlah pergeseran: "))

# teks_terenkripsi = caesar_cipher(input_teks, nilai_pergeseran)

# print("Teks  :", input_teks)
# print("Shift :", nilai_pergeseran)
# print("Cipher:", teks_terenkripsi)


# Fungsi untuk mengenkripsi string menggunakan Caesar Cipher
def caesar_cipher_enkripsi(teks, shift):
    hasil = ""  # Variabel untuk menyimpan hasil enkripsi
    
    # Looping untuk setiap karakter dalam string
    for karakter in teks:
        # Jika karakter adalah huruf kecil
        if karakter.islower():
            # Menggeser karakter dengan 'shift' dan melingkar kembali jika melampaui 'z'
            hasil += chr((ord(karakter) - ord('a') + shift) % 26 + ord('a'))
        
        # Jika karakter adalah huruf besar
        elif karakter.isupper():
            # Menggeser karakter dengan 'shift' dan melingkar kembali jika melampaui 'Z'
            hasil += chr((ord(karakter) - ord('A') + shift) % 26 + ord('A'))
        
        # Jika karakter adalah angka, tetap tidak berubah
        elif karakter.isdigit():
            # Menambahkan angka langsung tanpa perubahan
            hasil += karakter
        
        # Jika karakter adalah karakter spesial (non-alfabet), tetap tidak berubah
        else:
            hasil += karakter
    
    return hasil

# Input dari pengguna
teks = input("Masukkan teks yang ingin dienkripsi: ")
shift = int(input("Masukkan jumlah pergeseran (shift): "))

# Memanggil fungsi enkripsi dan menampilkan hasilnya
hasil_enkripsi = caesar_cipher_enkripsi(teks, shift)
print("Hasil enkripsi:", hasil_enkripsi)