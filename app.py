from core.scanner import listar_arquivos
from settings import *

def main():
    print("=" * 40)
    print("📂 FileOrganizer")
    print("=" * 40)

    pasta = input("Digite o caminho da pasta: ")

    try:
        arquivos = listar_arquivos(pasta)

        print(f"\nEncontrados {len(arquivos)} arquivo(s).\n")

        for arquivo in arquivos:
            print(arquivo.name)

    except Exception as erro:
        print(f"\nErro: {erro}")


if __name__ == "__main__":
    main()