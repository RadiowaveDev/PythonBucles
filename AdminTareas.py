# Implemente un administrador de tareas pendientes basico.
# El programa debe permitir al usuario agregar tareas, ver la lista de pendientes y marcarlas como completadas.
# Utilice un diccionario donde las tareas sean los keys y el estado sus valores
# diccionarioTareas = {tareas:estado} 
# (verdadero para completado y falso para pendiente).
# Use bucles y condicionales para interaccion con el usuario

menuTareas="============ Menu Tareas =============\n"
menuTareas+="1. Agregue tareas al administrador de tareas\n"
menuTareas+="2. Visualice lista de pendientes\n"
menuTareas+="3. Modifique tareas pendientes\n"
menuTareas+="4. Salir\n"
menuTareas+="============================================="

cond=True
diccionarioTareas={}
def agregarTarea():
    cant=int(input("Cuántas tareas desea agregar?: "))
    for i in range(cant):
        tarea=input(f"Defina la tarea {i+1}: ")
        estado=input("completado o pendiente? ")
        diccionarioTareas[tarea]=estado
        print("-------------------------------------")

def mostrar_pendientes():
    print("=====Lista de tareas pendientes==========")
    for tarea, estado in diccionarioTareas.items():
        if estado == 'pendiente':
            print(f"- {tarea}")
    print("---------------------------------------")       

def modificar_pendientes():
    print("=====Lista de tareas pendientes==========")
    for i, (tarea, estado) in enumerate(diccionarioTareas.items()):
        if estado == 'pendiente':
            print(f"{i + 1}. {tarea} - Estado: {estado}")
            opcion = input("¿Marcar como completada? (s/n): ").lower()
            if opcion == 's':
                diccionarioTareas[tarea] = 'completado'
                print(f"Tarea '{tarea}' marcada como completada.")
            elif opcion == 'n':
                print(f"No se modificó el estado de la tarea '{tarea}'.")
            else:
                print("Opción no válida. No se realizó ninguna modificación.")
    print("----------------------------------------")


while(cond):
    print(menuTareas)
    opc=int(input("Ingrese la función que desee realizar: "))
    if opc==1:
        agregarTarea()
    elif opc==2:
        mostrar_pendientes()
    elif opc==3:
        modificar_pendientes()
    elif opc==4:
        cond=False
            
