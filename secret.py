import random
tukka =""

password = input("input desired Password")
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
while(tukka != password):
    tukka = ""
    for letter in password:
        tukka_letter = letters[random.randrange(25)]
        tukka = str(tukka_letter) + str(tukka)
    print(tukka)
print("Password Matched Successfully!!! and the password is *{}* ".format(tukka))
