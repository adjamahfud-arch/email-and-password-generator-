import json
from pathlib import Path
import main_validasi as al
from datetime import datetime
import hashlib

file =Path("simpan_data.json")
file_2 =Path("data_backup.json")
format_waktu: str ="%H:%M  %d %A %Y"

class Start:
    def __init__(self,email: str, password: str, waktu: str ="") -> None:
        self.email =email
        self.password =password
        self.waktu =waktu
        self.status =True
      

    def to_dict(self):
        return {
           "email":self.email,
           "password":self.password,
           "waktu":self.waktu,
           "status":self.status
        }
      
    @classmethod
    def from_dict(cls,data):
        data_ =cls(data["email"],data["password"],data["waktu"])
        data_.status =data["status"]
        return data_
      

class Process: 
    def __init__(self):
        self.data_base =self.load()
      
    def load(self):
        try:
          dtap =json.loads(file.read_text(encoding="utf-8"))
          return [Start.from_dict(u) for u in dtap]
          
        except FileExistsError:
             return []
        except FileNotFoundError:
             return []
        except (json.JSONDecodeError, KeyError) as w:
             print(f"file rusak:({w})")
             return []
        except Exception as r:
             print(f"error:{r}")
             return []
          
    def tambah(self,dta):
        self.data_base.append(dta)
      
    def simpan(self):
        try:
          dta =[y.to_dict() for y in self.data_base]
          file.write_text(json.dumps(dta,ensure_ascii=False,indent=2),
          encoding="utf-8"
        )
          return True
        except OSError as o:
            print(f"error {o}")
            return []
        except Exception as l:
            print(f"error;{l}")
            return False
      
      
    def isi(self,email: str,password: str,wakt: str) -> None:
        try:
          name =Start(email,password,wakt)
          self.tambah(name)
          self.simpan()
          if self.simpan():
             print("data berhasil di simpan")
      
        except Exception as r:
            print(f"error:{r}")

class To_hash:
    def __init__(self):
        self.data_hash =self.load_hash()

    def tambah_hash(self,data):
        self.data_hash.append(data)

    def load_hash(self):
        try:
          load_file =json.loads(file_2.read_text(encoding="utf-8"))
          return [Start.from_dict(r) for r in load_file]
          
        except FileNotFoundError:
            print("file belum ada")
            return []
        except (json.JSONDecodeError, KeyError) as jy:
            print(f"file rusak ({jy})")
            return []
        except Exception as cp:
            print(f"error:{cp}")
            return []

    def simpan_hash(self):
        try:
          data_s =[b.to_dict() for b in self.data_hash]
          file_2.write_text(json.dumps(data_s,ensure_ascii=False,indent=2),
           encoding="utf-8"
          )

        except OSError as s:
             print(f"error:{s}")
        except Exception as ect:
             print(f"error:{ect}")

    def isi_hash(self,email_h: str ,password_h: str ,waktu: str) -> None:
        is_hash =Start(email_h,password_h,waktu)
        self.tambah_hash(is_hash)
        self.simpan_hash()
        


class Hash_in:
    @staticmethod
    def hash_(eml,pw,wkt):
        th =To_hash()
        try:
          ubah =hashlib.sha256(eml.encode()).hexdigest()
          ubah_1 =hashlib.sha256(pw.encode()).hexdigest()
          th.isi_hash(ubah,ubah_1,wkt)
        
        except Exception as ec:
             print(f"error:{ec}")  
        
  
      
                  
class Time:
    @staticmethod
    def waktu():
        timee =datetime.now().strftime(format_waktu)
        return timee


def main():
    sk =Process()
    st =Time()
    hi =Hash_in()
    try:
      eml =al.email_vali()
      passwor =al.password()
      timess =st.waktu()
      hi.hash_(eml,passwor,timess)
      sk.isi(eml,passwor,timess)
    except Exception as m:
       print(f"error:{m}")
      
        
if __name__ =="__main__":
   main()  
      
      
      