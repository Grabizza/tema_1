# Creati un program care are ca scop un meniu. Meniul se va selecta prin introducerea
# de la tastaura a unui numar intre 1 si 5 captat intr-o variabila. Prezentati prin afisare
# acest sir de caractere:
# “”” 1 – Afisare lista de cumparaturi
# 2 – Adaugare element
# 3 – Stergere element
# 4 – Sterere lista de cumparaturi
# 5 - Cautare in lista de cumparaturi “””
# Apoi folosindu-va de o constructie if-elif-else afisati: - daca utilizatorul scrie de la
# tastaura 1 afisati “Afisare lista de cumparaturi” - daca utilizatorul scrie de la tastaura 2
# afisati “Adugare element” - daca utilizatorul scrie de la tastaura 3 afisati “Stergere
# element” - daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturit”
# - daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element” - daca utilizatorul
# scrie altceva de la tastaura afisati “Alegerea nu exista. Reincercati”

print("Lista de cumparaturi!\n")
print("1 – Afisare lista de cumparaturi \n2 – Adaugare element \n3 – Stergere element \n4 – Sterere lista de cumparaturi \n5 – Cautare in lista de cumparaturi!\n\n")
a = input("Tastati cifra din dreptul obtiunii dorite: ")
if a == "1":
    print("Afisare lista de cumparaturi:\nbranza \noua \nlapte")
    input("Apasati tasta <enter> pentru a iesi din program!")
elif a == "2":
    print("Adaugare element: ")
    input("Introduceti elementul si apasati tasta <enter>: ")
    input("Apasati tasta <enter> pentru a iesi din program!")
elif a == "3":
    print("Stergere element")
    input("Apasati tasta <enter> pentru a iesi din program!")
elif a == "4":
    print("Stergere lista de cumparaturi")
    input("Apasati tasta <enter> pentru a iesi din program!").
elif a == "5":
    print("Cautare in lista de cumparaturi")
    input("Introduceti cuvantul cheie: ")
    input("Apasati tasta <enter> pentru a iesi din program!")
# elif a != "":
#     print("Alegerea nu exista.")
else:
    print("Alegerea nu exista. Reincercati!")



# if isinstance(a, int):
#     print("{} is an integer".format(a))
# elif isinstance(a, str):
#     print("{} is string".format(a))
# else:
#     print("{} is neither Integer nor string".format(a))



#     print("Afisare lista de cumparaturi:\nbranza \noua \nlapte")
#     input("Apasati tasta <enter> pentru a iesi din program!")
# # elif type(a) != int():
# #     print("Alegerea nu exista! Reincercati!")
# if int(a) == 1:
#      print("Afisare lista de cumparaturi:\nbranza \noua \nlapte")
#      input("Apasati tasta <enter> pentru a iesi din program!")
# elif int(a) == 2:
#      print("Adaugare element: ")
#      input("Introduceti elementul si apasati tasta <enter>: ")
#      input("Apasati tasta <enter> pentru a iesi din program!")
# elif int(a) == 3:
#      print("Stergere element")
#      input("Apasati tasta <enter> pentru a iesi din program!")
# elif int(a) == 4:
#      print("Stergere lista de cumparaturi")
#      input("Apasati tasta <enter> pentru a iesi din program!")
# elif int(a) == 5:
#      print("Cautare in lista de cumparaturi")
#      input("Introduceti cuvantul cheie: ")
#      input("Apasati tasta <enter> pentru a iesi din program!")
# elif type(a) != int() and 0 > a and a > 5:
#     print("Alegerea nu exista! Reincercati!")
