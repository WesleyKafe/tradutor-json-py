# Descrição:

Este script traduz arquivos JSON automaticamente para o idioma de sua escolha. Ele utiliza a biblioteca `googletrans` para realizar a tradução de valores em um arquivo JSON. O script suporta tradução para diversos idiomas, incluindo português (Brasil), espanhol, francês, alemão, italiano, russo, japonês e chinês. O arquivo de saída será gerado com o prefixo do idioma escolhido.

## :heavy_exclamation_mark: Pré-requisitos:

Python: Certifique-se de ter o Python 3.6 ou superior instalado no seu sistema.

## :book: Instalações necessárias:

- `googletrans`: Usada para realizar traduções automáticas.
- `tqdm`: Biblioteca para exibir a barra de progresso durante o processo de tradução.
- `os`: Biblioteca nativa do Python para manipulação de arquivos e diretórios.

## :book: Instruções de Instalação:

No terminal ou prompt de comando, execute o seguinte comando para instalar as bibliotecas externas necessárias:


`pip install googletrans tqdm`


`
## :book: Principais Funcionalidades:

Permite ao usuário escolher o idioma de destino para a tradução (por exemplo, pt_br, es, fr, de, etc.).
Traduz os valores de um arquivo JSON, mantendo a estrutura original.
Adiciona o prefixo do idioma escolhido no nome do arquivo de saída (ex: pt_br_arquivo.json).
Exibe uma barra de progresso para facilitar o acompanhamento da tradução.
O script pode ser executado diretamente no terminal, sem a necessidade de configurações adicionais.


## :book: Como Funciona:
Escolher o Idioma: O script solicita ao usuário que escolha o idioma de destino para a tradução (ex: português, espanhol, francês, etc.).
Ler o Arquivo JSON: O script lê o arquivo JSON de entrada.
Traduzir os Valores: Ele traduz todos os valores de texto do arquivo JSON para o idioma selecionado.
Salvar o Arquivo Traduzido: O arquivo traduzido é salvo com o prefixo do idioma no nome, como pt_br_arquivo.json.
Progresso: O script exibe uma barra de progresso durante o processo de tradução.


## Uso:
Execute o script no terminal.
Informe o nome do arquivo JSON de entrada.
Escolha o idioma de destino para a tradução.
O arquivo traduzido será gerado com o prefixo do idioma selecionado no mesmo diretório.


:octocat: Créditos

@WesleyKafe - Desenvolvedor do código.
