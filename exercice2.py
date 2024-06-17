prenom = input("entrer votre prénom: ")
age = input("entree votre âge: ")

age = int(age)

if age>=18:
    print("Vous êtes majeur, vous avez le droit de voter")
else:
    print("Vous êtes mineur. Pour voter, il faut attendre la majorité")