# import random

# def ambil_kartu():
#     deck = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]
#     return random.choice(deck)

# def main():
#     print("Welcome to Blackjack!")
    
#     kartu_pemain = ambil_kartu()
#     print(f"Kartu anda sekarang adalah: {kartu_pemain}")
    
#     while True:
#         pilihan = input("Apakah masih akan mengambil kartu? (y/n) ").lower()
#         if pilihan == 'y':
#             kartu_pemain = kartu_pemain + ambil_kartu()
#             print(f"Kartu anda sekarang adalah: {kartu_pemain}")
#             if kartu_pemain > 21:
#                 print("Anda kalah, kartu anda melebihi 21.")
#                 return
#         elif pilihan == 'n':
#             break
#         else:
#             print("Input tidak valid. Masukkan 'y' untuk ya atau 'n' untuk tidak.")
    
#     kartu_dealer = ambil_kartu()
#     print(f"Kartu dealer adalah: {kartu_dealer}")
    
#     while kartu_dealer < 17:
#         kartu_dealer = kartu_dealer + ambil_kartu()
#         print(f"Kartu dealer sekarang adalah: {kartu_dealer}")
    
#     if kartu_dealer > 21:
#         print("Anda menang!")
#     elif kartu_dealer > kartu_pemain:
#         print("Dealer menang!")
#     elif kartu_dealer < kartu_pemain:
#         print("Anda menang!")
#     else:
#         print("Seri!")

# main()

# Soal 2
s1 = "Abc"
s2 = "Xyz"

position = s1.find(s2)
print("posisi karakter ada pada index ke",position)
