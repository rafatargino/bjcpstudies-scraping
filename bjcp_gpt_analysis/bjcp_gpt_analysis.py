import openai
import os
from dotenv import load_dotenv, find_dotenv
import sys
import json

# Adicionar o diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

# Importar a função do módulo utils
from utils import save_data_to_text, save_data_to_json

#exemplo de prompts
#https://platform.openai.com/docs/examples/default-review-classifier
#https://platform.openai.com/docs/examples/default-keywords

# Referências
#https://hub.asimov.academy/blog/openai-api/

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv(find_dotenv())

# Obter a chave da API da variável de ambiente
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("A chave da API da OpenAI não está definida. Verifique se o arquivo .env contém 'OPENAI_API_KEY'.")

# Configurar a chave da API
openai.api_key = api_key

client = openai.Client()


lista_estilos = "1A. American Light Lager, 1B. American Lager, 1C. Cream Ale, 1D. American Wheat Beer, 2A. International Pale Lager, 2B. International Amber Lager, 2C. International Dark Lager, 21A. American IPA, 21B. Specialty IPA - Belgian IPA, 21B. Specialty IPA - Black IPA, 21B. Specialty IPA - Brown IPA, 21B. Specialty IPA - Red IPA, 21B. Specialty IPA - Rye IPA, 21B. Specialty IPA - White IPA"
lista_estilos = "1B. American Lager"

#lista_estilos = "1A. American Light Lager, 1B. American Lager, 1C. Cream Ale, 1D. American Wheat Beer, 2A. International Pale Lager, 2B. International Amber Lager, 2C. International Dark Lager" 
#lista_estilos = "3A. Czech Pale Lager, 3B. Czech Premium Pale Lager, 3C. Czech Amber Lager, 3D. Czech Dark Lager"
#lista_estilos = "5A. German Leichtbier, 5B. Kölsch, 5C. German Helles Exportbier, 5D. German Pils"
#lista_estilos = "6A. Märzen, 6B. Rauchbier, 6C. Dunkles Bock"
#lista_estilos = "7A. Vienna Lager, 7B. Altbier"
# 8A. Munich Dunkel, 8B. Schwarzbier  
# 9A. Doppelbock, 9B. Eisbock  
# 10A. Weissbier, 10B. Dunkles Weissbier, 10C. Weizenbock  
# 11A. Ordinary Bitter, 11B. Best Bitter, 11C. Strong Bitter  
# 12A. British Golden Ale, 12B. Australian Sparkling Ale, 12C. English IPA  
# 13A. Dark Mild, 13B. British Brown Ale, 13C. English Porter  
# 14A. Scottish Light, 14B. Scottish Heavy, 14C. Scottish Export  
# 15A. Irish Red Ale, 15B. Irish Stout, 15C. Irish Extra Stout  
# 16A. Sweet Stout, 16B. Oatmeal Stout, 16C. Tropical Stout, 16D. Foreign Extra Stout  
# 17A. British Strong Ale, 17B. Old Ale, 17C. Wee Heavy, 17D. English Barleywine  
# 18A. Blonde Ale, 18B. American Pale Ale  
# 19A. American Amber Ale, 19B. California Common, 19C. American Brown Ale  
# 20A. American Porter, 20B. American Stout, 20C. Imperial Stout  
# 21A. American IPA, 21B. Specialty IPA - Belgian IPA, 21B. Specialty IPA - Black IPA, 21B. Specialty IPA - Brown IPA, 21B. Specialty IPA - Red IPA, 21B. Specialty IPA - Rye IPA, 21B. Specialty IPA - White IPA  
# 22A. Double IPA, 22B. American Strong Ale, 22C. American Barleywine, 22D. Wheatwine  
# 23A. Berliner Weisse, 23B. Flanders Red Ale, 23C. Oud Bruin, 23D. Lambic, 23E. Gueuze, 23F. Fruit Lambic  
# 24A. Witbier, 24B. Belgian Pale Ale, 24C. Bière de Garde  
# 25A. Belgian Blond Ale, 25B. Saison, 25C. Belgian Golden Strong Ale  
# 26A. Trappist Single, 26B. Belgian Dubbel, 26C. Belgian Tripel, 26D. Belgian Dark Strong Ale  
# 27A. Historical Beer - Gose, 27A. Historical Beer - Kentucky Common, 27A. Historical Beer - Lichtenhainer, 27A. Historical Beer - London Brown Ale, 27A. Historical Beer - Piwo Grodziskie, 27A. Historical Beer - Pre-Prohibition Lager, 27A. Historical Beer - Pre-Prohibition Porter, 27A. Historical Beer - Roggenbier, 27A. Historical Beer - Sahti  
# 28A. Brett Beer, 28B. Mixed-Fermentation Sour Beer, 28C. Wild Specialty Beer  
# 29A. Fruit Beer, 29B. Fruit and Spice Beer, 29C. Specialty Fruit Beer  
# 30A. Spice, Herb, or Vegetable Beer, 30B. Autumn Seasonal Beer, 30C. Winter Seasonal Beer  
# 31A. Alternative Grain Beer, 31B. Alternative Sugar Beer  
# 32A. Classic Style Smoked Beer, 32B. Specialty Smoked Beer  
# 33A. Wood-Aged Beer, 33B. Specialty Wood-Aged Beer  
# 34A. Experimental Beer  


gpt_message = [
        {
            "role": "system", 
            "content": """Atue como um renomeado juiz de cerveja BJCP de nível grão mestre. Considerando o 
            estilo de cerveja que irei informar abaixo do guia de estilos BJCP 2021, crie uma lista para dos 
            principais descritores, no formato de palavras-chave/tags, para cada seção do guia de estilos a 
            seguir e nessa ordem: aroma, aparência, sabor, sensação de boca, impressão geral e comparação de 
            estilos. Além disso, siga fielmente as orientações abaixo:
            - Só utilize unicamente como fonte de informação o que está no guia de estilo 2021;
            - As palavras chaves ou tag serão construídas da seguinte forma. Os substantivos que representam as 
            características, como porexemplo torrado, malte, fermentação, serão colocados um em cada tag. Quando 
            houver descrição da intensidade da característa, como por exemplo alta, média-alta, baixa, será 
            informada na mesma tag da característica, com um "-" separando as duas, sem espaços, como por exemplo: 
            torrado-médio forte.
            - Para cada seção acima, haverá subseções para extrair as palavras-chave/tags confome a seguir e nessa 
            ordem: aroma (malte, lúpulo, ésteres e outros aromáticos), aparência (cor, limpidez, espuma), sabor 
            (lúpulo, malte, ésteres, equilíbrio e retrogosto), sensação de boca (corpo, carbonatação, calor, 
            cremosidade, adstringência), impressão geral (malte, lupulo e ésteres) e comparação de estilos (aqui as 
            tags podem ser frases curtas de 5 a 8 palavras para cada comparação com outros estilos, citrando os nomes
            dos outros estilos), 
            conforme exemplo abaixo:
            - Aroma: lupulo: lúpulo-proeminente, citrico, floral, pinho, resinoso;
	                 malte: torrado-baixo-médio, cereais;
	                 ésteres: ésteres-baixo, frutado.
            - É só para usar palavras chaves... não pode colcoar "com leve ester frutavel aceitavel". esses textos 
            serão apresentados em um estilo de "tag" de classificação em textos
            - Não usar "álcool-baixo (opcional)", preferir "álcool-baixo-opcional".
            - Não precisa dizer a origem da característica abordada, então ao dizer "leve-adstringência (lúpulo)", 
            dizer apenas "leve-adstringência"
            - retorne as informações em um arquivo json. Use o nome do estilo conforme informado abaixo."""
        },
        {
            "role": "user", 
            "content": f"O estilo a ser resumido são: {lista_estilos}"
        }
    ]

print("chamando o chatGPT...")
chat_completion = client.chat.completions.create(    
    model="gpt-4o-mini",
    messages=gpt_message,
    temperature=0.2,
)

mensagem_resp = chat_completion.choices[0].message.content

# Remover aspas triplas e a palavra "json" da primeira e última linha
mensagem_resp = mensagem_resp.strip().strip('```json').strip('```')

# Converter a string JSON em um objeto Python
try:
    response_json = json.loads(mensagem_resp)
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON: {e}")
    response_json = None

if response_json:
    # Salvar os resultados em um arquivo JSON
    print("Salvar texto...")
    save_data_to_text(mensagem_resp, 'bjcp_keywords.txt')
    print("Salvar json...")
    save_data_to_json(response_json, 'bjcp_keywords.json')
    print("\nA análise do bjcp foi salva em 'bjcp_keywords.json'")
else:
    print("\nNenhuma análise gerada...")

#for message in chat_completion:
    #print(message['message']['content'])
