from skimage import io

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

def frequenciaNiveisCinza(path_imagem):
  imagem = Image.open(path_imagem).convert('L')
  freq = [0] * 256
  w, h = imagem.size

  for i in range(h):
    for j in range(w):
      pixel = imagem.getpixel((j, i))
      freq[pixel] += 1

  return freq1
# Recebe uma imagem em niveis de cinza (matriz 2D de inteiros).
# Devolve uma outra imagem com o resultado da media.
def filtroMedia (f, n):
  f = Image.open(f).convert('L')
  f = np.array(f)

  h, w = f.shape
  g = np.zeros_like (f)
  for i in range(h):
    for j in range(w):
      tot = 0
      soma = 0
      for k in range (-n, n+1):
        for l in range (-n, n+1):
          i2 = i + k
          j2 = j + l
          if i2 >= 0 and i2 < h and j2 >= 0 and j2 < w:
            tot += 1
            soma += f[i2,j2]
      g[i,j] = int (soma / tot)
  
  return g


if __name__ == "__main__":
#   url = input()
  pasta_destino = "./"
  path_imagem = "./imagem.png"

#   baixar_e_salvar_imagem(url, pasta_destino)
  frequenciaAntesFiltragem = frequenciaNiveisCinza(path_imagem)

  imagemFiltrada = filtroMedia(path_imagem, 1)

  frequenciaAposFiltragem = frequenciaNiveisCinza(imagemFiltrada)

  print(frequenciaAntesFiltragem)
  print(frequenciaAposFiltragem)
