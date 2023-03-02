from api import *
from display import *
import signal, sys, colorama
from colorama import Fore


#Ctrl+c
def def_handler(sig,frame):
    print(f"\n\n{Fore.RED}[!] Saindo...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)




api = ApiRequests()
display = Display()



#Program starts here
display.main_menu()
user_option = int(input('Escolha uma opção: '))

if user_option not in (1,2,3,0):
    print('Opção invalida!!')

elif user_option == 1:
    display.convert_menu()
    base = str(input('From: ')).upper()
    to = str(input('To: ')).upper()
    amount = int(input('Montante: '))
    api.convert(base,to,amount)

elif user_option == 2:
    display.latest_menu()
    base = str(input('Base: ')).upper()
    to = str(input('To: ')).upper()
    api.latest_rate(base,to)

elif user_option == 3:
    api.show_all_symbols()

elif user_option == 0:
    print(f"\n\n{Fore.RED}[!] Saindo...")
    sys.exit(1)
