import requests
import os
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

def verifica_dimensoes_imagem(path_imagem):
    imagem = Image.open(path_imagem)
    largura, altura = imagem.size

    saida_formatada = "({}, {})".format(altura, largura)

    print(saida_formatada)


if __name__ == "__main__":
    url = input()
    pasta_destino = "./"
    path_imagem = "./imagem.png"

    baixar_e_salvar_imagem(url, pasta_destino)
    verifica_dimensoes_imagem(path_imagem)


# url = "https://drive.google.com/u/3/uc?id=1AabXYkvemO0hCDZC5iYJKP0xdOQsdJt7&export=download"