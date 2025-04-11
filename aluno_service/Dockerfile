FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos do serviço
COPY . .

# Instala dependências
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy pydantic

RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy pydantic email-validator

# Expõe a porta padrão do FastAPI
EXPOSE 8000

# Comando para iniciar o serviço
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
