# from prompt_toolkit import prompt
# from prompt_toolkit.formatted_text import HTML
# from prompt_toolkit.styles import Style
# import shutil

# # Datos para la barra de estado
# MODEL = "128K ORDENADOR PERSONAL"
# MODE = 1
# DISC = "dsfasdf.dsk"
# EMULATOR = "sdfsadf"

# # Obtener el ancho del terminal
# TERMINAL_WIDTH = shutil.get_terminal_size().columns

# # Función para la barra de estado
# def status_toolbar():
#     return HTML(
#         "<red> </red><green> </green><blue> </blue> <b>AMSTRAD <i>"
#         + MODEL
#         + "</i></b>            <b>MODE: </b>"
#         + str(MODE)
#         + "     <b>DISC: </b>"
#         + DISC
#         + "     <b>EMULATOR: </b>"
#         + EMULATOR
#     )

# # Estilo para el prompt
# style = Style.from_dict({
#     'top-toolbar': 'fg:#828282 bg:#ffffff',  # Fondo gris claro, texto negro para la barra de herramientas superior
# })

# # Crear el `prompt` con la barra de herramientas en la parte superior
# text = prompt(
#     '> ',
#     top_toolbar=status_toolbar,  # Colocar la barra de estado en la parte superior
#     style=style  # Usar el estilo personalizado
# )

# print('You said: %s' % text)





from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style

# Datos │para la barra de estado
MODEL = "128K ORDENADOR PERSONAL"
MODE = 1
DISC = "dsfasdf.dsk"
EMULATOR = "sdfsadf"


pepe=HTML('<style fg="ansired">██</style> '
            '<style fg="ansigreen">██</style> '
            '<style fg="ansiblue">██</style> '
            '<style fg="ansiwhite">│</style>')

# Función para la barra de estado
def status_toolbar():
    return HTML(
        "<red> </red><green> </green><blue> </blue> <b>AMSTRAD <i>"
        + MODEL
        + "</i></b>            <b>MODE: </b>"
        + str(MODE)
        + "     <b>DISC: </b>"
        + DISC
        + "     <b>EMULATOR: </b>"
        + pepe
    )

# Estilo para el prompt
style = Style.from_dict({
    # Estilo para el fondo de la barra de estado
    'bottom-toolbar': 'fg:#828282 bg:#ffffff',  # Fondo gris claro con texto negro
})

# Prompt con barra de estado personalizada
text = prompt(
    '> ',
    bottom_toolbar=status_toolbar,
    style=style  # Usar el estilo personalizado
)

print('You said: %s' % text)
