# Calculadora básica de 5 operaciones
num1 = int(input("Introduzca el primer numero : "))
num2 = int(input("Introduzca el segundo numero: "))

menuCalculadora="============ Menu Calculadora ======================\n"
menuCalculadora+="Indique la operacion a realizar:\n"
menuCalculadora+="1)Sumar\n"
menuCalculadora+="2)Restar\n"
menuCalculadora+="3)Multiplicar\n"
menuCalculadora+="4)Dividir\n"
menuCalculadora+="5)Potencia\n"
menuCalculadora+="6)Cambiar los numeros ingresados\n"
menuCalculadora+="7)Salir de calculadora\n"
menuCalculadora+="===================================================="

eleccion = 0
while eleccion !=7:
    print(menuCalculadora)
    print("Indique la operacion a realizar: ")   
    eleccion =int(input())
    if eleccion == 1:
        print("RESULTADO: ",num1," + ",num2," = ", num1+num2)
    elif eleccion ==2:
        print("RESULTADO: ",num1," - ",num2," = ", num1-num2)
    elif eleccion == 3:
        print("RESULTADO: ",num1," * ",num2," = ", num1*num2)
    elif eleccion ==4:
        print("RESULTADO: ",num1," / ",num2," = ", float(num1/num2))
    elif eleccion ==5:
        print("RESULTADO: ",num1," ^ ",num2," = ", num1 ** num2)
    elif eleccion ==6:
        num1 = int(input("Introduzca el primer numero : "))
        num2 = int(input("Introduzca el segundo numero: "))
    elif eleccion ==7:
        print("Hasta pronto")
        break
