import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def plotar_histograma(hist, titulo="Histograma"):
    plt.figure()
    plt.title(titulo)
    plt.plot(hist, color='blue')
    plt.xlabel("Bins")
    plt.ylabel("Frequência")
    plt.show()

def calcular_histograma(imagem_path):
    imagem = cv2.imread(imagem_path)
    if imagem is None:
        print(f"Erro ao carregar imagem: {imagem_path}")
        return None

    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    # Usa apenas o canal de Matiz (H)
    hist = cv2.calcHist([hsv], [0], None, [180], [0, 180])
    cv2.normalize(hist, hist, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    return hist

# Caminho da pasta com imagens de fundo de referência
caminho_fundos = "S17_CONF_REF"

# Lista para armazenar histogramas dos fundos
histogramas_fundo = []

if not os.path.exists(caminho_fundos):
    print(f"Erro: o caminho {caminho_fundos} não existe.")
elif not os.path.isdir(caminho_fundos):
    print(f"Erro: {caminho_fundos} não é uma pasta.")
else:
    for nome_arquivo in os.listdir(caminho_fundos):
        caminho_imagem = os.path.join(caminho_fundos, nome_arquivo)
        if os.path.isfile(caminho_imagem) and nome_arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
            hist = calcular_histograma(caminho_imagem)
            if hist is not None:
                histogramas_fundo.append(hist)
    print(f"{len(histogramas_fundo)} histogramas carregados da pasta '{caminho_fundos}'.")

def comparar_com_fundos(imagem_teste_path):
    hist_teste = calcular_histograma(imagem_teste_path)
    if hist_teste is None:
        print("Erro ao calcular histograma da imagem de teste.")
        return
    
   ## plotar_histograma(hist_teste, titulo=f"Histograma da imagem teste: {os.path.basename(imagem_teste_path)}")
    similares = 0
    for i, hist_fundo in enumerate(histogramas_fundo):
        similaridade = cv2.compareHist(hist_teste, hist_fundo, cv2.HISTCMP_CORREL)
      ##  print(f"Similaridade com fundo {i + 1}: {similaridade:.4f}")
       ## plotar_histograma(hist_teste, titulo=f"Histograma da imagem teste: {os.path.basename(imagem_teste_path)}")
        if similaridade > 0.7:  # Tente ajustar esse valor conforme necessidade
            similares += 1

    if similares >= 70:  # Pode ajustar o número mínimo de correspondências
        print("Fundo reconhecido! Vezes:" + str(similares) + " - " + imagem_teste_path)
        pasta_destino = "frames_conf3_teste_deletar_depois"

        os.makedirs(pasta_destino, exist_ok=True)

        # Lê a imagem
        imagem = cv2.imread(imagem_teste_path)

        # Define o novo caminho
        nome_arquivo = os.path.basename(imagem_teste_path)
        caminho_destino = os.path.join(pasta_destino, nome_arquivo)

        # Salva a cópia
        cv2.imwrite(caminho_destino, imagem)


    #else:
       #print("Fundo desconhecido! Vezes:" + str(similares) + " - " + imagem_teste_path)

# Exemplo de uso
comparar_com_fundos(r"frames\frame_01_42.jpg")

pasta_frames = 'framesep2_teste'


# Percorre todos os arquivos da pasta
for nome_arquivo in os.listdir(pasta_frames):
    # Garante que é uma imagem (por exemplo, .jpg, .png, etc.)
    if nome_arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
        caminho_completo = os.path.join(pasta_frames, nome_arquivo)
        comparar_com_fundos(caminho_completo) 
 
