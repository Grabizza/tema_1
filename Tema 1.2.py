# Creati un program in care utilizatorul sa introduca un numar. Validati daca acest
# numar este par sau impar si afisati un raspuns in acest sens.

# Programul nu functioneaza cu numere zecimale

a = input("Introduceti un numar:")
b = ((int(a)) / 2)

if b.is_integer():
    print("Numarul introdus este un numar par!")
else:
    print("Numarul introdus este numar impar!")