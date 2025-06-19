import face_recognition
import os

# Caminho da pasta com as fotos
pasta = "frames_conf3_teste_deletar_depois"
rostos_conhecidos = []
nomes_rostos = []
contagem = []

# Percorrer os arquivos da pasta
for arquivo in os.listdir(pasta):
    if arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
        caminho = os.path.join(pasta, arquivo)
        print(f"🔍 Processando {arquivo}...")

        imagem = face_recognition.load_image_file(caminho)
        codificacoes = face_recognition.face_encodings(imagem)

        print(f"👉 {len(codificacoes)} rosto(s) encontrado(s) em {arquivo}")

        for rosto in codificacoes:
            encontrado = False

            for i, conhecido in enumerate(rostos_conhecidos):
                resultado = face_recognition.compare_faces([conhecido], rosto, tolerance=0.5)

                if resultado[0]:
                    contagem[i] += 1
                    encontrado = True
                    break

            if not encontrado:
                rostos_conhecidos.append(rosto)
                nomes_rostos.append(arquivo)
                contagem.append(1)

print("\n✅ Processamento concluído!")
print("🔢 Resultados finais:")

for nome, qtd in zip(nomes_rostos, contagem):
    print(f"{nome}: {qtd} aparições")