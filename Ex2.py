nombre = input("Entrer un nombre: ")
nombre = int(nombre)

#un nombre est premier s'il n'a que lui et un comme diviseur
for i in range(2, nombre, 1):

    resteDivision = nombre%i
    
    if resteDivision != 0:
        print("le nombre est premier")
        
    else:
        print(" le nombre n'est pas premier")
        break
        
         
