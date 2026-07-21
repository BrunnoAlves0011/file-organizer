from pathlib import Path
from settings import FILE_TYPES

def create_folders(lt_extension: list, pasta: str, simula: bool):

    for ext in lt_extension:
        if ext in FILE_TYPES:
            path = pasta + '\\' + FILE_TYPES[ext]
        else:
            path = pasta + '\\Outros'
        directory_path = Path(path)
        try:
            directory_path.mkdir()
        except FileExistsError:
            continue
        except Exception as e:
            print(f"Erro: {e}")
            return False

    return True