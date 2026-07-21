from pathlib import Path

def relatorio_final(retorno: list):
    print("=" * 40)
    print("Relatorio Final da movientação dos arquivos:")
    print("=" * 40)

    for file in retorno:
        if file == 'True':
            continue
        else:
            objeto_retorno = file.split('%%%', 2)

            print("Arquivo", Path(objeto_retorno[0]).name, "movido para", Path(objeto_retorno[1]).name)

    return True