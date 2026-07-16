from pathlib import Path
# from settings import *

def listar_arquivos(pasta: str):
    lt_arquivos: list = []
    # path_used = pasta
    lv_caminho = Path(pasta)

    if not lv_caminho.exists():
        raise FileNotFoundError("Pasta não encontrada.")

    for lv_arquivo in lv_caminho.iterdir():
        if lv_arquivo.is_file():
            lt_arquivos.append(lv_arquivo)  

    return lt_arquivos