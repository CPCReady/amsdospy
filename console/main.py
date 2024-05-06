# import os
# import sys

# from pathlib import Path
# from dotenv import load_dotenv
# from prompt_toolkit import PromptSession, print_formatted_text, HTML
# from prompt_toolkit.completion import WordCompleter
# from prompt_toolkit.cursor_shapes import CursorShape
# from prompt_toolkit.lexers import PygmentsLexer
# from prompt_toolkit.styles import Style
# from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
# from prompt_toolkit.history import FileHistory
# from console import common as funtions
# from prompt_toolkit.history import InMemoryHistory

# from prompt_toolkit import prompt
# from prompt_toolkit.formatted_text import HTML


# def status_toolbar():
#     load_dotenv(dotenv_path=CONFIG_CPCREADY)

#     return HTML(" <red> </red><green> </green><blue> </blue> <b>AMSTRAD CPC " + funtions.readKey(CONFIG_CPCREADY,"MODEL") + "</b>    MODE: " + funtions.readKey(CONFIG_CPCREADY,"MODE") + "    DISC: " + funtions.readKey(CONFIG_CPCREADY,"DISC").replace('"',"") + "    EMULATOR: " + funtions.readKey(CONFIG_CPCREADY,"EMULATOR").replace('"',"") + " ")

# COMMAND_LIST  = ["LS","MODE", "DISC", "CPC", "CAT","SAVE", "CLS", "BORDER", "EXIT"]

# CONFIG_CPCREADY = os.getcwd() + "/cfg/CPCReady.cfg"


# session = PromptSession(history=FileHistory('~/.history_sdkcpc'))
# sql_completer = WordCompleter(COMMAND_LIST, ignore_case=True)

# style = Style.from_dict(
#     {
#         # "": "#ffff00",
#         "red": 'fg:red bold',
#     }
# )


# def main():
#     # Erase Screen
#     os.system('clear')
#     PATH_CPCREADY = Path(CONFIG_CPCREADY)

#     # Comprobar si el archivo existe
#     PATH_CPCREADY_EXIST = PATH_CPCREADY.is_file()

#     if not PATH_CPCREADY_EXIST:
#         print_formatted_text(HTML('<red>There is no CPCReady project. It is not possible to use Amstrad Console. </red>'), style=style)
#         exit()

#     load_dotenv(dotenv_path=CONFIG_CPCREADY)

#     funtions.cpcModels(os.getenv("MODEL"))

#     sessions = PromptSession(style=style, completer=sql_completer, cursor=CursorShape.BLOCK,auto_suggest=AutoSuggestFromHistory(),bottom_toolbar=status_toolbar)
#     #
#     # Show header is activated in config
#     # headerAmstrad()

#     while True:
#         try:
#             command = sessions.prompt('', style=style, auto_suggest=AutoSuggestFromHistory(),bottom_toolbar=status_toolbar)
#         except KeyboardInterrupt:
#             print_formatted_text(HTML('<yellow>GoodBye!!</yellow>'), style=style)
#             sys.exit(1)
#         except EOFError:
#             break
#         else:
#             if command:
#                 command.split()
#                 if command.split()[0].upper() in COMMAND_LIST:
#                     funtions.executeCommand(command)
#                     print_formatted_text(HTML('Ready'), style=style)
#                 else:
#                     # print_formatted_text(HTML('<yellow>Syntax error\nReady</yellow>'), style=style)
#                     print_formatted_text(HTML('Syntax error\nReady'), style=style)


# if __name__ == '__main__':
#     main()



import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from prompt_toolkit import (
    PromptSession,
    print_formatted_text,
    HTML,
    prompt,
)
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.cursor_shapes import CursorShape
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.styles import Style
from prompt_toolkit.history import FileHistory
from console import common as functions  # Renombrado para consistencia

# Configuración global
COMMAND_LIST = ["LS", "MODE", "DISC", "CPC", "CAT", "SAVE", "CLS", "BORDER", "EXIT"]
CONFIG_CPCREADY = os.path.join(os.getcwd(), "cfg", "CPCReady.cfg")
CONFIG_HISTORY = os.path.join(os.getcwd(), "cfg", ".history")

# Estilo para formatear texto
style = Style.from_dict({
    "red": "fg:red bold",
})

# Prompt session con autocompletado y toolbar dinámico
session = PromptSession(
    completer=WordCompleter(COMMAND_LIST, ignore_case=True),
    cursor=CursorShape.BLOCK,
    auto_suggest=AutoSuggestFromHistory(),
    history=FileHistory(CONFIG_HISTORY),
    style=style,
)

# Función para el toolbar dinámico
def status_toolbar():
    load_dotenv(dotenv_path=CONFIG_CPCREADY)
    return HTML(
        "<red> </red><green> </green><blue> </blue> <b>AMSTRAD CPC "
        + functions.readKey(CONFIG_CPCREADY, "MODEL")
        + "</b>    MODE: "
        + functions.readKey(CONFIG_CPCREADY, "MODE")
        + "    DISC: "
        + functions.readKey(CONFIG_CPCREADY, "DISC").replace('"', "")
        + "    EMULATOR: "
        + functions.readKey(CONFIG_CPCREADY, "EMULATOR").replace('"', "")
    )

def main():
    # Limpiar la pantalla
    os.system("clear")

    # Verificar si el archivo de configuración existe
    if not Path(CONFIG_CPCREADY).is_file():
        print_formatted_text(
            HTML("<red>No hay proyecto CPCReady. No se puede usar la consola Amstrad.</red>"),
            style=style,
        )
        sys.exit(1)

    # Cargar variables de entorno
    load_dotenv(dotenv_path=CONFIG_CPCREADY)

    # Configurar según el modelo
    functions.cpcModels(os.getenv("MODEL"))

    # Ciclo para el prompt
    while True:
        try:
            # Obtener el comando del usuario con un toolbar actualizado
            command = session.prompt(
                "",
                auto_suggest=AutoSuggestFromHistory(),
                bottom_toolbar=status_toolbar,
            )
        except KeyboardInterrupt:
            print_formatted_text(
                HTML("<yellow>¡Adiós!</yellow>"),
                style=style,
            )
            sys.exit(1)
        except EOFError:
            break
        else:
            if command:
                # Analizar y ejecutar el comando
                parts = command.split()
                main_command = parts[0].upper()

                if main_command in COMMAND_LIST:
                    functions.executeCommand(command)
                    print_formatted_text(
                        HTML("Ready"),
                        style=style,
                    )

                else:
                    print_formatted_text(HTML('Syntax error\nReady'), style=style)

if __name__ == "__main__":
    main()
