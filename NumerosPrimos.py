#EJERCICIO 04: Se quiere obtener los numeros primos desde el 0 hasta el 20 utilizando el bucle while.

for num in range (0,20):
 if num > 1:
   cont=0
   i=2
 while i<num and cont==0:
    resto=num%i
    if resto==0:
       cont+=1
    i+=1
 if cont==0:
   print(num)