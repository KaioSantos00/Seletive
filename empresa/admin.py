from django.contrib import admin

# Register your models here.
from .models import Empresa, Tecnologias, Vagas

admin.site.register(Tecnologias)
admin.site.register(Empresa)
admin.site.register(Vagas)