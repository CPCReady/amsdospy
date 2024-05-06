import os
import configparser
from pathlib import Path

def readKey(File, key, default="Key not found"):
    config = configparser.ConfigParser()
    archivo = Path(File)
    with open(archivo, "r") as f:
        contenido = f.read()
    if not contenido.strip().startswith("["):
        contenido = "[DEFAULT]\n" + contenido
    config.read_string(contenido)
    readkey = config.get("DEFAULT", key, fallback=default)
    return readkey

def executeCommand(command):
    # Ejecutar el comando y capturar la salida
    with os.popen(command) as resultado:
        salida = resultado.read()
        print(salida)

def cpcModels(model):
    
    if model == "6128":
        print("""
 Amstrad 128K Microcomputer    (v3)
 ©1985 Amstrad Consumer Electronics plc
         and Locomotive Software Ltd.

 BASIC 1.1

Ready""")
    elif model =="464":
        print ("""
 Amstrad 64K Microcomputer    (v1)
 ©1984 Amstrad Consumer Electronics plc
         and Locomotive Software Ltd.

 BASIC 1.0

Ready""") 

    elif model =="664":
        print ("""
 Amstrad 64K Microcomputer    (v2)
 ©1984 Amstrad Consumer Electronics plc
         and Locomotive Software Ltd.

 BASIC 1.1

Ready""")


# function model_cpc {
# case $1 in
#     6128)
# echo """ 
#  Amstrad 128K Microcomputer    (v3)
#  ©1985 Amstrad Consumer Electronics plc
#          and Locomotive Software Ltd.

#  BASIC 1.1

# Ready
# ${NORMAL}"""
#         ;;
#     664)
# echo """ 
#  Amstrad 64K Microcomputer    (v2)
#  ©1984 Amstrad Consumer Electronics plc
#          and Locomotive Software Ltd.

#  BASIC 1.1

# Ready
# ${NORMAL}"""
#         ;;
#     464)
# echo """ 
#  Amstrad 64K Microcomputer    (v1)
#  ©1984 Amstrad Consumer Electronics plc
#          and Locomotive Software Ltd.

#  BASIC 1.0

# Ready
# ${NORMAL}"""
#         ;;
#     m46128)
# echo """ 
#  Amstrad 128K Microcomputer    (v3)
#  ©1985 Amstrad Consumer Electronics plc
#          and Locomotive Software Ltd.

#  BASIC 1.1

#  M4 Board v2.0.6

# Ready
# ${NORMAL}"""
# ;;
#     m4664)
# echo """ 
#  Amstrad 64K Microcomputer    (v2)
#  ©1984 Amstrad Consumer Electronics plc
#          and Locomotive Software Ltd.

#  BASIC 1.1

#  M4 Board v2.0.6

# Ready
# ${NORMAL}"""
#         ;;
#     m4464)
# echo """ 
#  Amstrad 64K Microcomputer    (v1)
#  ©1984 Amstrad Consumer Electronics plc
#          and Locomotive Software Ltd.

#  BASIC 1.0

#  M4 Board v2.0.6

# Ready
# ${NORMAL}"""
#         ;;