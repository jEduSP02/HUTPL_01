
FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN apt-get update && apt-get install -y build-essential libpq-dev &&     pip install --no-cache-dir -r requirements.txt &&     apt-get purge -y build-essential && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*
COPY . /app
CMD ["sh", "-c", "python manage.py collectstatic --noinput && python manage.py migrate && gunicorn herbario.wsgi:application --bind 0.0.0.0:8000"]
