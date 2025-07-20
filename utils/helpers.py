from utils.logger import logger
from config import (
    EMAIL, IMAP_SERVER, FOLDER, DOWNLOAD_DIR,
    VALID_EXTENSIONS, ONLY_UNSEEN, MARK_AS_SEEN, LOG_EMAILS_WITHOUT_ATTACHMENTS, MAX_ATTACHMENT_SIZE_MB
)

# Função para exibir as configurações carregadas
def log_configuracoes():
    logger.info( "═" * 60)
    logger.info("🧩  CONFIGURAÇÕES CARREGADAS".center(60))
    logger.info("═" * 60)

    logger.info(f"📧  E-mail: {EMAIL}")
    logger.info(f"🌐  Servidor IMAP: {IMAP_SERVER}")
    logger.info(f"📂  Pasta de leitura: {FOLDER}")
    logger.info(f"💾  Pasta de download: {DOWNLOAD_DIR}")
    logger.info(f"🧷  Extensões permitidas: {VALID_EXTENSIONS}")
    logger.info(f"📎  Tamanho máximo do anexo: {MAX_ATTACHMENT_SIZE_MB} MB")
    logger.info(f"🔍  Buscar apenas e-mails não lidos? {ONLY_UNSEEN}")
    logger.info(f"👁️   Marcar como lido após leitura? {MARK_AS_SEEN}")
    logger.info(f"📭  Log de e-mails sem anexos: {LOG_EMAILS_WITHOUT_ATTACHMENTS}")
    logger.info("═" * 60 + "\n")


def log_summary(saved, skipped, no_attachments):
    logger.info("")
    logger.info("📥 RESUMO DO PROCESSAMENTO")
    logger.info("-" * 40)
    logger.info(f"📊 Total de anexos salvos: {saved}")
    logger.info(f"🚫 Total de anexos ignorados : {skipped}")
    logger.info(f"📭 Total de e-mails sem nenhum anexo: {no_attachments}")
    logger.info("-" * 40)
    logger.info("")



def truncate_text(text: str, max_length: int = 80) -> str:
    """
        Limita o tamanho de um texto e adiciona "..." no final se ultrapassar o limite.
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."