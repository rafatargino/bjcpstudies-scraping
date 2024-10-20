import requests
from bs4 import BeautifulSoup


#url = "https://www.scoresheets.cc/thomazpp"
#https://www.scoresheets.cc/henriqueboaventura
#https://www.scoresheets.cc/giraia
url = "https://www.scoresheets.cc/leopinto/scoresheet/5058-hunsruck-sahti"

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
        print(divs.)
        #print(divs)

        # Inicializar variáveis para armazenar os textos
        judge_name = ""
        style = ""
        brewery = ""

        # Iterar pelos divs encontrados
        for div in divs:
            texto = div.get_text(strip=True)
            # Verificar o texto e capturar as informações desejadas
            if "Nome do Juiz" in texto:
                judge_name = texto.split("Judge Name")[1].strip()
            elif "Estilo" in texto:  
                style = texto.split("Style")[1].strip()
            elif "Brewery" in texto:
                brewery = texto.split("Brewery")[1].strip()

        # Exibir os resultados
        print("Judge Name:", judge_name)
        print("Style:", style)
        print("Brewery:", brewery)

    else:
        print("Texto não encontrado.")
else:
    print(f"Falha ao acessar a página: {response.status_code}")
