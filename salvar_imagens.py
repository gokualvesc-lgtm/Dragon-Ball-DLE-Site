import sqlite3
import requests
import os
import time

# Pasta onde as imagens serão salvas
PASTA_IMAGENS = "imagens_salvas"
os.makedirs(PASTA_IMAGENS, exist_ok=True)

# Busca todos os personagens da API
print("Baixando lista de personagens da API...")

url = "https://dragonball-api.com/api/characters?limit=1000"
resposta = requests.get(url)

if resposta.status_code != 200:
    print("Erro ao acessar a API.")
    exit()

dados = resposta.json()

# Cria um dicionário para facilitar a busca
api_personagens = {}

for personagem in dados["items"]:
    nome = personagem["name"].lower().strip()
    api_personagens[nome] = personagem["image"]

# Conecta ao banco
conn = sqlite3.connect("PersonagensDB.db")
cursor = conn.cursor()

cursor.execute("SELECT nome FROM personagens")
personagens_db = cursor.fetchall()

print(f"Encontrados {len(personagens_db)} personagens no banco.\n")

for (nome,) in personagens_db:

    nome_busca = nome.lower().strip()

    if nome_busca not in api_personagens:
        print(f"❌ Não encontrado na API: {nome}")
        continue

    imagem_url = api_personagens[nome_busca]

    try:
        imagem = requests.get(imagem_url, timeout=15)

        if imagem.status_code == 200:

            extensao = imagem_url.split(".")[-1].split("?")[0]
            if len(extensao) > 5:
                extensao = "png"

            caminho = os.path.join(
                PASTA_IMAGENS,
                f"{nome}.{extensao}"
            )

            with open(caminho, "wb") as arquivo:
                arquivo.write(imagem.content)

            print(f"✅ Baixado: {nome}")

        else:
            print(f"❌ Erro ao baixar: {nome}")

    except Exception as erro:
        print(f"❌ {nome}: {erro}")

    time.sleep(0.2)

conn.close()

print("\nConcluído!")