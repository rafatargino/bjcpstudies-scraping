import time
import random
from get_beer_urls import get_beer_urls
from get_beer_info import get_beer_info
from utils.utils import save_data_to_json, SearchType

# ------------------------------------------------------
if __name__ == "__main__":

    # URL base da tabela de avaliações
    #base_url = "https://www.scoresheets.cc/thomazpp"
    #base_url = "https://www.scoresheets.cc/gabriela.a.lando"
    #base_url = "https://www.scoresheets.cc/henriqueboaventura"
    #base_url = "https://www.scoresheets.cc/giraia"
    #type = SearchType.USER
    #tag = ""
    
    base_url = "GE+BJCP"
    tag = "GEBJCPACERVA"
    type = SearchType.KEYWORD
    beer_urls = get_beer_urls(base_url, type)
        
    print(beer_urls)
    #teste para uma cerveja apenas:
    #beer_urls = ["https://www.scoresheets.cc/thomazpp/scoresheet/5616-hoegaarden-hoegaarden"]

    # Dicionário para acumular todas as informações das cervejas
    all_beer_info = []

    # Total de cervejas a serem capturadas
    total_beers = len(beer_urls)

    # Iterar sobre as URLs e chamar a função de scraping
    for index, url in enumerate(beer_urls, start=1):  # Usar enumerate para obter o índice
        print(f"\nCapturando Cerveja {index}/{total_beers}: {url}")
        beer_info = get_beer_info(url, tag)
        
        if beer_info:
            all_beer_info.append(beer_info)
            # Exibir os resultados
            # print("Informações da Cerveja:")
            # for key, value in beer_info.items():
            #     print(f"{key}: {value}")
        else:
            print("Nenhuma informação encontrada.")
        
        pause_time = random.randint(7, 15)  # Gera um número aleatório entre 7 e 15
        print(f"Pausando por {pause_time} segundos...")
        time.sleep(pause_time)  # Ajuste o tempo conforme necessário
    
    if total_beers > 0:
        # Salvar os resultados em um arquivo JSON
        save_data_to_json(all_beer_info, 'beer_info.json')
        print("\nAs informações das cervejas foram salvas em 'beer_info.json'.")
    else:
        print("\nNenhum cerveja encontrada...")

    
