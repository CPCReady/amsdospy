import os
import sys
from dotenv import load_dotenv
from prompt_toolkit import PromptSession, print_formatted_text, HTML
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.cursor_shapes import CursorShape
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.history import FileHistory
from console import common as funtions

COMMAND_LIST  = ["MODE", "DISC", "CPC", "CAT","SAVE", "CLS", "BORDER", "EXIT"]
COMMAND_LIST2 = ["|ERA"]
MODELS_CPC    = ['464', '6128', '664']
MODE_CPC      = ['0','1','2']

# from sdkcpc.load import loadCommand


# from sdkcpc.concat import concatCommand
# from sdkcpc.make import makeCommand

# from sdkcpc.machine import modelCommandbye

# from sdkcpc.run import runCommand

# from sdkcpc.save import saveCommand

# from sdkcpc.cat import catCommand
# from sdkcpc.common import *
# from sdkcpc.about import headerAmstrad, aboutCommand
# from sdkcpc.cls import clsCommand




session = PromptSession(history=FileHistory('~/.history_sdkcpc'))
sql_completer = WordCompleter(["COMMAND_LIST"], ignore_case=True)

style = Style.from_dict(
    {
        # Default style.
        "": "#ffff00"
    }
)


def main():
    # Erase Screen
    os.system('clear')
    # print(os.getcwd())
    load_dotenv(dotenv_path=os.getcwd() + '/tests/prueba2/cfg/CPCReady.cfg')
    
    funtions.cpcModels(os.getenv("MODEL"))

    sessions = PromptSession(style=style, completer=sql_completer, cursor=CursorShape.BLOCK)

    # Show header is activated in config
    # headerAmstrad()

    while True:
        try:
            command = sessions.prompt('', style=style, auto_suggest=AutoSuggestFromHistory())
        except KeyboardInterrupt:
            print_formatted_text(HTML('<yellow>GoodBye!!</yellow>'), style=style)
            sys.exit(1)
        except EOFError:
            break
        else:
            if command:
                command.split()
                if command.split()[0].upper() in COMMAND_LIST:
                    if command.split()[0].upper() == "ABOUT":
                        print ("about")
                    elif command.split()[0].upper() == "CAT":
                        print ("about")
                    if command.split()[0].upper() == "CLS":
                        print ("about")
                    elif command.split()[0].upper() == "CONCAT":
                        if countCommand(command.split(), 2):
                            # file = command.split()[1]
                            print ("about")
                    elif command.split()[0].upper() == "MAKE":
                        # if len(command.split()) == 2:
                        #     file = command.split()[1]
                        #     file_split = os.path.splitext(file)
                        #     if file_split[1].upper() != ".DSK":
                        #         file = file + ".dsk"
                        #     updateConfigKey("files", "dsk", file.replace(" ", "_"))
                        # makeCommand()
                        print ("about")
                    elif command.split()[0].upper() == "LOAD":
                        # if len(command.split()) == 2:
                        #     file = command.split()[1].replace('"', '')
                        # else:
                        #     file = ""
                        # loadCommand(file, False)
                        print ("about")
                    elif command.split()[0].upper() == "MACHINE":
                        print ("about")
                    elif command.split()[0].upper() == "RUN":
                        print ("about")
                    elif command.split()[0].upper() == "SAVE":
                        print ("about")
                    elif command.split()[0].upper() == "CDT":
                        print_formatted_text(HTML('<white>Coming soon</white>'), style=style)
                    print_formatted_text(HTML('<yellow>Ready</yellow>'), style=style)
                else:
                    print_formatted_text(HTML('<yellow>Syntax error\nReady</yellow>'), style=style)


if __name__ == '__main__':
    main()

def countCommand(command, number):
    if len(command) == number:
        return True
    else:
        print_formatted_text(HTML('<yellow>Operand missing</yellow>'), style=style)
