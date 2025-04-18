while True:
    print ("Calculadora")
    print ("1.Suma")
    print ("2.Resta")
    print ("3.Multiplicacion")
    print ("4.Division")
    print ("5.Potencia")
    print ("6.Salir")
    
    opcion = input ("Elige una opcion (1-6):")
    
    if opcion == "6":
        print ("Hasta la proxima")
        break
    
    num1=float(input ("primerNumero"))
    num2=float(input("segundoNumero"))
    if opcion == "1":
        print (f"Resultado: {num1+num2}")
    elif opcion == "2":
        print (f"Resultado: {num1-num2}")
    elif opcion == "3":
        print (f"Resultado:{num1*num2}")
    elif opcion == "4":
        if num2 !=0:
            print (f"Resultado:{num1/num2}")
        else:
            print ("No se puede dividir por cero.")
    elif opcion == "5":
        print (f"Resultado{num1**num2}")
    else:
        print("Opcion no valida, por favor elige una opcion entre 1 y 6")
