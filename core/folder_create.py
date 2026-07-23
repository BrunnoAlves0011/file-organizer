from pathlib import Path
from settings import FILE_TYPES
from core.simula import simula_organizer

def create_folders(lt_extension: list, pasta: str, simula: bool):

    if simula == False:
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
    else:
        simula_organizer(lt_extension, pasta)
        return False
    return True