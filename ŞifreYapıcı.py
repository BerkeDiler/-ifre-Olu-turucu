import string
import random

def get_password_length():
    while True:
        try:
            length = int(input("Harf Uzunlugunu yazin: "))
            return length
        except:
            print("lütfen bir sayı girin.")

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation #Bütün Harfleri bir araya topluyor
    return ''.join(random.choice(all_characters) for i in range(length))

password_length = get_password_length()
print("Oluşturulan şifre: ", generate_password(password_length))


