from funciones import *

menu = ("agregar","editar","eliminar","buscar","reporte","salir")
contador = 0
for i in menu:
    contador += 1
    print(f"[{contador}].-{i}")

while True:

    opcion = int(input("ingrese una opcion: "))

    if opcion == 1:
        nombre = str(input("ingrese un nuevo nombre "))
        email = str(input("ingrese un nuevo email "))
        fecha_de_registro = str(input("ingrese la nueva fecha de registro "))
        Agregar_Usuario(nombre,email,fecha_de_registro)
    elif opcion == 2:
        UsuarioID = int(input("ingrese una id "))
        nombre = str(input("ingrese un nuevo nombre "))
        email = str(input("ingrese un nuevo email "))
        fecha_de_registro = str(input("ingrese la nueva fecha de registro "))
        editar_usuario(UsuarioID,nombre,email,fecha_de_registro)
    elif opcion == 3:
        UsuarioID = int(input("ingrese una id "))
        eliminar_usuario(UsuarioID)
    elif opcion == 4:
        ver_usuario = str(input("presione cualquier boton si desea ver a los usuario "))
        ver_usuarios(ver_usuario)
    elif opcion == 5:
        verReport = str(input("presione caulquiere boton si desea ver el reporte"))
        ver_reporte(verReport)
    elif opcion == 6:
        print("saliendo del sistema")
        break