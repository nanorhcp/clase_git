while True:
    numero_usuario = (input("Ingresa un número entero para iniciar el programa: "))


    if numero_usuario.isdigit():

        numero_entero = int(numero_usuario)

        if numero_entero == 0:
            print(("Por favor, ingresa un número válido: "))

        entrada_usuario = input(str("Ahora, ingresa una palabra o frase: "))
        caracteres = len(entrada_usuario)

        print(f"Tu palabra o frase tiene {caracteres} caracteres")

        factorial = 1

        for i in range(1, caracteres + 1):
            factorial = factorial * i

        print(f"El factorial de dichos caracteres es: {factorial}")

        if factorial % 2 == 0:
            print(f"Este número es par.")
        else:
            print(f"Este número es impar.")




else:
    print(f"Error. {numero_usuario} no es válido.")

