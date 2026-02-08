FROM python:3.9-slim

WORKDIR /app

# Copiar requirements
COPY paso_01_setup/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar aplicación
COPY paso_05_api/api.py .
COPY paso_04_modelado/modelo_final.pkl .

# Exponer puerto
EXPOSE 5000

# Comando para ejecutar
CMD ["python", "api.py"]

