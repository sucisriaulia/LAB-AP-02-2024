nilai = float(input("Masukkan nilai akhir :"))
if nilai > 100 or nilai <0 :
    print("inputan tidak valid")
    exit()

else : 
    persentase = float(input("Masukkan persentase kehadiran :"))
    tambahan = float(input("Masukkan nilai rata rata tugas tambahan :"))

    if persentase < 75 :
        status = "Tidak lulus : kehadiran kurang dari 75%"
    elif nilai >= 85 :
        status = "Lulus dengan predikat A"
    elif nilai >= 70 : 
        status = "Lulus dengan predikat B"
    elif nilai >= 60 :
        status = ("Lulus dengan predikat c ")
    else:
        status = "Lulus dengan predikat c " if tambahan >= 70 else " Tidak lulus"

print(f"{status}")