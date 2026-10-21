import json
from pathlib import Path
import main_validasi as al
from datetime import datetime

file =Path("simpan_data.json")
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
          
          
    def simpan(self):
        try:
          dta =[y.to_dict() for y in self.data_base]
          file.write_text(json.dumps(dta,ensure_ascii=False,indent=2),
          encoding="utf-8"
        )
          return True
          
        except OSError as o:
            print(f"error:{o}")
            return False
          
        except Exception as l:
            print(f"error;{l}")
            return False
          
    def tambah(self,dta):
        self.data_base.append(dta)
      
    def isi(self,email: str,password: str,wakt: str) -> None:
        try:
          name =Start(email,password,wakt)
          self.tambah(name)
          self.simpan()
          if self.simpan():
             print("data berhasil di simpan")
      
        except Exception as r:
            print(f"error:{r}")
          
class Time:
    @staticmethod
    def waktu():
        timee =datetime.now().strftime(format_waktu)
        return timee


def main():
    sk =Process()
    st =Time()
    try:
      eml =al.email_vali()
      passwor =al.password()
      timess =st.waktu()
      sk.isi(eml,passwor,timess)
    except Exception as m:
       print(f"error:{m}")
      
        
if __name__ =="__main__":
   main()  
      
      
      