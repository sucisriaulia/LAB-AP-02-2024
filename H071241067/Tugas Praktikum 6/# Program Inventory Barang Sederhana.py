# Program Inventory Barang Sederhana

# Inisialisasi data barang dalam bentuk dictionary
inventory = {}

# Fungsi untuk menambah barang
def tambah_barang():
    kode = input("Masukkan kode barang: ")
    nama = input("Masukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah barang: "))
    harga = float(input("Masukkan harga barang: "))
    
    inventory[kode] = {
        "nama": nama,
        "jumlah": jumlah,
        "harga": harga
    }
    print(inventory)
    print(f"Barang {nama} berhasil ditambahkan!\n")

# Fungsi untuk menghapus barang
def hapus_barang():
    kode = input("Masukkan kode barang yang ingin dihapus: ")
    if kode in inventory:
        del inventory[kode]
        print(f"Barang dengan kode {kode} berhasil dihapus!\n")
    else:
        print("Barang tidak ditemukan!\n")

# Fungsi untuk menampilkan daftar barang
def tampilkan_daftar_barang():
    if not inventory:
        print("Tidak ada barang di dalam inventory.\n")
    else:
        print("Daftar Barang:")
        for kode, barang in inventory.items():
            print(f"Kode: {kode}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")
        print() # Line break

# Fungsi untuk mencari barang
def cari_barang():
    kode = input("Masukkan kode barang yang ingin dicari: ")
    if kode in inventory:
        barang = inventory[kode]
        print(f"Barang ditemukan! Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}\n")
    else:
        print("Barang tidak ditemukan!\n")

# Fungsi untuk mengupdate data barang
def update_barang():
    kode = input("Masukkan kode barang yang ingin diupdate: ")
    if kode in inventory:
        nama_baru = input("Masukkan nama barang baru: ")
        jumlah_baru = int(input("Masukkan jumlah barang baru: "))
        harga_baru = float(input("Masukkan harga barang baru: "))
        
        inventory[kode] = {
            "nama": nama_baru,
            "jumlah": jumlah_baru,
            "harga": harga_baru
        }
        print(f"Barang dengan kode {kode} berhasil diupdate!\n")
    else:
        print("Barang tidak ditemukan!\n")

# Menu utama program
def menu():
    while True:
        print("=== Program Inventory Barang ===")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Daftar Barang")
        print("4. Cari Barang")
        print("5. Update Data Barang")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            hapus_barang()
        elif pilihan == "3":
            tampilkan_daftar_barang()
        elif pilihan == "4":
            cari_barang()
        elif pilihan == "5":
            update_barang()
        elif pilihan == "6":
            print("Terima kasih telah menggunakan program inventory!")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih menu yang benar.\n")

# Menjalankan menu
menu()