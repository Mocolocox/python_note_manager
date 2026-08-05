#Gestor de notas
notas = []

while True:
    print("\n===== GESTOR DE NOTAS =====")
    print("1. Agregar notas")
    print("2. Ver notas")
    print("3. Salir")
    print("4. Eliminar Nota")
    try:
        usuario = int(input("Elegí una opción: "))
    except ValueError:
        print("Opcion incorrecta, intenta con un numero")
        break
    if usuario == 1:
        notas.append(input("Escribí tu nota:"))
    elif usuario == 2:
        if not notas:
            print("no hay notas, escribe algo primero")
        for nota in notas:
            print(nota)
    elif usuario == 3:
        print("fin del programa")
        break
    elif usuario == 4:
        if not notas:
            print("no hay elementos que eliminar, guarda algo primero")
        else:
            for posicion, nota in enumerate(notas):
                print(posicion,nota)
            try:
                opcion_usuario = int(input("¿que nota desea borrar?(elegir con numeros): "))
                notas.pop(opcion_usuario)
            except ValueError:
                print("Opcion incorrecta, intenta con un numero")
            except IndexError:
                print("intenta con un numero dentro del rango")
    else:
        print("Opcion invalida")