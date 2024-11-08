data_penggunaan = float(input("Masukkan jumlah data yang digunakan (GB): "))
waktu_penggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? ").lower()
jenis_pengguna = input("Apakah Anda pengguna Personal atau Bisnis? ")

if data_penggunaan <0 :
    print("input tidak valid")
    exit()
def tentukan_paket(data_penggunaan, waktu_penggunaan, jenis_pengguna):
    if data_penggunaan < 10:
        kategori_penggunaan = "Ringan"
    elif 10 <= data_penggunaan <= 50:
        kategori_penggunaan = "Sedang"
    else:
        kategori_penggunaan = "Berat"
    
    if kategori_penggunaan == "Ringan" and waktu_penggunaan == "off-peak" and jenis_pengguna == "personal":
        return "Paket A"
    elif kategori_penggunaan == "Sedang" and waktu_penggunaan == "peak" and jenis_pengguna == "personal":
        return "Paket B"
    elif kategori_penggunaan == "Berat" and waktu_penggunaan == "peak" and (jenis_pengguna == "personal" or jenis_pengguna == "bisnis"):
        return "Paket C"
    elif kategori_penggunaan == "Berat" and waktu_penggunaan == "off-peak" and jenis_pengguna == "bisnis":
        return "Paket D"
    else:
        return "Tidak ada paket yang cocok"


paket = tentukan_paket(data_penggunaan, waktu_penggunaan, jenis_pengguna)
print("Paket yang sesuai:", paket)



