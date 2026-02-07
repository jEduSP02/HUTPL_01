
import os
from django.core.wsgi import get_wsgi_application
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'herbario.settings')
application = get_wsgi_application()

User = get_user_model()
if os.getenv("CREATE_SUPERUSER") == "1":
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@outlook.com", "01234")
        print("Superusuario creado automáticamente.")
