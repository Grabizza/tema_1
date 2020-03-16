# Creati un program in care utilizatorul sa introduca un numar. Calculati daca numarul
# este pozitiv, zero sau negativ. In cazul in care este pozitiv validati daca este mai mic
# decat 10 si afisati un mesaj de confirmare..Daca numarul este zero afisati “Numarul
# este 0”, iar daca numarul este negativ atunci transformati numarul in numar pozitiv si
# afisati numarul pozitiv.

# Nu functioneaza pentru numere zecimale!

a = input("Introduceti numarul: ")
b = (float(a))
if b > 0 and b > 10:
    print("Numarul este pozitiv si este mai mare decat 10!")
    input("Apasati tasta <enter> pentru a iesi din program!")
elif b > 0 and b < 10:
    print("Numarul este pozitiv si este mai mic decat 10!")
    input("Apasati tasta <enter> pentru a iesi din program!")
elif b == 0:
    print("Numarul este 0!")
    input("Apasati tasta <enter> pentru a iesi din program!")
else:
    d = (b*(-1))
    print("Numarul introdus este negativ! Se va afisa opusul sau: " + str(d))
    input("Apasati tasta <enter> pentru a iesi din program!")