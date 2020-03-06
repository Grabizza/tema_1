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
input("Pentru afisarea meniului apasati tasta <enter>!\n")
print("1 – Afisare lista de cumparaturi \n2 – Adaugare element \n3 – Stergere element \n4 – Sterere lista de cumparaturi \n5 – Cautare in lista de cumparaturi!\n")
a = input("Tastati cifra din dreptul obtiunii dorite: ")
b = (int(a))
c = 1
d = 2
e = 3
f = 4
g = 5
if b == c:
    print("Afisare lista de cumparaturi:\nbranza \noua \nlapte")
    input("Apasati tasta <enter> pentru a iesi din program!")
elif b == d:
    print("Adaugare element: ")
    input("Introduceti elementul si apasati tasta <enter>: ")
    input("Apasati tasta <enter> pentru a iesi din program!")
elif b == e:
    print("Stergere element")
    input("Apasati tasta <enter> pentru a iesi din program!")
elif b == f:
    print("Stergere lista de cumparaturi")
    input("Apasati tasta <enter> pentru a iesi din program!")
elif b == g:
    print("Cautare in lista de cumparaturi")
    input("Introduceti cuvantul cheie: ")
    input("Apasati tasta <enter> pentru a iesi din program!")
else:
    print("Alegerea nu exista! Reincercati!")
    input("Apasati tasta <enter> pentru a iesi din program!")