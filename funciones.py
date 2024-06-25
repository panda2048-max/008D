import json

def Agregar_Usuario(nombre:str,email:str,fecha_de_registro:str):
    with open("biblioteca.json", mode="r") as AgregarJson:
        LeerJson = json.load(AgregarJson)

        usuario = {
            "UsuarioID": len(LeerJson["Usuario"]) + 1,
            "Nombre":nombre,
            "Email":email,
            "FechaRegistro":fecha_de_registro
        }
        LeerJson["Usuario"].append(usuario)

    with open("biblioteca.json", mode="w") as AgregarJson:
        json.dump(LeerJson,AgregarJson, indent=4)
        print("usuario agregado correctamente ")

def editar_usuario(UsuarioID:int,nombre:str,email:str,fecha_de_registro:str):
    with open("biblioteca.json", mode="r") as editarJson:
        LeerJson = json.load(editarJson)
        Cliente_encontrado = False
        for i in LeerJson["Usuario"]:
            if i["UsuarioID"] == UsuarioID:
                i["Nombre"] = nombre
                i["Email"] = email
                i["FechaRegistro"] = fecha_de_registro
                Cliente_encontrado =  True
                break
        if not Cliente_encontrado:
            print("la id no se encuentra disponible ")
        else:
            with open("biblioteca.json", mode="w") as editarJson:
                json.dump(LeerJson,editarJson, indent=4)
                print("usuario editado correctamente ")


def eliminar_usuario(UsuarioID:int):
    with  open("biblioteca.json", mode="r") as eliminarjson:
        LeerJson = json.load(eliminarjson)
        cliente_encontrado = False
        for i,usuario in enumerate(LeerJson["Usuario"]):
            if usuario["UsuarioID"] == UsuarioID:
                LeerJson["Usuario"].pop(i)
                cliente_encontrado = True
                break
        if not cliente_encontrado:
            print(" no se encontro al cliente que desea eliminar ")
        else:
            for j in range(i,len(LeerJson["Usuario"])):
                LeerJson["Usuario"][j]["UsuarioID"] -= 1

            with open("biblioteca.json", mode="w") as eliminarjson:
                json.dump(LeerJson,eliminarjson, indent=4)
                print(" el usuario a sido eliminado")

def ver_usuarios(ver_usuario:str):
    with  open("biblioteca.json", mode="r") as ver_usuariojson:
        LeerJson = json.load(ver_usuariojson)
        print(LeerJson["Usuario"])

def ver_reporte(verReport:str):
    with open("Recursosbibliotecalibro.json", mode="r") as verJson:
        leerJson = json.load(verJson)
        print(leerJson)