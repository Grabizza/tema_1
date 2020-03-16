# Sa se verifice daca textul introdus de la tastatura de catre un utilizator este un sir de
# caractere de tip string sau un sir de numere. Utilizati instructiunea de tip if-elif-else.
# In cazul in care valoarea este un sir de caractere, afisati pe ecran mesajul “Sirul de
# caractere a fost gasit de Alexandra”, unde Alexandra reprezinta numele vostru
# preluat automat de la tastatura.
# In cazul in care valoarea este un sir de numere afisati pe ecran mesajul “Sirul de
# numere a fost gasit de Alexandra”, unde Alexandra reprezinta numele vostru preluat
#

# * nu am reusit sa rezolv problema cand am mai multe numere zecimale in sir

a = input("Spune-mi cum te numesti: ")
b = input("Introduceti un sir de caractere: ")
c = b.replace("-","").replace(" ","")
if c.isdigit():
    print("Sirul de numere a fost gasit de {}" .format(a)+".")
    input("Apasati tasta <enter> pentru a iesi din program!")
elif c.isalpha():
    print("Sirul de caractere a fost gasit de {}" .format(a)+".")
    input("Apasati tasta <enter> pentru a iesi din program!")
elif float(c):
    print("Sirul de numere a fost gasit de {}".format(a) + ".")
    input("Apasati tasta <enter> pentru a iesi din program!")
else:
    print("Ai introdus un sir mixt de caractere {}!" .format(a))
    input("Apasati tasta <enter> pentru a iesi din program!")