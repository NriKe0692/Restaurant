from django.contrib import admin
from .forms import RegistradoTaRol
from .forms import RegistrarUsuarios
from .forms import RegistrarTipoPlatillo
from .forms import RegistrarPlatillo
from .forms import RegistrarEstadoPlatillo
from .forms import RegistrarDetalle
from .models import TaRol
from .models import TaUsuario
from .models import TaTipoPlatillo
from .models import TaEstadoPlatillo
from .models import TaPlatillo
from .models import TaDetalle

# Register your models here.
class ListaRoles(admin.ModelAdmin):
	form = RegistradoTaRol
	list_display = ["__unicode__","idrol","nombre"]
admin.site.register(TaRol,ListaRoles)

class ListaUsuarios(admin.ModelAdmin):
	form = RegistrarUsuarios
	list_display = ["__unicode__","idusuario","idrol","clave","estado"]
admin.site.register(TaUsuario,ListaUsuarios)

class ListaTipoPlatillo(admin.ModelAdmin):
	form = RegistrarTipoPlatillo
	list_display = ["__unicode__","idtipoplatillo","nombre"]
admin.site.register(TaTipoPlatillo,ListaTipoPlatillo)

class ListaEstadoPlatillo(admin.ModelAdmin):
	form=RegistrarEstadoPlatillo
	list_display=["__unicode__","idestadoplatillo","nombre"]
admin.site.register(TaEstadoPlatillo,ListaEstadoPlatillo)

class ListaPlatillo(admin.ModelAdmin):
	form=RegistrarPlatillo
	list_display=["__unicode__","idplatillo","nombre","precio","idtipoplatillo","idestadoplatillo"]
admin.site.register(TaPlatillo,ListaPlatillo)

class ListaDetalle(admin.ModelAdmin):
	form =  RegistrarDetalle
	list_display = ["idpedido","idplatillo","cantidad","precioparcial"]
admin.site.register(TaDetalle, ListaDetalle)