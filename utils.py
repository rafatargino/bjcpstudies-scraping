from enum import Enum
import json
import os

# enumerador para os tipos de pesquisa (usuário ou palavra-chave)
class SearchType(Enum):
    USER = "user"
    KEYWORD = "search"

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
