# Creati un program in care utilizatorul sa introduca un numar. Calculati daca numarul
# este pozitiv, zero sau negativ. In cazul in care este pozitiv validati daca este mai mic
# decat 10 si afisati un mesaj de confirmare..Daca numarul este zero afisati “Numarul
# este 0”, iar daca numarul este negativ atunci transformati numarul in numar pozitiv si
# afisati numarul pozitiv.

# Nu functioneaza pentru numere zecimale!

a = input("Introduceti numarul:")
b = (int(a))
c = 0
if b > c:
    print("Numarul este pozitiv!")
elif b == c:
    print("Numarul este 0!")
else:
    d = (b*(-1))
    print("Numarul introdus este negativ! Se va afisa opusul sau: " + str(d))