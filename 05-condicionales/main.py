#Condicional IF
print("Ejemplo 1")
color = "verde"
#color = input("Adivina un color")
if color == "rojo":
    print("El colo es ROJO")
else:
    print("El color no es ROJO")


#IF anidados
print("Ejemplo 2")
nombre = "Victor Robles"
ciudad = "Barcelona"
continente ="Asia"
edad = 17
mayoria_edad = 18
if edad >= mayoria_edad:
    #bloque 1
    print(f"{nombre} es mayor de edad")
    if continente == "Europa":
        print(f"El usuario es europeo y de la {ciudad}")
    else:
        print("No es europeo")

else:
    print(f"{nombre} NO es mayor de edad")


#Elif
