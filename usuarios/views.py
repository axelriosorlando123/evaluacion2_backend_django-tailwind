from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from catalogo.models import Cliente  # Importamos el modelo Cliente

# Vista de Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email:
            try:
                user_obj = User.objects.get(email=email)
                username = user_obj.username
            except User.DoesNotExist:
                messages.error(request, 'No existe una cuenta con ese correo electrónico.')
                return render(request, 'usuarios/login.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            return redirect('home')
        else:
            messages.error(request, 'Usuario, correo o contraseña incorrectos.')

    return render(request, 'usuarios/login.html')


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Sesión cerrada correctamente.')
    return redirect('home')


# Vista de Registro con creación de Cliente
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        email = request.POST.get('email')
        rut = request.POST.get('rut')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        if form.is_valid():
            user = form.save(commit=False)
            user.email = email
            user.save()

            # Crear automáticamente el Cliente asociado
            Cliente.objects.create(
                rut=rut,
                nombre=user.username,
                correo=email,
                telefono=telefono,
                direccion=direccion
            )

            login(request, user)
            messages.success(request, '¡Cuenta creada exitosamente y cliente registrado!')
            return redirect('home')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = UserCreationForm()

    return render(request, 'usuarios/register.html', {'form': form})



