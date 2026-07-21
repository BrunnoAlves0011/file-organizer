import shutil
from settings import FILE_TYPES

def file_move(arquivos: list, source: str):
    retorno = []
    retorno.append('True')

    for arquivo in arquivos:
        try:
            ext = str(arquivo).split('.', 2)
            ext = ext[1].lower()
            if ext in FILE_TYPES:
                dest = source + '\\' + FILE_TYPES[ext]
            else:
                dest = source + '\\Outros'
            shutil.move(str(arquivo), dest)
            retorno.append(str(str(arquivo) + '%%%' + dest))
        except Exception as e:
            print(f"Erro: {e}")
            retorno[0] = 'False'
            return retorno

    return retorno