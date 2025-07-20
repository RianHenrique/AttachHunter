import os
from config import DOWNLOAD_DIR
from utils.logger import logger, logger_file_only
from utils.helpers import truncate_text, log_summary
from config import VALID_EXTENSIONS, LOG_EMAILS_WITHOUT_ATTACHMENTS, MAX_ATTACHMENT_SIZE_BYTES, MAX_ATTACHMENT_SIZE_MB


def save_attachments(emails):

    """
        Salva os anexos dos e-mails recebidos na pasta configurada.
        Os arquivos são renomeados de forma informativa (data de envio, remetente e nome original)
        e tratados para evitar sobrescritas, mesmo que tenham nomes repetidos.
    """

    # Cria a pasta de download se não existir
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    total_saved = 0
    total_skipped = 0
    total_no_attachments = 0

    for msg in emails:
        # Identificadores para compor o nome do arquivo
        date_str = msg.date.strftime("%Y-%m-%d")
        sender = sanitize_filename(msg.from_)


        for att in msg.attachments:

            # Verifica se a extensão do anexo é válida
            if not att.filename.lower().endswith(VALID_EXTENSIONS):
                logger.warning(f"⚠️  Anexo ignorado (extensão não permitida): {att.filename} | Data de envio: {msg.date.strftime('%Y-%m-%d')} | Remetente: {msg.from_}")
                total_skipped += 1
                continue

            # Verifica se o anexo é muito grande
            if is_attachment_too_large(att, msg):
                total_skipped += 1
                continue

            # Cria o nome do arquivo com base na data, remetente e nome original
            base_name = sanitize_filename(att.filename)
            name, ext = os.path.splitext(base_name)
            filename_base = f"{date_str}-{sender}-{name}"
            filename = f"{filename_base}{ext}"
            filepath = os.path.join(DOWNLOAD_DIR, filename)

            # Evita sobrescrita se mesmo nome for gerado
            counter = 1
            while os.path.exists(filepath):
                filename = f"{filename_base}_{counter}{ext}"
                filepath = os.path.join(DOWNLOAD_DIR, filename)
                counter += 1

            try:
                # Salva o anexo
                with open(filepath, "wb") as f:
                    f.write(att.payload)

                total_saved += 1

            except Exception as e:
                logger.exception(
                    f"❌ Erro ao salvar o anexo: {att.filename} | Caminho: {filepath} | "
                    f"Remetente: {msg.from_} | Data: {msg.date.strftime('%Y-%m-%d')}"
                )
                total_skipped += 1 


        no_attachments = len(msg.attachments) == 0
        subject_limited = truncate_text(msg.subject)
        
        # Se o e-mail não tiver anexos, printa no terminal se a configuração permitir
        if no_attachments:

            total_no_attachments += 1
            
            if LOG_EMAILS_WITHOUT_ATTACHMENTS:
                logger.warning(f"⚠️  E-mail sem anexos | Assunto: {subject_limited} | Data: {msg.date.strftime('%Y-%m-%d')} | Remetente: {msg.from_}")
            else:
                logger_file_only.warning(f"⚠️  E-mail sem anexos | Assunto: {subject_limited} | Data: {msg.date.strftime('%Y-%m-%d')} | Remetente: {msg.from_}")


    log_summary(total_saved, total_skipped, total_no_attachments)





def sanitize_filename(name: str) -> str:
    """Remove caracteres problemáticos para nomes de arquivo"""
    return "".join(c if c.isalnum() or c in "-_." else "_" for c in name)

def is_attachment_too_large(att, msg) -> bool:
    """
        Verifica se o anexo é muito grande.
        Retorna True se o anexo for maior que o limite configurado.
    """
    size = len(att.payload)
    if size > MAX_ATTACHMENT_SIZE_BYTES:
        logger.warning(
            f"⚠️  Anexo ignorado (ultrapassa o tamanho permitido): {att.filename} "
            f"| Tamanho: {size / (1024 * 1024):.2f} MB "
            f"| Limite: {MAX_ATTACHMENT_SIZE_MB} MB "
            f"| Remetente: {msg.from_} | Data: {msg.date.strftime('%Y-%m-%d')}"
        )
        return True
    return False

