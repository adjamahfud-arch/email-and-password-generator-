from pathlib import Path
import json
import sys

parent =Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent))


file =Path("simpan_data.json")

class Tampung:
    def __init__(self,email,password,waktu):
        self.email =email
        self.password =password
        self.waktu =waktu
        self.status =None
      
    @classmethod    
    def from_dict(cls,data):
        data_ =cls(data["email"],data["password"],data["waktu"])  
        data_.status =data["status"]
        return data_
      
    @classmethod  
    def load_file(cls):
        try:
          fl =json.loads(
              file.read_text(encoding="utf-8")
          )
          return [cls.from_dict(y) for y in fl]
        except FileNotFoundError:
             return []
        except FileExistsError:
             return []
        except (json.JSONDecodeError, KeyError) as r:
             print(f"file rusak ({r})")
             return []
        except Exception as w:
             print(f"error:{w}")
             return []
     
          
        