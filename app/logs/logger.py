import logging
import logging.handlers

# Логер выводящий информацию о всех изменениях (кроме чтения) и Info

def main_log():
    file_handler = logging.FileHandler(filename='logs.log')
    logging.basicConfig(level=logging.WARNING, format='%(asctime)s || %(name)s || %(message)s || %(levelname)s',
                        handlers=[file_handler])
    logger = logging.getLogger(__name__)
    return logger
