import requests
from bs4 import BeautifulSoup
from database import dblivro, livros
from tabelaLivros import inserirlivro, listarlivros, zerartabela

with livros.app_context():
    dblivro.create_all()


def gerenciarlivros():
    url = "https://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    for i, book in enumerate(books[:10]):
        title = book.h3.a['title']
        price = f'£{book.find('p', class_='price_color').text}'
        rating = book.find('p', class_='star-rating')['class'][1]
        availability = book.find('p', class_='instock availability').text.strip()

        if rating == "One":
            try:
                rating = '⭐'
            except:
                rating = '*'

        elif rating == "Two":
            try:
                rating = '⭐⭐'
            except:
                rating = '**'

        elif rating == "Three":
            try:
                rating = '⭐⭐⭐'
            except:
                rating = '***'

        elif rating == "Four":
            try:
                rating = '⭐⭐⭐⭐'
            except:
                rating = '****'

        elif rating == "Five":
            try:
                rating = '⭐⭐⭐⭐⭐'
            except:
                rating = '******'

        inserirlivro(title, price, rating, availability)


if __name__ == '__main__':
    print("""
***ALERTA***
Este menu é para os desenvolvedores da aplicação.
Para fazer a tarefa da AP2, utilize o arquivo app.py""")
    while True:
        opcao = int(input("""
    MENU DE OPÇÕES: 
    [ 1 ] Listar Livros.
    [ 2 ] Zerar Tabela.
    [ 3 ] Testar insercao
    [ 4 ] Encerrar
    → """))
        if opcao == 1:
            listarlivros()

        elif opcao == 2:
            zerartabela()

        elif opcao == 3:
            gerenciarlivros()

        elif opcao == 4:
            break

        else:
            print("opcao invalida")
