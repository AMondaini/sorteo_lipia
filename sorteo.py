import os
import json
import random
carpeta = "archivos"
archivo_salida = "usuarios_concursantes.txt"

usernames = set()

for archivo in os.listdir(carpeta):
    if archivo.endswith(".txt"):
        ruta_archivo = os.path.join(carpeta, archivo)
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                try:
                    data = json.loads(linea)
                    if "userName" in data:
                        usernames.add(data["userName"])
                except json.JSONDecodeError:
                    print(f"Error al procesar la línea en {ruta_archivo}")

usernames = list(usernames)

with open(archivo_salida, 'w', encoding='utf-8') as f:
    for username in usernames:
        f.write(username + '\n')

if len(usernames) >= 3:
    usernames_aleatorios = random.sample(usernames, 3)
else:
    usernames_aleatorios = usernames

print("Usernames seleccionados:", usernames_aleatorios)
print(f"La lista completa de usuarios concursantes se ha exportado a {archivo_salida}.")
