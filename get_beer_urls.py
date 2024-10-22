import requests
from bs4 import BeautifulSoup
import re 


def get_beer_urls(base_url):
    urls = []
    page = 1

    while True:
        # Criar a URL da página atual
        url = f"{base_url}?page={page}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Falha ao acessar a página: {response.status_code}")
            break

        # Analisar o conteúdo da página
        soup = BeautifulSoup(response.text, 'html.parser')

 
        # with open('output.html', 'w', encoding='utf-8') as f:
        #     f.write(soup.prettify())

        # Encontrar a tabela de avaliações
        table = soup.find('table')  # Ajuste conforme necessário

        # Verificar se a tabela foi encontrada
        if not table:
            print("Tabela de avaliações não encontrada.")
            break

        # Encontrar todas as linhas da tabela
        rows = table.find_all('tr')

        # Capturar URLs de cada linha (ignorando o cabeçalho)
        for row in rows[1:]:
            link = row.find('a')
            if link and 'href' in link.attrs:
                full_url = link['href']
                # Adiciona a URL ao array
                urls.append(full_url)

        # Verificar se há um link para a próxima página
        next_page = soup.find('a', string=re.compile("Next", re.IGNORECASE))
        if not next_page:
            break

        page += 1  # Mover para a próxima página

    return urls