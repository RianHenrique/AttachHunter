# import logging
# from datetime import datetime

# logger = logging.getLogger("email_downloader")
# logger.setLevel(logging.INFO)

# # Formato para exibir no terminal
# console_handler = logging.StreamHandler()
# console_handler.setFormatter(logging.Formatter("[%(levelname)s] - %(message)s"))
# logger.addHandler(console_handler)

# # Gera nome do arquivo com data e hora
# log_filename = datetime.now().strftime("logs/log_%Y-%m-%d_%H-%M-%S.txt")
# file_handler = logging.FileHandler(log_filename, encoding="utf-8")
# file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
# logger.addHandler(file_handler)


import logging
from datetime import datetime

# Logger principal: imprime no terminal e salva no arquivo
logger = logging.getLogger("email_downloader")
logger.setLevel(logging.INFO)

# Handler para exibir no terminal
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("[%(levelname)s] - %(message)s"))
logger.addHandler(console_handler)

# Gera nome do arquivo com data e hora
log_filename = datetime.now().strftime("logs/log_%Y-%m-%d_%H-%M-%S.txt")
file_handler = logging.FileHandler(log_filename, encoding="utf-8")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# Adiciona o file handler ao logger principal
logger.addHandler(file_handler)

# Logger exclusivo para salvar apenas no arquivo
logger_file_only = logging.getLogger("logger_file_only")
logger_file_only.setLevel(logging.INFO)
logger_file_only.addHandler(file_handler)
