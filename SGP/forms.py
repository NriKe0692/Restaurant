from django import forms
from .models import TaRol
from .models import TaUsuario
from .models import TaTipoPlatillo
from .models import TaPlatillo
from .models import TaEstadoPlatillo
from .models import TaDetalle

class RegistradoTaRol(forms.ModelForm):
	class Meta:
		model = TaRol
		fields = ["nombre"]

class RegistrarUsuarios(forms.ModelForm):
	class Meta:
		model = TaUsuario
		fields = ["idusuario","idrol","clave","estado"]

class RegistrarTipoPlatillo(forms.ModelForm):
	class Meta:
		model = TaTipoPlatillo
		fields = ["idtipoplatillo","nombre"]

class RegistrarPlatillo(forms.ModelForm):
	class Meta:
		model = TaPlatillo
		fields = ["nombre","precio","idtipoplatillo","idestadoplatillo"]

class RegistrarEstadoPlatillo(forms.ModelForm):
	class Meta:
		model = TaEstadoPlatillo
		fields = ["nombre"] 	

class RegistrarDetalle(forms.ModelForm):
	class Meta:
		model = TaDetalle
		fields = ["idpedido","idplatillo","cantidad","precioparcial"]
	