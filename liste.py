entier = [39, 2, 5, 8, 9, 19, 12, 4, 23]

for i in entier:
    print(i)
    
nombre = input("entrer un nombre: \n")

if nombre in entier:
    print("Le nombre"+ " " +nombre+ " " + "est bien là")
else:
    print("Le nombre" + " " +nombre+ " " + "n'est pas là")


