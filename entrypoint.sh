#!/bin/sh
set -e

echo "==> Esperando variables requeridas..."
: "${PORT:?PORT no está definido}"
# Si usas DB en Render:
# : "${DATABASE_URL:?DATABASE_URL no está definido}"

echo "==> Verificando que no falten migraciones..."
python manage.py makemigrations --check --dry-run

echo "==> Ejecutando migraciones..."
python manage.py migrate --noinput

echo "==> Recolectando estáticos..."
python manage.py collectstatic --noinput

echo "==> Iniciando Gunicorn en el puerto $PORT..."
exec gunicorn herbario.wsgi:application --bind 0.0.0.0:$PORT --workers 3 --timeout 120
