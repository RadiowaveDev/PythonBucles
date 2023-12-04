#Desarrolla un programa que genere un numero aleatorio entre 1 y 100.
# El usuario tendra que adivinar el numero.
# Provea pistas tales como "mas alto" o "mas bajo" despues de cada respuesta incorrecta.
# Puede utilizar un bucle "while" infinito para pedir el numero al usuario hasta que adivine el correcto

import random
k=random.randrange(1,100)
cond=True
print("Adivine el numero entre 1 y 100: ")
while(cond):
    num = int(input("Ingrese su numero elegido: "))
    if(num<k): print("Mas Alto")
    if(num>k): print("Mas Bajo")
    if(num==k):
        print("Acertaste!")
        print("Fin del juego!")
        cond=False
    resp= input("Desea volver a intertarlo? (SI/NO): ")
    if(resp=="NO"):
        print("Fin del juego!")
        cond=False
    else:
        print("==========================================")
  


