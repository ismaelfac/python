from django.contrib import admin

# Register your models here.
from .forms import RegModelForm
from .models import Registrado

class AdminRegistrado(admin.ModelAdmin):
   list_display = ["__unicode__","nombre","timestamp"]
   form = RegModelForm
   #list_display_links = ["nombre"] # no aplica con email, por que este es __unicode__
   list_filter = ["timestamp"] #filtros
   list_editable = ["nombre"]  # columna editable
   search_fields = ["email","nombre"] # Busqueda por nombre y email
   #class Meta:
   #  model = Registrado

admin.site.register(Registrado, AdminRegistrado)
