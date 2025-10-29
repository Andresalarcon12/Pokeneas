# Build stage
FROM python:3.12-slim

# Evita prompts interactivos en apt
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Instalar dependencias del sistema (build essentials mínimos si hiciera falta)
# y limpiar cachés para imagen pequeña
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Crear carpeta app
WORKDIR /app

# Copiar requirements primero (mejor caché)
COPY requirements.txt /app/requirements.txt

# Instalar deps (incluye gunicorn para producción)
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt \
 && pip install --no-cache-dir gunicorn==22.0.0


COPY . /app

# Puerto de la app
EXPOSE 5000

# Variables opcionales (puedes sobreescribirlas en Swarm)
ENV FLASK_ENV=production \
    PYTHONPATH=/app

# Comando de arranque con gunicorn (app = instancia en run.py)
# -w 2 yendo a 2 workers
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "run:app"]
