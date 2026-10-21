from storage import Tampung
from pathlib import Path
import sys
import json

parent =Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent))

import main_validasi as mv

class Cocok:
     def __init__(self,salah: int =0) -> None:
         self.data_base =Tampung.load_file()
         self.kesempatan =3
         self.salah =salah
       
     def cocok(self,email: str ,password: str) -> True | False | None:
         if not self.data_base:
            print("data msih kosong")
            return
         for k in self.data_base:
             if k.email == email and k.password == password:
                print("berhasil masuk")
                return True
             
         print(f"email atau password anda salah")
         self.salah +=1
         return False
       
     def keluar(self):
         if not self.kesempatan > self.salah:
            print("kesempatan habis keluar dari program")
            return True
               
def main():
   cc =Cocok()
   while True:
      mtode =cc.keluar()
      if mtode:
         sys.exit()
      emaill =mv.email_vali()
      keyy =mv.password()
      hasil =cc.cocok(emaill,keyy)
      if hasil:
         break
      else:
         continue
      
if __name__ =="__main__":
   main()
  

                
                