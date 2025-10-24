#nombre = input("Ingrese su nombre: ")
#print("HOLA, ", nombre.upper())

#numero = float(input("Ingrese un número "))
#print(numero + 5)


#nombre1 = input("Ingrese aquí su nombre: ")
#nombre2 = input("Ingrese aquí su apellido: ")

#print("¡Hola,", nombre1, nombre2, "!")

#numero1 = float(input("Ingrese aquí el primer número: "))
#numero2 = float(input("Ingrese aquí el segundo número: "))
#numero3 = float(input("Ingrese aquí el tercer número: "))
#numero4 = float(input("Ingrese aquí el cuarto número: "))
#numero5 = float(input("Ingrese aquí el quinto número: "))

#print("Aquí tiene el promedio de dichos números: ", (numero1 + numero2 + numero3 + numero4 + numero5) / 5)

#frase = input("Escriba aquí su frase: ")

#print ("Aquí tiene su frase en minúsculas: ", frase.lower())

"""while True:
    numero = int(input("Ingrese aquí el número: "))

    if numero % 2 == 0:
        print("Es par.")

    else:
        print("No es par.")
    
    """""


"""numero = int(input("Ingrese aquí el número: "))
suma = 0

while numero != 0:
    suma += numero
    numero = int(input("Siguiente número: "))

print (f"La suma es {suma}")"""

import random
numero_secreto = random.randint(1, 50)
contador = 1
incorrecto = True

print("Adivine el número correcto entre 1 y 50. Tiene cinco intentos")
numero_usuario = int(input("Primer intento: "))


while incorrecto and contador -1 <= 5:
    
    if numero_usuario > numero_secreto:
        contador += 1
        numero_usuario = int(input("Ingrese un número menor: "))
        

    elif numero_usuario < numero_secreto:
        contador += 1
        numero_usuario = int(input("Ingrese un número mayor: "))

    else:
        print(f"¡Ganaste!")
        incorrecto = False
        

if incorrecto == True:
    print(f"¡Te quedaste sin intentos! El número correcto era: {numero_secreto}")
