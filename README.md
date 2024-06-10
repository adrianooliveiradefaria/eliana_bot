# Eliana Bot

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Eliana Bot é um robô de automação para o WhatsApp. Desenvolvido para auxiliar no controle financeiro da empresa e gerar comodidade e um serviço aos clientes, enviando mensagens personalizadas, X dias antes da data de vencimento das parcelas.

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
│
├── lib/
│   ├── __init__.py
│   ├── log.py
│   └── utils.py
├── log/
│   ├── __init__.py
│   ├── log.txt
|
├── enviar.png
├── eliana_bot.py
├── elegiantia.xlsx
├── pyproject.txt
└── README.md

lib/: Contém módulos auxiliares (log.py e utils.py).
enviar.png: Imagem usada pelo pyautogui para localizar o botão de envio no WhatsApp Web.
eliana_bot.py: Script principal que executa o robô.
elegantia.xlsx: Planilha de exemplo usada para testar o robô.
pyproject.txt: Arquivo de configuração do poetry.
README.md: Documentação do projeto.

Instalação
Siga os passos abaixo para configurar o ambiente e executar o Eliana Bot:

Clone o repositório:
git clone https://github.com/adrianooliveiradefaria/eliana_bot.git
cd eliana_bot

Instale o poetry:
https://python-poetry.org/docs/basic-usage/

Instale as dependências:
poetry install

Ative o ambiente virtual:
poetry shell

Uso
Para executar o Eliana Bot, utilize o seguinte comando:
python eliana_bot.py

Certifique-se de que o arquivo elegantia.xlsx está na raiz do projeto e contenha os dados corretos.

Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Contato
Desenvolvido por Adriano Faria - adriano@conectasolucoes.com.br
