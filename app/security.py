import re
import logging


class MaskingFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%', validate=True):
        super().__init__(fmt, datefmt, style, validate)
        # Padrões para mascarar chaves e senhas comuns nos logs
        self.patterns = [
            (r'(password=["\'])(.*?)(["\'])', r'\1*******\3'),
            (r'(key=["\'])(.*?)(["\'])', r'\1*******\3'),
            (r'(token=["\'])(.*?)(["\'])', r'\1*******\3'),
            (r'(DB_PASSWORD=["\'])(.*?)(["\'])', r'\1*******\3')
        ]

    def format(self, record):
        message = super().format(record)
        for pattern, replacement in self.patterns:
            message = re.sub(pattern, replacement, message)
        return message


def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__module__)
        logger.info(f"Chamando a função de segurança: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.error(f"Erro na função {func.__name__}: {str(e)}")
            raise e
    return wrapper
