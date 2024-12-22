import random
karakterler = "+-/*!#½$?*=@abcdefghijklmnopqrstuvwxyzABCDEFGHİJKLMNOPQRSTUVWYZ1234567890"

sayi = int(input("Kaç karakterlik bir şifre oluşturmak istersiniz?"))
sifre = ""           
for i in range(sayi):
    sifre = sifre + random.choice(karakterler)

print(sifre)
print("Şireniz başarılı bir şekilde oluşturuldu!")