import json
import time
import random
from get_beer_urls import get_beer_urls
from get_beer_info import get_beer_info

def load_existing_data(filename):
    """Carrega dados existentes de um arquivo JSON."""
    if os.path.exists(filename):
        with open(filename, mode='r', encoding='utf-8') as json_file:
            return json.load(json_file)
    return []  # Retorna uma lista vazia se o arquivo não existir

def save_data_to_json(data, filename):
    """Salva dados em um arquivo JSON, adicionando novos itens ao existente."""
    existing_data = load_existing_data(filename)  # Carrega dados existentes
    existing_data.extend(data)  # Adiciona novos dados à lista existente

    with open(filename, mode='w', encoding='utf-8') as json_file:
        json.dump(existing_data, json_file, ensure_ascii=False, indent=4)

# ------------------------------------------------------

if __name__ == "__main__":

    # URL base da tabela de avaliações
    #base_url = "https://www.scoresheets.cc/thomazpp"
    base_url = "https://www.scoresheets.cc/henriqueboaventura"

    # Obter todas as URLs de avaliações
    beer_urls = get_beer_urls(base_url)
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
        beer_info = get_beer_info(url)
        
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
    
    # Salvar os resultados em um arquivo JSON
    save_data_to_json(all_beer_info, 'beer_info.json')

    print("\nAs informações das cervejas foram salvas em 'beer_info.json'.")



# url = "https://www.scoresheets.cc/thomazpp"
# #
# #https://www.scoresheets.cc/giraia
# #url = "https://www.scoresheets.cc/thomazpp"
# #https://www.scoresheets.cc/henriqueboaventura
# #https://www.scoresheets.cc/giraia
# url = 
# # Envie uma solicitação GET para a página
# response = requests.get(url)
# # Verifique se a solicitação foi bem-sucedida
# if response.status_code == 200:
# else:
#     print(f"Falha ao acessar a página: {response.status_code}")