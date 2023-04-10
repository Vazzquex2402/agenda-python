tareas = {}

# Función para agregar una tarea a la agenda
def agregar_tarea():
    dia = input("¿En qué día tienes la tarea? (formato DD/MM/YYYY): ")
    tarea = input("¿Qué tarea tienes que hacer? ")
    tareas[dia] = tarea
    print("Tarea agregada correctamente a la agenda.")

# Función para mostrar las tareas de la agenda
def mostrar_tareas():
    if len(tareas) == 0:
        print("No hay tareas en la agenda.")
    else:
        print("Tareas en la agenda:")
        for dia, tarea in tareas.items():
            print("- " + dia + ": " + tarea)

while True:

    accion = input("¿Qué acción desea realizar? (agregar/mostrar/salir): ")
     
    if accion == "agregar":
        agregar_tarea()
    elif accion == "mostrar":
        mostrar_tareas()
    elif accion == "salir":
        break
    else:
        print("Acción no reconocida. Por favor, inténtelo de nuevo.")
