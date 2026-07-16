from settings import *
from core.scanner import listar_arquivos
from core.separator import file_separator
from core.folder_create import create_folders
from core.move_file import file_move

def main():
    print("=" * 40)
    print("📂 FileOrganizer")
    print("=" * 40)

    pasta = input("Digite o caminho da pasta: ")

    try:
        # Obtem os arquivos presentes na pasta
        arquivos = listar_arquivos(pasta)

        print(f"\nEncontrados {len(arquivos)} arquivo(s).\n")

        # Pega as exetenções dos arquivos
        extension = file_separator(arquivos)

        # Cria as pastas referente as exetenções dos arquivos
        folder = create_folders(extension, pasta)

        if  folder == True:
            # Seguir com movimentação
            print('Pastas criadas com sucesso!')

            # Com as pastas criadas, mover os arquivos para sua respectiva pasta
            file_move()
        else:
            print('Erro ao criar pastas!')
            # algo aconteceu

    except Exception as erro:
        print(f"\nErro: {erro}")


if __name__ == "__main__":
    main()