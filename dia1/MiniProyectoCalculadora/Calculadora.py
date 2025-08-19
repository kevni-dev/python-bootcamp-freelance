#----Mini proyecto práctico----
print("Calculadora Básica")

#Instrucción para repetir el codigo indefinidamente
while True:
    
    #Pedir opcion para hacer  la operacion correspondiente(en este caso numerales)
    opcion = int(input("Ingrese el numeral de la operacion a elegir\n1.Suma\n2.Resta\n3.Multiplicación\n4.División\n5.Salir\nOpción: "))

    #Opcion para salir del bucle
    if opcion == 5:
        print("Saliendo del programa...")
        break

    #Pedir al usuario el ingreso de los numeros a utilizar
    numero1 = int(input("Ingrese primer numero: "))
    numero2 = int(input("Ingrese segundo numero: "))

    #A cada opcion asinarle su proceso mediante if y mostrar por pantalla
    if opcion == 1:
        print(f"La suma es: {numero1 + numero2}")
    elif opcion == 2:
        print(f"La resta es: {numero1 - numero2}")
    elif opcion == 3:
        print(f"La multiplicación es: {numero1 * numero2}")
    elif opcion == 4:
        #Verificar que el denominador sea diferente de cero, caso contrario, mostrar error
        if numero2 != 0:
            print(f"La division es: {numero1 / numero2}")
        else:
            print("No se puede dividir por 0")
    #Si el usuario ingresa un numeral fuera de las opciones mostrar opcion invalida
    else:
        print("Opción invalida.")
