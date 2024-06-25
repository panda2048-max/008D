import json
libros = {
    "ficcion":3,
    "realismo":0,
    "novela":1,
    "poesia":0,
    "teatro":2,
    "ensayo":3,
    "historia":2,
    "bibiografia":1,
    "ciencia ficcion":3,
    "fantasia":3,
    "literatura culinaria":1,
    "cuento":1
}

with open("Recursosbibliotecalibro.json", mode="w") as reportjson:
    json.dump(libros,reportjson, indent=4)

