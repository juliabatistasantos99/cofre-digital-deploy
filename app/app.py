import os
import logging
from flask import Flask, jsonify
from app.security import MaskingFormatter, log_decorator

# 1. Criando a aplicação Flask
app = Flask(__name__)

# 2. Configurando logging avançado com máscara de segurança
handler = logging.StreamHandler()
handler.setFormatter(MaskingFormatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


@app.route('/')
def home():
    logger.info("Acessando a rota inicial do Cofre Digital.")
    return jsonify({
        "message": "Cofre Digital Online!",
        "environment": os.getenv('ENVIRONMENT', 'unknown'),
        "version": os.getenv('APP_VERSION', '1.0.0')
    })

# 3. Simulando conexão com banco usando o decorator seguro


@app.route('/database')
@log_decorator
def database_info():
    db_host = os.getenv('DB_HOST', 'localhost')
    db_user = os.getenv('DB_USER', 'user')
    db_password = os.getenv('DB_PASSWORD', 'SENHA_NAO_CONFIGURADA')

    # Este log será interceptado e a senha será mascarada automaticamente!
    logger.info(
        f"Conectando ao banco em {db_host} com user='{db_user}' e password='{db_password}'")

    return jsonify({
        "host": db_host,
        "user": db_user,
        "password": "MASCARADA_NOS_LOGS"
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
