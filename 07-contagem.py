import requests
import os
import numpy as np
from PIL import Image

def baixar_e_salvar_imagem(url, pasta_destino):
    try:
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            caminho_imagem = os.path.join(pasta_destino, 'imagem.png')
            
            with open(caminho_imagem, 'wb') as arquivo:
                arquivo.write(resposta.content)

        else:
            print("Erro ao acessar a URL da imagem.")
    except Exception as e: 
        print(f"Ocorreu um erro: {e}")

def contagem_pixels(path_imagem):
    image = Image.open(path_imagem)
    
    image = image.convert('L')
    
    pixels = np.array(image.getdata())

    contagem_pixels = [0] * 256

    for pixel in pixels:
        contagem_pixels[pixel] += 1

    return contagem_pixels

if __name__ == "__main__":
    url = input()
    pasta_destino = "./"
    path_imagem = "./imagem.png"

    baixar_e_salvar_imagem(url, pasta_destino)
    contagem_pixels = contagem_pixels(path_imagem)
    
    print(contagem_pixels)