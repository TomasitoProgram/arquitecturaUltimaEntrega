from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import OrdenForm, ElementoOrdenForm
from .models import Orden

def home(request):
    return render(request, 'home.html')

def user_login(request):
    context = {}

    if request.method == 'POST':
        # Usar paréntesis con `get`
        username = request.POST.get("username")  # Obtener el valor del campo 'username'
        password = request.POST.get("password")  # Obtener el valor del campo 'password'

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Llama correctamente a la función `auth_login`
            return redirect('home')  # Redirige a la página 'home'
        else:
            context['error'] = "Usuario o contraseña inválidos."

    return render(request, 'login.html', context)
def user_logout(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login')  # Redirige al formulario de login o donde prefieras

def ordenes(request):
    return render(request, 'crear_orden.html')

def menu_admin(request):
    return render(request, 'menu_admin.html')

def lista_ordenes(request):
    ordenes = Orden.objects.all()  # Obtiene todas las órdenes de la base de datos
    return render(request, 'lista_ordenes.html', {'ordenes': ordenes})

def crear_orden(request):
    if request.method == 'POST':
        print('blup')
        form = OrdenForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('lista_ordenes')  # Redirige a una página que liste las órdenes
    else:
        form = OrdenForm()
    return render(request, 'crear_orden.html', {'form': form})

def actualizar_orden(request, pk):
    orden = get_object_or_404(Orden, pk=pk)
    if request.method == 'POST':
        form = OrdenForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('lista_ordenes')  # Redirige a la página de lista de órdenes
    else:
        form = OrdenForm(instance=orden)
    return render(request, 'actualizar_orden.html', {'form': form, 'orden': orden})

def eliminar_orden(request, pk):
    orden = get_object_or_404(Orden, pk=pk)
    if request.method == 'POST':
        orden.delete()
        return redirect('lista_ordenes')  # Redirige a la página de lista de órdenes
    return render(request, 'eliminar_orden.html', {'orden': orden})
