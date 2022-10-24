from django.contrib import admin
from apps.libro.models import *

# Register your models here.
admin.site.register(Autor)
admin.site.register(libro)
admin.site.register(Editorial)
admin.site.register(Categoria)
admin.site.register(Idioma)
admin.site.register(Reserva)
