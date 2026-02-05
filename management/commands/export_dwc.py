
from django.core.management.base import BaseCommand
import csv
from pathlib import Path
from apps.specimens.models import Specimen

class Command(BaseCommand):
    help = 'Exporta datos básicos en CSV con mapeo Darwin Core simplificado.'

    def handle(self, *args, **options):
        export_dir = Path('exports')
        export_dir.mkdir(exist_ok=True)
        file_path = export_dir / 'dwc_occurrence.csv'
        # Mapeo simple a Darwin Core: occurrenceID, scientificName, eventDate, decimalLatitude, decimalLongitude, catalogNumber
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'occurrenceID','scientificName','eventDate','decimalLatitude','decimalLongitude','catalogNumber'
            ])
            writer.writeheader()
            for s in Specimen.objects.select_related('taxon','event').all():
                writer.writerow({
                    'occurrenceID': s.id,
                    'scientificName': s.taxon.scientific_name if s.taxon else '',
                    'eventDate': s.event.date.isoformat() if s.event and s.event.date else '',
                    'decimalLatitude': s.event.latitude if s.event else '',
                    'decimalLongitude': s.event.longitude if s.event else '',
                    'catalogNumber': s.code,
                })
        self.stdout.write(self.style.SUCCESS(f'Exportación creada: {file_path}'))
