num1=float(input ("primerNumero"))
operacion=input("operacion (+,-,/,%)")
num2=float(input("segundoNumero"))
if operacion == '+':
    print (num1+num2)
elif operacion == '-':
    print (num1-num2)
elif operacion == '%':
    print (num1%num2)
elif operacion == '/':
    if num2 !=0:
        print(num1/num2)
    else:
        print ("No se puede dividir por 0")
else:
    print ("Operacion no valida")
