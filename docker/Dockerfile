# 1. Base da imagem com Python (segurança)
FROM python:3.10-slim

# 2. Definindo diretório de trabalho
WORKDIR /app

# 3. Copiando arquivos do projeto para o container
COPY app/ /app/app/

# 4. Instalando dependências necessárias
RUN pip install --no-cache-dir flask

# 5. Mudando para usuário não-root (boa prática de segurança)
USER 1000

# 6. Expondo a porta da aplicação
EXPOSE 5000

# 7. Comando de inicialização
CMD ["python", "-m", "app.app"]
