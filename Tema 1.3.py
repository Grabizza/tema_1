# Creati un program in care utilizatorul sa introduca un an. Calculati daca anul este
# bisect sau nu si afisati un raspuns in acest sens. OBS. Un an bisect se imparte exact
# la 4 (fara rest).


a = input("Introduceti anul:")
b = ((int(a)) / 4)

if b.is_integer():
    print("Anul este bisect!")
else:
    print("Anul nu este bisect!")