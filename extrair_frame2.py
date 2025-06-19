import os
import subprocess

def extrair_frames_ffmpeg(video_path, output_dir="framesep2", intervalo=2):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Comando FFmpeg para extrair 1 frame a cada `intervalo` segundos
    comando = [
        "ffmpeg",
        "-i", video_path,
        "-vf", f"fps=1/{intervalo}",
        os.path.join(output_dir, "temp_%04d.jpg")
    ]

    print("Extraindo frames com ffmpeg...")
    subprocess.run(comando, check=True)
    print("Extração concluída.")

    # Renomear os arquivos com minuto e segundo
    renomear_frames(output_dir, intervalo)

def renomear_frames(pasta, intervalo):
    arquivos = sorted(f for f in os.listdir(pasta) if f.startswith("temp_"))
    for i, nome in enumerate(arquivos):
        tempo = i * intervalo
        minutos = tempo // 60
        segundos = tempo % 60
        novo_nome = f"frame_{minutos:02d}_{segundos:02d}.jpg"
        caminho_antigo = os.path.join(pasta, nome)
        caminho_novo = os.path.join(pasta, novo_nome)
        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {novo_nome}")

if __name__ == "__main__":
    extrair_frames_ffmpeg("S17EP2.mp4", intervalo=2)
