import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import shutil

# Função para organizar os arquivos
def organizar_arquivos(diretorio_downloads):
    arquivos = Path(diretorio_downloads).iterdir()

    for arquivo in arquivos:
        if arquivo.is_file():
            extensao = arquivo.suffix[1:]
            if extensao:
                pasta_extensao = Path(diretorio_downloads) / extensao
                pasta_extensao.mkdir(exist_ok=True)
                shutil.move(str(arquivo), str(pasta_extensao / arquivo.name))
            else:
                pasta_outros = Path(diretorio_downloads) / 'outros'
                pasta_outros.mkdir(exist_ok=True)
                shutil.move(str(arquivo), str(pasta_outros / arquivo.name))

# Função para abrir o seletor de diretório
def selecionar_diretorio():
    pasta = filedialog.askdirectory()
    if pasta:
        organizar_arquivos(pasta)
        status_label.config(text=f"Arquivos organizados em:\n{pasta}")

# Criação da interface
janela = tk.Tk()
janela.title("Organizador de Arquivos")
janela.geometry("400x150")

instrucoes = tk.Label(janela, text="Clique no botão abaixo e escolha o diretório:")
instrucoes.pack(pady=10)

botao = tk.Button(janela, text="Selecionar Diretório", command=selecionar_diretorio)
botao.pack(pady=5)

status_label = tk.Label(janela, text="")
status_label.pack(pady=10)

janela.mainloop()
