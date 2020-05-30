"""
mandassnmasmamsm
"""
import requests
from bs4 import BeautifulSoup


def get_url_nomes_livros():
    """
    Cria uma lista de dicionários com a url e o nome dos livros
    """

    URL = 'https://marcusnunes.me/posts/livros-gratuitos-da-springer/'
    resp = requests.get(URL)
    soup = BeautifulSoup(resp.content, 'html.parser')

    return [ {'url':link.get('href'), 'nome': link.text} for link in soup.find_all('ul')[1].find_all('a')]

def get_livros(lista):
    """
    Pega a lista gerada pela função get_url_nomes_listas e baixa e pdf e grava
    no diretório atual
    """

    for livro in lista:
        resp = requests.get(livro['url'])
        soup = BeautifulSoup(resp.content, 'html.parser')
        div = soup.select('.cta-button-container__item')
        try:
            link = div[0].find('a')
            print(f'baixando {livro["nome"]} ...')
            resp = requests.get('https://link.springer.com' + link.get('href'))
            with open(f'{livro["nome"]}.pdf', 'wb') as f:
                f.write(resp.content)
        except IndexError:
            print(f'Ocorreu um erro ao baixar o livros {livro["nome"]}')



if __name__ == '__main__':
    l = get_url_nomes_livros()
    #print(l)
    get_livros(l)
