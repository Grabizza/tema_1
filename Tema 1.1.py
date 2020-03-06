# Sa se verifice daca textul introdus de la tastatura de catre un utilizator este un sir de
# caractere de tip string sau un sir de numere. Utilizati instructiunea de tip if-elif-else.
# In cazul in care valoarea este un sir de caractere, afisati pe ecran mesajul “Sirul de
# caractere a fost gasit de Alexandra”, unde Alexandra reprezinta numele vostru
# preluat automat de la tastatura.
# In cazul in care valoarea este un sir de numere afisati pe ecran mesajul “Sirul de
# numere a fost gasit de Alexandra”, unde Alexandra reprezinta numele vostru preluat
# automat de la tastatura.

a = input("Introduceti un sir de caractere:")
b = input("Spune-mi cum te numesti si am sa ghicesc ce tip de caractere ai introdus: ")
if a.isdigit():
    print("Sirul de numere a fost gasit de {}" .format(b)+".")
elif a.isalpha():
    print("Sirul de caractere a fost gasit de {}" .format(b)+".")
else:
    print("N-ai noroc {}!" .format(b))