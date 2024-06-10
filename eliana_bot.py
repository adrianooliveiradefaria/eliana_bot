import csv
import locale
import subprocess
import webbrowser
from textwrap import dedent
from time import sleep
from urllib.parse import quote

import openpyxl
import pyautogui

from lib.log import logger
from lib.utils import (calcular_dias_restantes, formatar_numero,
                       obter_periodo_do_dia)

# Permissão para Print Screen no gerenciador gráfico Wayland
comando_adicionar_usuario = "xhost +SI:localuser:$(whoami)"
permissao = subprocess.run(
    comando_adicionar_usuario,
    shell=True,
    check=True,
    text=True,
    capture_output=True
)

# Definindo os padrões brasileiros de data, hora e número à aplicação
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def processar_dados(arquivo):
    """
    Extrai dados da planilha em que a linha contenha informções completas.
    :args
        [str] - Nome do arquivo da planilha localizada na raiz da aplicação.
    :returns
        None.
    """
    # Verifica a existência do arquivo
    try:
        workbook = openpyxl.load_workbook(arquivo)  # ('elegantia.xlsx')
    except Exception as e:
        logger.critical(
            f'Erro ao abrir {arquivo}. Verifique sua existência.'
        )
        exit(1)

    # Seleciona a primeira Planilha do arquivo
    try:
        planilha = 'Planilha1'
        planilha_clientes = workbook[planilha]
    except Exception as e:
        f'Planilha {planilha} não encontrada no arquivo {arquivo}.'
        exit(1)

    for linha in planilha_clientes.iter_rows(min_row=2):
        if linha[1].value:
            nome = linha[0].value
            telefone = linha[1].value
            valor = linha[2].value
            vencimento = linha[3].value
            dias_restantes = calcular_dias_restantes(vencimento)
            print(nome, telefone, valor, vencimento)

            # Personalizando link de envio pelo WhatsApp
            # Site com a lista dos códigos Unicode para emoji:
            # https://emojipedia.org/pt
            msg = dedent(f'''
            Olá, *{nome}*!  {obter_periodo_do_dia()}.
            Sou a _*Eliana*_, a assistente virtual 🤖 da *Elegantia Moda*.

            Rapidinho... só para te informar que sua parcela de {formatar_numero(valor)} vence em *{dias_restantes}* dias.

            Espero ter ajudado no seu controle financeiro. 😉
            '''
            )

            endpoint_whatsapp = f'https://web.whatsapp.com/send?phone=55{
                telefone}&text={quote(msg)}'
            # Configução para rodar no Brave
            browser_command = '/usr/bin/google-chrome'
            webbrowser.register(
                'chrome',
                None,
                webbrowser.Chrome(browser_command)
            )
            try:
                # webbrowser.open(endpoint_whatsapp) # utiliza o navegador padrão
                webbrowser.get('chrome').open(endpoint_whatsapp)
                sleep(round(20, 30))
            except Exception as e:
                logger.critical(
                    f'Erro ao carregar o WhatsApp Web. {e}'
                )
                exit(1)

            try:
                botao_enviar = pyautogui.locateCenterOnScreen('enviar.png')
                sleep(10)
                pyautogui.click(botao_enviar[0], botao_enviar[1])
                sleep(8)
                pyautogui.hotkey('ctrl', 'w')
                sleep(5)
            except Exception as e:
                logger.error(
                    f'Erro ao enviar a mensagem para {
                        nome} - {telefone}. Enviando para arquivo de erro.'
                )
                arquivo_csv = 'FalhaNoEnvio.csv'
                with open(arquivo_csv, mode='a', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow([
                        nome, telefone, valor, vencimento, dias_restantes
                    ])
                continue


# Rodando a aplicação
if __name__:
    processar_dados('elegantia.xlsx')
    exit(0)
