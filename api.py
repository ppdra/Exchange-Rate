import requests, json, os, colorama
from colorama import Fore
from apiKey import *

class ApiRequests:

    """Para fazer as requisicoes na API"""

    def convert(self,base,to,amount):
        """
            Recebe 3 parametros
            base (moeda base para a conversao) : str
            to (moeda para ser convertida): str
            amount : int

            return:
                printa a conversao do valor

        """
        
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={base}&amount={amount}"

        payload={}
        headers={
            "apikey": apiKey
        }
       
        response = requests.get(url, headers=headers, data = payload)

        if response.status_code != 200:
            print("\nProvavel falha nos parametros da requisiçao ou na chave api")
        else:
            result = response.json()
            valor = result['result']
            print(f"\n\n{Fore.GREEN}{amount} {base} é igual a {valor} {to}")


    def latest_rate(self,base,symbol):
        """
        Recebe 2 valores
            base (moeda base para a cotacao) : str
            symbol : str
            
            Return:
                printa o valor da ultima cotaçao

        """
        
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={symbol}&base={base}"

        payload = {}
        headers= {
            "apikey": apiKey
        }

        response = requests.get(url, headers=headers, data = payload)

        if response.status_code != 200:
            print("\nProvavel falha nos parametros da requisicao pu na chave api")
        else:
            result = response.json()
            valor = result["rates"]
            date = result["date"]
            print(f"\n{Fore.GREEN}1 {base} é igual a {valor[symbol]} {symbol}\nCotação do dia {date}")


    def show_all_symbols(self):
        """
        Esta parte na realidade nao é feita requisacao na api,para nao usar as poucas 250 requisicoes por mes que tem direito. Sera feito uma busca no arquivo json que ai sim foi requisitado na api.
        Return:
            Ira retornar os symbols e o nome correspondente deste symbol para ser usado tanto no convert quanto no latest rate"""

        os.system('clear')
        print(f"\n{Fore.CYAN}List of all symbols can be used: \n\n")
        with open("data/symbols.json") as file:
            data = json.load(file)
            for k,v in data['symbols'].items():
                print(f"{Fore.CYAN}{k} > {v}")
