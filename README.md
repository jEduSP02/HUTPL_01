
# Herbario – Django Starter

Plantilla mínima para la Actividad 3.

## Requisitos
- Docker y Docker Compose

## Inicio rápido
```bash
cp .env.example .env
# Ajusta variables si es necesario
docker compose up --build -d
# Migraciones y superusuario
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

## Endpoints
- Admin: http://localhost:8000/admin/
- API
  - /api/taxa/
  - /api/events/
  - /api/specimens/
  - /api/genetics/samples/
  - /api/genetics/sequences/
  - /api/loans/
  - /api/specimens/{id}/qr/

## Exportación Darwin Core (CSV)
```bash
docker compose exec web python manage.py export_dwc
ls exports/
```

## Notas
- Para PostGIS, habilitar GeoDjango y usar `django.contrib.gis` + base de datos PostGIS.
- Integra Leaflet en tus formularios para capturar coordenadas.
