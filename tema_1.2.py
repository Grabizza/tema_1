# Creati un program in care utilizatorul sa introduca un numar. Validati daca acest
# numar este par sau impar si afisati un raspuns in acest sens.

# Programul nu functioneaza cu numere zecimale

a = input("Introduceti un numar: ")
if (int(a) % 2 > 0):
    print("Numarul introdus este un numar impar!")
    input("Apasati tasta <enter> pentru a iesi din program!")
else:
    print("Numarul introdus este numar par!")
    input("Apasati tasta <enter> pentru a iesi din program!")