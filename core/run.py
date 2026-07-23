from settings import *

# Funções
from core.scanner import listar_arquivos
from core.separator import file_separator
from core.folder_create import create_folders
from core.move_file import file_move
from core.relatorio import relatorio_final
from core.log import gerar_log

def run_organizer(pasta: str, simula: bool, exibir_relatorio: bool):

    status = []

    return
    # print("=" * 40)
    # print("📂 FileOrganizer")
    # print("=" * 40)
    
    try:
        # Caminho da pasta a ser realizado o escaneamento dos arquivos
        # pasta = input("Digite o caminho da pasta: ")
    
        # Obtem uma lista dos arquivos presentes na pasta
        arquivos = listar_arquivos(pasta)

        # Informa a quantidade de arquivos encontrados
        status.append(f"\nEncontrados {len(arquivos)} arquivo(s).\n")

        # Com os arquivos extrai as extenções dos arquivos baseado no dicionario FILE_TYPES
        extension = file_separator(arquivos, simula)
        
        # Cria as pastas com referencia as exetenções dos arquivos extaidas
        folder = create_folders(extension, pasta, simula)

        if  folder == True:
            # Sucesso ao criar as pastas, seguir com movimentação
            status.append('Pastas criadas com sucesso!')

            # Com as pastas criadas, mover os arquivos para sua respectiva pasta
            move_return = file_move(arquivos, pasta, simula)
            if move_return[0] == 'True':
                status.append('Arquivos movidos com sucesso!')
                if exibir_relatorio == True:
                    # Com os arquivos em suas pastas mostrar relatório dos arquivos alterados
                    relatorio_final(move_return)
            else:
                status.append('Erro ao mover arquivos!')
                # algo aconteceu
        elif simula == True:
            return
        else:
            status.append('Erro ao criar pastas!')
            # algo aconteceu

    except Exception as erro:
        status.append(f"\nErro: {erro}")

    gerar_log(move_return, pasta, status)