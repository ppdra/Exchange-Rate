import os, colorama
from colorama import Fore

class Display:

    colorama.init(autoreset=True)


    def main_menu(self):
        banner = "Welcome to Exchange Rate"
        os.system('clear')
        print("=" * len(banner))
        print(banner)
        print("=" * len(banner))
        print("""\n
[ 1 ] - Converão de valores
[ 2 ] - Ultimas Cotação
[ 3 ] - Monstrar todas as moedas.
[ 0 ] - Sair\n """)


    def convert_menu(self):
        os.system('clear')
        print(f"""{Fore.MAGENTA}Usage example:\n
from: EUR
to: BRL
montante: 100
\nresposta = 100 EUR é igual a 500 BRL\n=============\n""")


    def latest_menu(self):
        os.system('clear')
        print(f"""{Fore.MAGENTA}Usage example:\n
base: EUR
to: BRL
\nresposta = 1 BRL é igual a EUR\n================\n""")
