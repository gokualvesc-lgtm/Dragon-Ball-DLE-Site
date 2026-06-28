import os
import numpy as np
from PIL import Image
from rembg import remove

PASTA_ENTRADA = "imagens_salvas"
PASTA_SAIDA = "silhuetas"

os.makedirs(PASTA_SAIDA, exist_ok=True)

for arquivo in os.listdir(PASTA_ENTRADA):

    if not arquivo.lower().endswith(
        (".png", ".jpg", ".jpeg", ".webp")
    ):
        continue

    caminho = os.path.join(PASTA_ENTRADA, arquivo)

    try:
        print(f"Processando {arquivo}...")

        # Abre imagem
        img = Image.open(caminho).convert("RGBA")

        # Remove fundo
        img = remove(img)

        arr = np.array(img)

        # Fundo branco
        resultado = np.ones((arr.shape[0], arr.shape[1], 3),
                            dtype=np.uint8) * 255

        # Tudo que não for transparente vira preto
        mascara = arr[:, :, 3] > 0

        resultado[mascara] = [0, 0, 0]

        nome = os.path.splitext(arquivo)[0]

        Image.fromarray(resultado).save(
            os.path.join(PASTA_SAIDA, f"{nome}.jpg"),
            quality=95
        )

        print(f"✅ {nome}.jpg")

    except Exception as erro:
        print(f"❌ Erro em {arquivo}: {erro}")

print("Concluído!")