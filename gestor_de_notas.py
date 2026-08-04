#Gestor de notas
notas = []

while True: 
    print("\n===== GESTOR DE NOTAS =====")
    print("1. Agregar notas")
    print("2. Ver notas")
    print("3. Salir")

    usuario = int(input("Elegí una opción: "))
    if usuario == 1: 
        notas.append(input("Escribí tu nota:"))
    elif usuario == 2:
        if notas == []: 
            print("no hay notas, escribe algo primero")
        for nota in notas:
            print(nota)
    elif usuario == 3:
        print("fin del programa")
        break
    else: 
        print("Opcion invalida")