import os
import json
from enum import Enum

# Enumerador para os tipos de pesquisa (usuário ou palavra-chave)
class SearchType(Enum):
    USER = "user"
    KEYWORD = "search"

def load_existing_json(filename):
    #"""Carrega dados existentes de um arquivo JSON."""
    if os.path.exists(filename):
        with open(filename, mode='r', encoding='utf-8') as json_file:
            return json.load(json_file)
    return []  # Retorna uma lista vazia se o arquivo não existir

def save_data_to_json(data, filename):
    #"""Salva dados em um arquivo JSON, adicionando novos itens ao existente."""
    existing_data = load_existing_json(filename)  # Carrega dados existentes
    if isinstance(existing_data, list):
        if isinstance(data, list):
            existing_data.extend(data)  # Adiciona novos dados à lista existente
        else:
            existing_data.append(data)  # Adiciona o novo dado à lista existente
    else:
        if isinstance(data, list):
            existing_data = [existing_data] + data  # Cria uma nova lista com os dados existentes e novos
        else:
            existing_data = [existing_data, data]  # Cria uma nova lista com os dados existentes e novos

    with open(filename, mode='w', encoding='utf-8') as json_file:
        json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
    # """Salva dados em um arquivo JSON, adicionando novos itens ao existente."""
    # existing_data = load_existing_data(filename)  # Carrega dados existentes
    # existing_data.extend(data)  # Adiciona novos dados à lista existente

    # with open(filename, mode='w', encoding='utf-8') as json_file:
    #     json.dump(existing_data, json_file, ensure_ascii=False, indent=4)

def load_existing_text(filename):
    """Carrega dados existentes de um arquivo de texto."""
    if os.path.exists(filename):
        with open(filename, mode='r', encoding='utf-8') as text_file:
            return text_file.readlines()
    return []  # Retorna uma lista vazia se o arquivo não existir

def save_data_to_text(data, filename):
    """Salva dados em um arquivo de texto, adicionando novos itens ao existente."""
    existing_data = load_existing_text(filename)  # Carrega dados existentes
    existing_data.extend(data)  # Adiciona novos dados à lista existente

    with open(filename, mode='w', encoding='utf-8') as text_file:
        text_file.writelines(existing_data)
