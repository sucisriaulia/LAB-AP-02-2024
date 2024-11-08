#Soal 1
n = int(input('Masukkan Jumlah Baris :'))
 
#Mencetak Bagian Atas Segitiga
for i in range(n // 2) if n % 2 == 0 else range(n // 2 + 1) :
    print('  ' * (n // 2 - i - (n % 2 == 0)) + ' *' * (2 * i + 1))

#Mencetak Bagian Bawah Segitiga
for i in range(n // 2 - 1, -1, -1):
    print('  ' * (n // 2 - i - (n % 2 == 0)) + ' *' * (2 * i + 1))

#  1soal
# n = int(input("Masukkan Jumlah Baris: "))

# if n%2==0: 
#     for i in range(1, n//2 + 1):
#          print(" " * (n//2 - i),) 
#          print("* " * (2*1 - 1))
#     for i in range(n//2, 0, -1): 
#         print(" "* (n//2 - i), end="")
#         print("* " *(2*11))

# else: 
#     for i in range(1, n//2 + 2): 
#         print(" "*((n//2+1) - i), end="")
#         print("* " * (2*1-1))

# for i in range(n//2, 0, -1): 
#     print(" "((n//2+1) - i), end="") 
#     print(" " * (2*1 - 1))