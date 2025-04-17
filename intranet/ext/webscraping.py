from bs4 import BeautifulSoup
import requests

def bs(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # Ajuste a codificação conforme necessário

    if response.status_code == 403:
        print("Acesso proibido: Erro 403.")

    return BeautifulSoup(response.content, 'html.parser')
