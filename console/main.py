
import os
import sys
from pathlib import Path
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
from prompt_toolkit.shortcuts import message_dialog

# Configuración global
COMMAND_LIST = ["ABOUT", "CLS", "CPC", "DISC", "MODE", "NEW", "RUN", "SAVE", "EXIT","GIT"]
CONFIG_CPCREADY = os.path.join(os.getcwd(), "cfg", "CPCReady.cfg")
CONFIG_HISTORY = os.path.join(os.getcwd(), "cfg", ".history")

# Estilo para formatear texto
style = Style.from_dict({
    # "": "#ffff00", # Default style.
    "red": "fg:red bold",
    # 'rprompt': 'bg:#ff0066 #ffffff',
})

# def get_rprompt():
#     return '<rprompt>'

def bye():
    print_formatted_text(
        HTML("<white>\nCPCReady v1.0.0</white>"),
        style=style,
    )
    print_formatted_text(
        HTML("<white>Goodbye!\n</white>"),
        style=style,
    )

# Prompt session con autocompletado y toolbar dinámico
session = PromptSession(
    # completer=WordCompleter(COMMAND_LIST, ignore_case=True),
    cursor=CursorShape.BLOCK,
    auto_suggest=AutoSuggestFromHistory(),
    history=FileHistory(CONFIG_HISTORY),
    # rprompt=get_rprompt,
    style=style,
)

# Función para el toolbar dinámico
def status_toolbar():
    return HTML(
        "<red> </red><green> </green><blue> </blue> <b>AMSTRAD CPC "
        + functions.readKey(CONFIG_CPCREADY, "MODEL")
        + "</b>    <b>MODE: </b>"
        + functions.readKey(CONFIG_CPCREADY, "MODE")
        + "    <b>DISC: </b>"
        + functions.readKey(CONFIG_CPCREADY, "DISC").replace('"', "")
        + "    <b>EMULATOR: </b>"
        + functions.readKey(CONFIG_CPCREADY, "EMULATOR").replace('"', "")
    )




def main():
    # Limpiar la pantalla
    os.system("clear")

    # Verificar si el archivo de configuración existe
    if not Path(CONFIG_CPCREADY).is_file():
        print_formatted_text(
            HTML("<red>There is no CPCReady project. Cannot use Amstrad console.</red>"),
            style=style,
        )
        sys.exit(1)

    # Configurar según el modelo
    functions.cpcModels(functions.readKey(CONFIG_CPCREADY, "MODEL"),functions.readKey(CONFIG_CPCREADY, "EMULATOR").replace('"', ""))

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
            os.system("clear")
            bye()
            sys.exit(1)
        except EOFError:
            break
        else:
            if command:
                # Analizar y ejecutar el comando
                parts = command.split()
                main_command = parts[0].upper()

                if main_command in COMMAND_LIST:
                    if main_command == "EXIT":
                        os.system("clear")
                        bye()
                        sys.exit(0)
                    elif main_command == "ABOUT":
                        functions.about()
                        print_formatted_text(HTML('\nReady'), style=style)
                    else:
                        functions.executeCommand(command)
                        print_formatted_text(
                            HTML("Ready"),
                            style=style,
                        )
                else:
                    print_formatted_text(HTML('Syntax error\nReady'), style=style)

if __name__ == "__main__":
    main()
