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
[ 1 ] - Convert
[ 2 ] - Latest Rate
[ 3 ] - Show all symbols
[ 0 ] - Exit\n """)


    def convert_menu(self):
        os.system('clear')
        print(f"""{Fore.MAGENTA}Usage example:\n
from: EUR
to: BRL
amount: 100
\nresponse = 100 EUR is equal 500 BRL\n=============\n""")


    def latest_menu(self):
        os.system('clear')
        print(f"""{Fore.MAGENTA}Usage example:\n
base: EUR
to: BRL
\nresponse = 1 BRL equivale a 5 EUR\n================\n""")
