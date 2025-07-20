from imap_tools import MailBox, AND
from config import EMAIL, PASSWORD, IMAP_SERVER, FOLDER, ONLY_UNSEEN, MARK_AS_SEEN
from utils.logger import logger
from imap_tools.message import MailMessage
from typing import List


def get_real_folder_name(mailbox: MailBox, folder_keyword: str) -> str:

    """
        Busca uma pasta no IMAP que contenha o texto informado.
        Retorna o nome real completo (ex: INBOX.Curriculos).
    """

    folders = mailbox.folder.list()
    for folder in folders:
        if folder_keyword.lower() in folder.name.lower():
            return folder.name  # Nome exato reconhecido pelo servidor

    raise ValueError(f'Pasta {folder_keyword} não encontrada. Pastas disponíveis:\n' +
                 "\n".join([f.name for f in folders]))




def connect_and_fetch_emails() -> List[MailMessage]:

    """
        Conecta ao servidor IMAP, acessa a pasta configurada e retorna os e-mails encontrados.
        Aplica filtro de leitura e marcação de leitura com base nas configurações do .env.
    """

    try:
        logger.info("🔌 Conectando ao servidor IMAP...")
        with MailBox(IMAP_SERVER).login(EMAIL, PASSWORD) as mailbox:
            real_folder = get_real_folder_name(mailbox, FOLDER)
            logger.info(f"📁 Pasta IMAP encontrada: {real_folder}")
            
            mailbox.folder.set(real_folder)
            logger.info("📨 Buscando e-mails...")

            # Se configurado, busca apenas e-mails não lidos. Caso contrário, busca todos.
            if ONLY_UNSEEN:
                criteria = AND(seen=False)
                emails = list(mailbox.fetch(criteria=criteria, mark_seen=MARK_AS_SEEN))
            else:
                emails = list(mailbox.fetch(mark_seen=MARK_AS_SEEN))


            logger.info(f"✅ {len(emails)} e-mails encontrados.")
            logger.info("")
            
            return emails
    except Exception as e:
        logger.exception("❌ Erro ao conectar e buscar e-mails:")
        return []
