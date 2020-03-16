# Creati un program in care utilizatorul sa introduca un an. Calculati daca anul este
# bisect sau nu si afisati un raspuns in acest sens. OBS. Un an bisect se imparte exact
# la 4 (fara rest).


a = input("Introduceti un an între 1582 și 4818: ")

if int(a) % 100 == 0 and int(a) % 4 == 0 and int(a) % 400 == 0:
    print("Anul este bisect conform calendarului Gregorian!")
    input("Apasati tasta <enter> pentru a iesi din program!")
elif int(a) % 100 == 0 and int(a) % 4 == 0 and int(a) % 400 > 0:
    print("Anul nu este bisect conform calendarului Gregorian!")
    input("Apasati tasta <enter> pentru a iesi din program!")
elif int(a) % 4 == 0:
    print("Anul este bisect conform calendarului Gregorian!")
    input("Apasati tasta <enter> pentru a iesi din program!")
else:
    print("Anul nu este bisect conform calendarului Gregorian!")
    input("Apasati tasta <enter> pentru a iesi din program!")