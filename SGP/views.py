from django.shortcuts import render

from .forms import RegistradoTaRol

# Create your views here.
def inicio(request):
	titulo = "Registro de Roles"
	form = RegistradoTaRol(request.POST or None)
	#if request.user.is_authenticated():
		#titulo="Hola, %s!" %(request.user) #%s es un string q toma el valor de %(request.user)
	context = {
		"titulo_template":titulo,
		"form":form
	}

	if form.is_valid():
		instance = form.save()
		nombre=form.cleaned_data.get("nombre")
		context = {
			"titulo_template" : "Gracias %s, ya se ha registrado" %(nombre)
		}

	return render(request, "inicio.html",context)