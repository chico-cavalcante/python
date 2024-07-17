"""Hello World Multi Linguas.

dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

como usar :

tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

execução:
    python3 hello.py
	ou
	./hello.py
"""
__version__ ="0.0.1"	
__author__ = "Francisco Cavalcante"
__licence__ = "unlicense"

import os 

Current_language = os.getenv("LANG","en_US")[:5]
msg = "hello, world!"

if current_language == "pt_BR":
    msg = "olá, Mundo!"
	
elif current_language == "it_IT":	
	msg = "Ciao, Mondo!"
	
print (msg)
