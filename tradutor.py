import json
from googletrans import Translator
from tqdm import tqdm
import os

# Função para traduzir qualquer arquivo JSON para a linguagem escolhida
def traduzir_json(arquivo_entrada, arquivo_saida, idioma_destino):
    # Inicializar o tradutor
    translator = Translator()
    
    # Abrir o arquivo original
    with open(arquivo_entrada, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Função recursiva para traduzir os valores no JSON com barra de progresso
    def traduzir_valores(dado):
        if isinstance(dado, dict):
            for chave, valor in dado.items():
                dado[chave] = traduzir_valores(valor)  # Traduz cada valor dentro do dicionário
        elif isinstance(dado, list):
            for i in tqdm(range(len(dado)), desc="Traduzindo lista", leave=False):
                dado[i] = traduzir_valores(dado[i])  # Traduz cada item dentro da lista
        elif isinstance(dado, str) and dado.strip():  # Verifica se a string não está vazia
            traducao = translator.translate(dado, src='en', dest=idioma_destino)
            return traducao.text
        return dado

    # Traduzir o JSON
    print("Iniciando tradução...")
    data_traduzida = traduzir_valores(data)

    # Salvar o JSON traduzido
    with open(arquivo_saida, 'w', encoding='utf-8') as file:
        json.dump(data_traduzida, file, ensure_ascii=False, indent=4)

    print(f"Arquivo traduzido salvo em: {arquivo_saida}")

# Função para escolher o idioma de destino
def escolher_idioma():
    idiomas = {
        '1': 'pt_br',   # Português (Brasil)
        '2': 'es',      # Espanhol
        '3': 'fr',      # Francês
        '4': 'de',      # Alemão
        '5': 'it',      # Italiano
        '6': 'ru',      # Russo
        '7': 'ja',      # Japonês
        '8': 'zh-cn'    # Chinês
    }

    print("Escolha o idioma de destino para tradução:")
    for chave, idioma in idiomas.items():
        print(f"{chave}: {idioma.capitalize()}")

    escolha = input("Digite o número do idioma desejado: ").strip()

    return idiomas.get(escolha, 'pt_br')  # Default é pt_br se a escolha for inválida

# Pedir o nome do arquivo de entrada
entrada = input("Digite o nome do arquivo de entrada (ex: arquivo.json): ").strip()

# Verificar se o arquivo existe
if os.path.exists(entrada):
    # Gerar o nome do arquivo de saída com o prefixo do idioma escolhido
    idioma_destino = escolher_idioma()
    nome_arquivo, extensao = os.path.splitext(entrada)
    saida = idioma_destino + "_" + nome_arquivo + extensao  # Prefixo com o idioma

    # Executar a tradução
    traduzir_json(entrada, saida, idioma_destino)
else:
    print("Erro: O arquivo de entrada não foi encontrado.")
