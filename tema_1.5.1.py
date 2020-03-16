print("Lista de cumparaturi!\n")
print("1 – Afisare lista de cumparaturi \n2 – Adaugare element \n3 – Stergere element \n4 – Sterere lista de cumparaturi \n5 – Cautare in lista de cumparaturi!\n\n")
a = True
while a:
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
          input("Apasati tasta <enter> pentru a iesi din program!")
     elif a == "5":
          print("Cautare in lista de cumparaturi")
          input("Introduceti cuvantul cheie: ")
          input("Apasati tasta <enter> pentru a iesi din program!")
     elif a != "":
          print("Alegerea nu exista! Reincercati!\n")