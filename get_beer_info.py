import requests
from bs4 import BeautifulSoup
import re


def extract_initial_number(concatenated_text, ignore_digits):
    # Usar expressão regular para encontrar a parte inicial do número
    # Cria a parte da expressão regular para ignorar 1 ou 2 dígitos no final
    if ignore_digits == 1:
        pattern = r'(\d{1,2}(?:\.\d+)?)(?=\d{1}$)'  # Ignora 1 dígito
    elif ignore_digits == 2:
        pattern = r'(\d{1,2}(?:\.\d+)?)(?=\d{2}$)'  # Ignora 2 dígitos
    else:
        raise ValueError("ignore_digits deve ser 1 ou 2.")

    # Usar a expressão regular para encontrar a parte inicial do número
    match = re.match(pattern, concatenated_text)
    if match:
        return match.group(1)  # Retorna o primeiro grupo que corresponde ao número

    return None  # Retorna None se não houver correspondência


def get_beer_info(url, tag):
    # Envie uma solicitação GET para a página
    response = requests.get(url)

    # Verifique se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Analise o conteúdo HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Usar o seletor CSS para encontrar o elemento que contém o texto desejado
        container = soup.find(id="scoresheet-container")    

        # Verificar se o container foi encontrado
        if container:
            # Capturar todos os divs dentro do container
            divs = container.find_all('div')  # Você pode ajustar para outra tag se necessário
            #print(divs)

            # Contar quantos divs foram encontrados
            #div_count = len(divs)
            #print(f"Número de <div> encontrados: {div_count}")

            # Inicializar um dicionário para armazenar os dados
            beer_info = {}

            # Verificar se temos divs suficientes
            if len(divs) >= 97:  # Certifique-se de que há pelo menos 10 divs
                # Capturar informações específicas com base nas iterações
                beer_info["Judge Name"] = divs[5].get_text(strip=True).split("Judge Name")[1].strip()
                beer_info["Style"] = divs[7].get_text(strip=True).split("Style")[1].strip()
                beer_info["Brewery"] = divs[8].get_text(strip=True).split("Brewery")[1].strip()
                beer_info["Beer"] = divs[9].get_text(strip=True).split("Beer Name")[1].strip()
                beer_info["Special ingredients"] = divs[10].get_text(strip=True).split("Special ingredients")[1].strip()    
                beer_info["Bottle Inspection"] = divs[11].get_text(strip=True).split("etc.")[1].strip()
                beer_info["Aroma"] = divs[36].get_text(strip=True)
                beer_info["Aroma Score"] = extract_initial_number(divs[33].get_text(strip=True),2)
                beer_info["Appearance"] = divs[44].get_text(strip=True)
                beer_info["Appearance Score"] = extract_initial_number(divs[41].get_text(strip=True),1)
                beer_info["Flavor"] = divs[53].get_text(strip=True)
                beer_info["Flavor Score"] = extract_initial_number(divs[50].get_text(strip=True),2)
                beer_info["Mouthfeel"] = divs[61].get_text(strip=True)
                beer_info["Mouthfeel Score"] = extract_initial_number(divs[58].get_text(strip=True),1)
                beer_info["Overall Impression"] = divs[69].get_text(strip=True)
                beer_info["Overall Impression Score"] = extract_initial_number(divs[66].get_text(strip=True),2)
                beer_info["Total Score"] = extract_initial_number(divs[72].get_text(strip=True),2)
                beer_info["Stylistic Accuracy"] = divs[83].get_text(strip=True)
                beer_info["Technical Merit"] = divs[90].get_text(strip=True)
                beer_info["Intangibles"] = divs[97].get_text(strip=True)

                # Captura dos valores das barras de progresso
                progress_bars = container.find_all('div', class_='progress-bar')
                for progress in progress_bars:
                    # Obter o valor do atributo aria-valuenow
                    value = progress['aria-valuenow']
                    # Armazenar o valor correspondente à barra
                    if "Stylistic Accuracy" in progress.find_previous('p').get_text(strip=True):
                        beer_info["Stylistic Accuracy"] = value
                    elif "Technical Merit" in progress.find_previous('p').get_text(strip=True):
                        beer_info["Technical Merit"] = value
                    elif "Intangibles" in progress.find_previous('p').get_text(strip=True):
                        beer_info["Intangibles"] = value

                if tag:
                    beer_info["Tag"] = tag 
                    
                print(beer_info)

            else:
                print("Não há divs suficientes para capturar as informações necessárias.")
                return None
            
            # Exibir os resultados armazenados no dicionário
            # print("Informações da Cerveja:")
            # for key, value in beer_info.items():
            #     print(f"{key}: {value}")
            
            return beer_info
    
        else:
            print("Container não encontrado.")
            return None
    else:
        print(f"Falha ao acessar a página: {response.status_code}")
        return None
