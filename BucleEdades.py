#EJERCICIO 03: A una conferencia sobre ITIL, asistieron personas de diferentes edades y géneros.
# Construir un algoritmo que muestre: a) Cuántas personas asistieron al congreso. 
# b) Cuántos hombres y cuantas mujeres. 
# c) Promedio de edades por género. d) La edad de la persona más joven que asistió al congreso.
# Ingresar datos hasta que se ingrese la edad cero.

cond = True
#Masculino (mas) y Femenino (fem)
mas = 0
fem = 0
#Acumulador Edades asistentes masculino y femenino 
edsummas = 0
edsumfem = 0
edmenor = 120 

while(cond):
  asised = int(input("Ingrese edad "))
  if asised == 0:
    cond = False
    break
  
  asisgen = input("Ingrese genero ")
  if asisgen == "masculino":
    mas += 1
    edsummas += asised
  if asisgen == "femenino":
    fem += 1
    edsumfem += asised
  if edmenor > asised:
    edmenor = asised

print('la cantidad de asistentes es: ' + str((mas+fem)) )
print('la cantidad de hombres: ' + str(mas) )
print('la cantidad de mujeres: ' + str(fem) )

if mas != 0:
  edprommas = edsummas / (mas)
  print('la edad promedio de los hombres es '+ str(edprommas))
if fem != 0:
  edpromfem = edsumfem / (fem)
  print('la edad promedio de las mujeres es '+ str(edpromfem))
print('la edad de la persona mas joven es: ' + str(edmenor) )