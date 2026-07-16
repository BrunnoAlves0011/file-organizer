from pathlib import Path

def create_folders(lt_extension: list, pasta: str):

    for ext in lt_extension:
        path = pasta + '\\' + ext
        directory_path = Path(path)
        try:
            directory_path.mkdir()
        except FileExistsError:
            print(f"Pasta '{ext}' já existe")
        except Exception as e:
            print(f"Erro: {e}")
            return False

    return True