a = "*"
nombreDemande = input("Entrer un nombre de votre choix: ")
nombreDemande = int(nombreDemande)

for i in range(0, nombreDemande,1):
    print(a * (i+1))