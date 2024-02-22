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

def calculoFrequenciaNiveisCinza(path_imagem):
  imagem = Image.open(path_imagem).convert('L')
  freq = [0] * 256
  w, h = imagem.size

  for i in range(h):
    for j in range(w):
      pixel = imagem.getpixel((j, i))
      freq[pixel] += 1

  return freq, h, w

def probabilidade(frequencia, h, w):
  prob = np.array (frequencia) / (h*w)

  return prob

if __name__ == "__main__":
  url = input()
  pasta_destino = "./"
  path_imagem = "./imagem.png"

  baixar_e_salvar_imagem(url, pasta_destino)
  freq, h, w = calculoFrequenciaNiveisCinza(path_imagem)
  prob = probabilidade(freq, h, w)

  print(prob)