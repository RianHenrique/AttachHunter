# 📨 Email Attachment Downloader

Automatize o processo de download de anexos com segurança e controle. Ideal para empresas que recebem um grande fluxo de currículos, propostas ou outros arquivos via e-mail.

---

## 📌 Descrição

Este projeto em Python conecta-se a uma conta de e-mail via IMAP, acessa uma pasta específica e baixa automaticamente os anexos dos e-mails que estiverem nela, considerando apenas extensões válidas e respeitando um tamanho máximo configurável por anexo. Todas as configurações são feitas via arquivo .env, e todo o processo é registrado no terminal e também em arquivos de log .txt.

---

## 🚀 Funcionalidades

- 🔐 Conexão segura via IMAP.
- 📂 Busca e leitura de e-mails em pastas específicas.
- 📎 Download automático de anexos (.pdf, .doc, .docx).
- 🧼 Nomes de arquivos sanitizados para evitar erros.
- 🧾 Evita sobrescrita de arquivos com nomes iguais.
- 🛑 Ignora anexos inválidos ou grandes demais.
- 📋 Log completo no terminal e em arquivo `.txt` com data/hora.
- 🧪 Registro de e-mails sem anexos no Terminal (opcional).
- ⚙️ Configuração 100% via arquivo `.env`.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.13.4
- [imap-tools](https://github.com/ikvk/imap_tools)
- python-dotenv
- logging (módulo padrão do Python)

---

## 📁 Estrutura do Projeto

```
AttachHunter/
│
├── utils/                          # Funções auxiliares e gerenciamento de logs
│   ├── logger.py                  # Configuração dos loggers (terminal e arquivo)
│   ├── helpers.py                 # Funções utilitárias, como truncamento de texto e sumário de logs
│   └── __init__.py                # Arquivo necessário para tratar 'utils' como um pacote
│
├── config.py                      # Carrega e valida as configurações definidas no .env
├── .env.example                   # Exemplo de variáveis de ambiente que devem ser definidas
│
├── main.py                        # Ponto de entrada da aplicação, orquestra todo o processo
├── imap_client.py                 # Conecta ao servidor IMAP e busca os e-mails conforme as regras
├── attachment_handler.py          # Processa os e-mails e salva os anexos conforme os critérios
│
├── logs/                          # Pasta onde os arquivos de log são salvos automaticamente
│   └── log_YYYY-MM-DD_HH-MM-SS.txt # Arquivos de log com data e hora no nome
│
└── requirements.txt              # Dependências necessárias para rodar o projeto

```

---

## 🧪 Como Usar

### 1. Clone o repositório

```bash
git clone https://github.com/RianHenrique/AttachHunter.git
cd AttachHunter
```

### 2. Crie e edite o arquivo `.env`

```bash
cp .env.example .env
```

Preencha suas credenciais e configurações no `.env`.

### 3. Instale as dependências

```bash
pip3 install -r requirements.txt
```

### 4. Execute o script

```bash
python main.py
```

---

## 🛠️ Variáveis de Configuração (.env)

| Variável                           | Descrição |
|------------------------------------|-----------|
| `EMAIL_USERNAME`                   | E-mail de login |
| `EMAIL_PASSWORD`                   | Senha do e-mail |
| `IMAP_SERVER`                      | Host do servidor IMAP |
| `EMAIL_FOLDER`                     | Nome da pasta com os e-mails |
| `DOWNLOAD_DIR`                     | Pasta onde salvar os anexos |
| `VALID_EXTENSIONS`                | Extensões válidas (ex: `.pdf,.docx`) |
| `MAX_ATTACHMENT_SIZE_MB`          | Tamanho máximo permitido por anexo (em MB) |
| `ONLY_UNSEEN`                     | Buscar apenas e-mails não lidos (`True` ou `False`) |
| `MARK_AS_SEEN`                    | Marcar como lido após leitura (`True` ou `False`) |
| `LOG_EMAILS_WITHOUT_ATTACHMENTS` | Define se e-mails sem anexos devem ser registrados no terminal. Se `False`, serão registrados apenas no arquivo de log (`True` ou `False`) |


---

## 💡 Exemplo de Log

```bash
[INFO] - Iniciando processo de download de anexos...
[INFO] - 📁 Pasta IMAP encontrada: INBOX.Curriculos
[INFO] - 📨 Buscando e-mails...
[INFO] - ✅ 5 e-mails encontrados.
[WARNING] - ⚠️  Anexo ignorado (extensão não permitida): exemplo.exe
[INFO] - 📊 Total de anexos salvos: 3
[INFO] - 🚫 Total de anexos ignorados: 1
[INFO] - 📭 Total de e-mails sem nenhum anexo: 1
```

---

