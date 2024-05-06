import configparser
from pathlib import Path

# Crear un objeto ConfigParser
config = configparser.ConfigParser()

# Leer el archivo como un string para añadir la sección por defecto
archivo = Path("/Users/david/Devsecops/CPCReady/amstrad-console/tests/prueba2/cfg/CPCReady.cfg")

with open(archivo, "r") as f:
    contenido = f.read()

# Si no tiene sección, añadir una por defecto
if not contenido.strip().startswith("["):
    contenido = "[DEFAULT]\n" + contenido

# Leer el contenido con ConfigParser
config.read_string(contenido)

# Obtener el valor de 'MODE' desde la sección 'DEFAULT'
mode = config.get("DEFAULT", "MODE")

print("Valor de MODE:", mode)
