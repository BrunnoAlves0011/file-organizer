# from settings import *

def file_separator(arquivos_lista: list, simula: bool):
    lt_extension = []
    for file in arquivos_lista:
        lv_file = str(file).split('.', 2)
        lt_extension.append(lv_file[1].lower())

    lt_extension = list(set(lt_extension))

    return lt_extension
