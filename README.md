# Eliana Bot

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Eliana Bot é um robô de automação para o WhatsApp confeccionado para a loja de moda feminina Elegantia.
Desenvolvido para auxiliar no controle financeiro interno e agregar comodidade e utilidade aos clientes, enviando mensagens personalizadas, que informam que restam X dias para a data de vencimento das parcelas, baseando-se na diferença entre o vencimento e o dia que a lojista executa o robô.

## Funcionalidades

- Extração de dados de uma planilha Excel.
- Cálculo dos dias restantes para o vencimento da parcela.
- Envio de mensagens personalizadas via WhatsApp Web.
- Registro de logs para monitoramento e depuração.
- Notificação de falhas no envio de mensagens.
- Criação de um arquivo de conferência com as remessas que falharam (em desenvolvimento).

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```plaintext
eliana_bot/
|
│── elina_bot/
│   ├── __init__.py
├── lib/
│   ├── log.py
│   └── utils.py
├── log/
│   ├── log.txt
|
├── enviar.png
├── eliana_bot.py
├── elegiantia.xlsx
└── README.md
```

- lib/: Contém módulos auxiliares (log.py e utils.py).
- enviar.png: Imagem usada pelo pyautogui para localizar o botão de envio no WhatsApp Web.
- eliana_bot.py: Script principal que executa o robô.
- elegantia.xlsx: Planilha de exemplo usada para testar o robô.
- README.md: Documentação do projeto.

## Instalação
Siga os passos abaixo para configurar o ambiente e executar o Eliana Bot:

Clone o repositório:
```
git clone https://github.com/adrianooliveiradefaria/eliana_bot.git
cd eliana_bot
```

Instale o poetry:
```
https://python-poetry.org/docs/basic-usage/
```

Instale as dependências:
```
poetry install
```

Ative o ambiente virtual:
```
poetry shell
```

## Uso
Para executar o Eliana Bot, utilize o seguinte comando:
```
python eliana_bot.py
```

Certifique-se de que o arquivo elegantia.xlsx está na raiz do projeto e contenha os dados corretos.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato
Desenvolvido por Adriano Faria - adriano@conectasolucoes.com.br
