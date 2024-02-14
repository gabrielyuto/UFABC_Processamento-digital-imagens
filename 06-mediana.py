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

def mediana_niveis_de_cinza(path_imagem):
    image = Image.open(path_imagem)
    
    image = image.convert('L')
    
    gray_array = np.array(image.getdata())    
    median_gray = np.median(gray_array)
    
    return median_gray

def resultado_formatado(resultado):
    saida_formatada = "{:.1f}".format(resultado)
    print(saida_formatada)

if __name__ == "__main__":
    url = input()
    pasta_destino = "./"
    path_imagem = "./imagem.png"

    baixar_e_salvar_imagem(url, pasta_destino)
    media_gray = mediana_niveis_de_cinza(path_imagem)
    
    resultado_formatado(media_gray)