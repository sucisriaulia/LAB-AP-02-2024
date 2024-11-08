a = int(input("Masukkan panjang sisi pertama :"))
b = int(input("Masukkan panjang sisi kedua :"))
c = int(input("Masukkan panjang sisi ketiga :"))


if a<0 or b<0 or c<0 :
    print("invalid karena ada input di bawah")
    exit()
if a+b > c and a+c > b and b+c >a:
    if a == b == c:
        print("Segitiga sama sisi")
    elif a==b or b == c or c==a :
        print("Segitiga sama kaki")
    else:
        print("Segitiga sembarang")
else:
    print("Tidak dapat membentuk segitiga yang valid")
