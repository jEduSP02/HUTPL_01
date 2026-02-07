FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencias del sistema (psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el proyecto
COPY . /app

# Copia el entrypoint
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# (Opcional) Si ya no compilas nada en runtime, puedes purgar build-essential
# RUN apt-get purge -y build-essential && apt-get autoremove -y

# Por convención, Render inyecta $PORT
ENV PORT=8000

ENTRYPOINT ["/app/entrypoint.sh"]
