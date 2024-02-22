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

  return freq, h, w, imagem

def probabilidade(frequencia, h, w):
  prob = np.array (frequencia) / (h*w)

  return prob

def probAcumuladas(prob):
  probAc = [0] * 256
  probAc[0] = prob[0]
  for i in range (1, 256):
    probAc[i] = probAc[i-1] + prob[i]

  return probAc

def calculaEqualizacaoHistograma(h, w, imagem, probAcumulada):
  imEq = imagem.copy()

  for i in range(h):
    for j in range(w):
      pixel = imagem.getpixel((j, i))
      novo_pixel = int(probAcumulada[pixel] * 255)
      imEq.putpixel((j, i), novo_pixel)

  return imEq

def calculoFrequenciaNiveisCinzaImEq(imagem):
  freq = [0] * 256
  w, h = imagem.size

  for i in range(h):
    for j in range(w):
      pixel = imagem.getpixel((j, i))
      freq[pixel] += 1

  return freq

if __name__ == "__main__":
#   url = input()
  pasta_destino = "./"
  path_imagem = "./imagem.png"

#   baixar_e_salvar_imagem(url, pasta_destino)
  freq, h, w, imagem = calculoFrequenciaNiveisCinza(path_imagem)
  prob = probabilidade(freq, h, w)
  probAcumulada = probAcumuladas(prob)
  imEq = calculaEqualizacaoHistograma(h, w, imagem, probAcumulada)

  freqImEq = calculoFrequenciaNiveisCinzaImEq(imEq)  

  print(freq)
  print (freqImEq)