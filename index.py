from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):# Função para baixar um vídeo do YouTube
  try:
    # Cria uma instância do objeto YouTube com a URL fornecida
    yt = YouTube(url)
    # Filtra os streams para obter apenas os que têm vídeo e áudio juntos e formato mp4
    streams = yt.streams.filter(progressive=True, file_extension="mp4")
     # Obtém a stream com a maior resolução disponível
    highest_res_stram = streams.get_highest_resolution()
     # Baixa o vídeo no diretório especificado pelo usuário
    highest_res_stram.download(output_path=save_path)
    print("Vídeo baixado com sucesso")

  except Exception as e:
    print(e)

def open_file_dialog_():
  folder = filedialog.askdirectory()
  if folder:
    print(f"Pasta escolhida: {folder}")
  return folder

if __name__ == "__main__":
  root = tk.Tk()
  root.withdraw()

  video_url = input("Escreva a URL: ")
  save_dir = open_file_dialog_()

  if not save_dir: 
    print("Escolha uma pasta: ") # Instrução para o usuário escolher uma pasta
  else: 
    download_video(video_url, save_dir)# Baixa o vídeo do YouTube