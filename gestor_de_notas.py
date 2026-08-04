#Gestor de notas
notas = []

while True: 
    print("\n===== GESTOR DE NOTAS =====")
    print("1. Agregar notas")
    print("2. Ver notas")
    print("3. Salir")
    print("4. Eliminar Nota")

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
    elif usuario == 4:
        if notas == []:
            print("no hay elementos que eliminar, guarda algo primero")
        else:
            for posicion, nota in enumerate(notas):
                print(posicion,nota)
            opcion_usuario = int(input("¿que nota desea borrar?(elegir con numeros): "))
            notas.pop(opcion_usuario)
    else: 
        print("Opcion invalida")