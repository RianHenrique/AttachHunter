from imap_client import connect_and_fetch_emails
from attachment_handler import save_attachments
from utils.logger import logger
from utils.helpers import log_configuracoes

def main():
    
    try:
        log_configuracoes()
        logger.info("Iniciando processo de download de anexos...")

        # Conecta, encontra a pasta correta e busca os e-mails
        emails = connect_and_fetch_emails()

        # Salva os anexos de cada e-mail
        save_attachments(emails)

        logger.info("✅ Processo finalizado com sucesso!")

    except Exception as e:
        logger.exception(f"❌ Erro inesperado durante a execução: {e}")

if __name__ == "__main__":
    main()








   