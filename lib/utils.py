from datetime import datetime
from decimal import Decimal


def obter_periodo_do_dia():
    """
    Gera uma saudação de acordo com o período do dia:
        Bom dia
        Boa tarde
        Boa noite
    :args
        None.
    :returns
        [str] - Saudação de acordo com o período do dia.
    """    
    agora = datetime.now()
    hora = agora.hour

    periodos_saudacao = {
        (0, 12): 'Bom dia ☀️',
        (12, 18): 'Boa tarde ☀️',
        (18, 24): 'Boa noite 🌛'
    }

    for periodo, saudacao in periodos_saudacao.items():
        inicio, fim = periodo
        if inicio <= hora < fim:
            return saudacao
        

# Calcula os dias restantes para o vencimento
def calcular_dias_restantes(data_vencimento):
    """
    Calcula os dias restantes para o vencimento da parcela a partir da data atual.
    :args
        None.
    :returns
        [str] - Com o número de dias para o vencimento.
    """
    hoje = datetime.now()
    #dt_vencimento = datetime.strptime(data_vencimento, '%d/%m/%Y')
    dias_restantes = (data_vencimento - hoje).days
    return dias_restantes


def formatar_numero(numero):
    """    
    Formata um número no padrão pt_BR-UTF-8 (1.234,56).
    :args
        [int/float] - Número para conversão.
    :returns
        [int/float] - Número formatado.
    """
    # Usar Decimal para garantir precisão
    numero_decimal = Decimal(numero).quantize(Decimal('0.01'))
    # Formatar usando f-string e substituir ponto por vírgula
    numero_formatado = f"{numero_decimal:,.2f}".replace('.', 'X').replace(',', '.').replace('X', ',')
    return numero_formatado


