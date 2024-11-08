import re

def is_valid_username(username):
    pattern = r"^[A-Za-z0-9]{5,20}$" 
    return re.search(pattern, username)

def is_valid_email(email):
    pattern = r"^[a-z0-9]+[0-9]*@[a-z]+\.(com|co\.id)$" 
    return re.search(pattern, email)

def is_valid_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9]{8,}$" 
    return re.search(pattern, password)

#---------
# username = input("Masukkan username: ")
# if is_valid_username(username):
#     email = input("Masukkan email: ")
#     if is_valid_email(email):
#         password = input("Masukkan password: ")
#         if is_valid_password(password):
#             print(f"\nRegistrasi berhasil! Selamat datang {username}") 
#         else:
#             print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")
#     else:
#         print("\nEmail yang kamu input tidak valid. Registrasi gagal!")
# else:
#     print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")


Class Shape:
     def __init__(self,side,color):
         self.side = side
         self.color = color

     def expand_size(self,added_size):
         self.side+=added_size

    def count_area(self):
        self.side*=4
        print(f"The are is(self.side)")

circle = Circle(12,"red",7)
circle.count_area()