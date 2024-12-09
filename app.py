from PIL import Image
import os

# Caminhos dos diretórios
imagem_base_path = "C:/Users/caiog/OneDrive/Área de Trabalho/project 1/Sem título.png"  # Caminho da imagem base
imagens_pasta_path = "C:/Users/caiog/OneDrive/Área de Trabalho/project 1/fotos"  # Pasta com as imagens
output_pasta_path = "C:/Users/caiog/OneDrive/Área de Trabalho/project 1/prontas"  # Pasta para salvar resultados

# Coordenadas do retângulo na imagem base
retangulo_coords = (138, 264, 330, 540)  # (esquerda, topo, direita, base)

# Carrega a imagem base
imagem_base = Image.open(imagem_base_path)

# Garante que a pasta de saída existe
os.makedirs(output_pasta_path, exist_ok=True)

# Processa cada imagem na pasta
for arquivo in os.listdir(imagens_pasta_path):
    if arquivo.lower().endswith((".png", ".jpg", ".jpeg")):  # Processa apenas imagens
        # Caminho da imagem de origem
        imagem_path = os.path.join(imagens_pasta_path, arquivo)

        # Abre a imagem de origem
        imagem_overlay = Image.open(imagem_path)

        # Redimensiona a imagem para caber no retângulo
        largura_destino = retangulo_coords[2] - retangulo_coords[0]
        altura_destino = retangulo_coords[3] - retangulo_coords[1]
        imagem_overlay = imagem_overlay.resize((largura_destino, altura_destino))

        # Cria uma cópia da imagem base para edição
        imagem_editada = imagem_base.copy()

        # Cola a imagem redimensionada na cópia da imagem base
        imagem_editada.paste(imagem_overlay, (retangulo_coords[0], retangulo_coords[1]))

        # Converte para RGB antes de salvar (para evitar erro com JPEG)
        imagem_editada = imagem_editada.convert("RGB")

        # Salva a nova imagem com o nome do arquivo original
        output_path = os.path.join(output_pasta_path, arquivo)
        imagem_editada.save(output_path)

print(f"Processo concluído! As imagens foram salvas na pasta: {output_pasta_path}")
