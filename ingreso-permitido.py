edad = int(input("Por favor, ingrese la edad del cliente: "))

permitido = True 

if edad >= 18:
    permitido = True
    print ("Puedes ingresar a la discoteca")
else: 
    permitido = False
    print("Lo sentimos mucho, no se puede ingresar a la discoteca siendo menor de edad")
