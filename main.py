from scraping import get_beer_info


if __name__ == "__main__":
    
    # Conjunto de URLs a serem passadas como parâmetros
    urls = [
        "https://www.scoresheets.cc/leopinto/scoresheet/5058-hunsruck-sahti",
        "https://www.scoresheets.cc/leopinto/scoresheet/5047-hoegaarden-hoegaarden"
    ]

    # Iterar sobre as URLs e chamar a função de scraping
    for url in urls:
        print(f"\nCapturando informações da URL: {url}")
        beer_info = get_beer_info(url)

        # Exibir os resultados
        if beer_info:
            print("Informações da Cerveja:")
            for key, value in beer_info.items():
                print(f"{key}: {value}")
        else:
            print("Nenhuma informação encontrada.")

# url = "https://www.scoresheets.cc/thomazpp"
# #https://www.scoresheets.cc/henriqueboaventura
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