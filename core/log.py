import datetime
from pathlib import Path

def gerar_log(arquivos: list, pasta: str, status: list):

    # Pegar data e hora atual
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dt = dt.replace(" ", "_")
    dt = dt.replace(":", "-")

    # Criar nome do arquivo log com data+hora 2000-01-01_12-00-00
    log_name = 'Log_'+dt+'.txt'

    # Pega o caminho da pasta Log
    file = Path(__file__).parent.parent / 'logs' / log_name

    # Cria o arquivo
    file.touch(exist_ok=True)

    # Texto do log
    log = 'Log ' + dt + '\nRealizado na pasta ' + pasta 

    # Informações de execução
    for statu in status:
        log = log + statu

    # Caso tenha erro não gravar informações de arquivos
    if 'Erro' in status:
        return
    
    # Informações dos arquivos
    for arquivo in arquivos:
        if arquivo == 'True':
            continue
        else:
            objeto_retorno = arquivo.split('%%%', 2)
        log = log + "\nOrigem: " + objeto_retorno[0] + " Destino: " + objeto_retorno[1]

    if 'True' in log:
        log.replace('True', '')
    elif 'False' in log:
        log.replace('False', '')

    # Cria o arquivo com o texto do log
    with file.open("a", encoding="utf-8") as f:
        f.write(log)

    return