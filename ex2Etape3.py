#Etape 1
texte = input("insérer un texte: \n")

#convertir a un ens
#list = set(a)

# separer les mots grâce a un espace
mots = texte.split()
#compter les occurences dse caractères

def compterDesMots(mots):
    dico = {}
    for mot in mots:
        #si le mots actuel (mot) est déjà une clé dans le dictionnaire dico
        if mot in dico:
            #augmente le nombre de ce mot
            dico[mot] += 1

            #si on la rencontre pour la première fois
        else:
            dico[mot] = 1

    return dico

result = compterDesMots(mots)
print(result)