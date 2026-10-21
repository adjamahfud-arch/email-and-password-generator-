
def email_vali():
    while True:
       try:
         email_ =str(input("masukkan email anda:")).strip()
         if email_ =="":
            print("pilihan wajib di isi!")
            continue
         if not email_.endswith(".com"):
            print("email harus/ wajib disertai .com!")
            continue
         if not "@gmail" in email_:
             print(f"email anda {email_} tidak meniliki @!")
             continue
         return email_
       except Exception as l:
           print(f"error:{l}")
         
def password():
    while True:
       try:
         word =str(input("buat password:"))
         if word =="":
            print("pilihan wajib di isi!")
            continue
         if not len(word) > 8:
            print(f"passwor anda {word} harus minimal 8 caracter!")
            continue
         return word
       except Exception as e:
           print(f"error:{e}")


if __name__ =="__main__":
   password()
  