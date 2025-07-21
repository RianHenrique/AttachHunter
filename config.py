from dotenv import load_dotenv
import os

load_dotenv()  # Carrega o .env

# ==== Credenciais e Conexão ====
EMAIL = os.getenv("EMAIL_USERNAME")
PASSWORD = os.getenv("EMAIL_PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER", "email-ssl.com.br")
FOLDER = os.getenv("EMAIL_FOLDER", "INBOX.Curriculos")

# ==== Diretórios e Filtros ====
DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR", "Curriculos")
VALID_EXTENSIONS = tuple(
    ext.strip().lower() for ext in os.getenv("VALID_EXTENSIONS", ".pdf,.doc,.docx").split(",")
)

# ==== Limite de anexo ====
MAX_ATTACHMENT_SIZE_MB = float(os.getenv("MAX_ATTACHMENT_SIZE_MB", "5"))
MAX_ATTACHMENT_SIZE_BYTES = MAX_ATTACHMENT_SIZE_MB * 1024 * 1024

# ==== Flags de comportamento ====
def str_to_bool(s):
    return str(s).lower() in ("true", "1", "yes")

ONLY_UNSEEN = str_to_bool(os.getenv("ONLY_UNSEEN", "False"))
MARK_AS_SEEN = str_to_bool(os.getenv("MARK_AS_SEEN", "False"))
LOG_EMAILS_WITHOUT_ATTACHMENTS = str_to_bool(os.getenv("LOG_EMAILS_WITHOUT_ATTACHMENTS", "False"))


