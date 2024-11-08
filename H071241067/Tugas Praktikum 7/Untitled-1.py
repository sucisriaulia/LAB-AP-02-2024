
     class Karakter:
    def __init__(self, nama, umur, nyawa, skills):
        self.nama = nama
        self.umur = umur
        self.nyawa = nyawa
        self.skills = skills 
        
    def bunuh_diri(self):
        if self.nyawa > 0:
            self.nyawa -= 10
            print(f"{self.nama} melakukan bunuh diri! Nyawa sekarang: {self.nyawa}")
        else:
            print(f"{self.nama} sudah tidak punya nyawa tersisa!")