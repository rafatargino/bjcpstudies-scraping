import requests
from bs4 import BeautifulSoup


#url = "https://www.scoresheets.cc/thomazpp"
#https://www.scoresheets.cc/henriqueboaventura
#https://www.scoresheets.cc/giraia
url = "https://www.scoresheets.cc/leopinto/scoresheet/5047-hoegaarden-hoegaarden"

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
        div_count = len(divs)
        print(f"Número de <div> encontrados: {div_count}")

        # Inicializar um dicionário para armazenar os dados
        beer_info = {}
        i=0

        # Iterar pelos divs encontrados
        for index, div in enumerate(divs):
            texto = div.get_text(strip=True)
                                   
            # Salvar o texto em um arquivo
            # with open("beer_info.txt", "a", encoding="utf-8") as file:
            #     file.write(str(index) + "\n")  # Adiciona o texto ao arquivo
            #     file.write(texto + "\n")  # Adiciona o texto ao arquivo

            # Verificar a posição do índice para capturar as informações desejadas
            if index == 5:  # 5ª iteração para Judge Name
                captura = texto.split("Judge Name")[1].strip()
                beer_info["judge name"] = captura
            elif index == 7:  # 7ª iteração para Style
                captura = texto.split("Style")[1].strip()
                beer_info["style"] = captura
            elif index == 8:  # 8ª iteração para Brewery
                captura = texto.split("Brewery Name")[1].strip()
                beer_info["brewery"] = captura
            elif index == 9:  
                captura = texto.split("Beer Name")[1].strip()
                beer_info["beer"] = captura
            elif index == 10:  
                captura = texto.split("Special ingredients")[1].strip()
                beer_info["ingredients"] = captura
            elif index == 11:  
                captura = texto.split("Bottle InspectionAppropriate size, cap, fill level, label removal, etc.")[1].strip()
                beer_info["bottle"] = captura
            elif index == 36:  
                beer_info["aroma"] = texto                                                
            elif index == 44:  
                beer_info["appearance"] = texto                                                
            elif index == 53:  
                beer_info["flavor"] = texto                                                
            elif index == 61:  
                beer_info["mouthfeel"] = texto                                                
            elif index == 69:  
                beer_info["impression"] = texto
            elif index == 83:  
                beer_info["stylistic accuracy"] = texto                                                
            elif index == 90:  
                beer_info["technical Merit"] = texto                                                
            elif index == 97:  
                beer_info["intangibles"] = texto                                                                                                                                

        # Exibir os resultados armazenados no dicionário
        print("Informações da Cerveja:")
        for key, value in beer_info.items():
            print(f"{key}: {value}")

    else:
        print("Texto não encontrado.")
else:
    print(f"Falha ao acessar a página: {response.status_code}")
