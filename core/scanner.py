from pathlib import Path
from settings import *

def listar_arquivos(pasta: str):
    path_used = pasta
    caminho = Path(pasta)

    if not caminho.exists():
        raise FileNotFoundError("Pasta não encontrada.")

    for arquivo in caminho.iterdir():
        if arquivo.is_file():
            arquivos_lista.append(arquivo)  

    # return [arquivo for arquivo in caminho.iterdir() if arquivo.is_file()]
    return arquivos_lista