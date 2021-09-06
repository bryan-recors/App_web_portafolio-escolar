from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

def index(request):
    return render(request,'index.html',{
    })

def login_view(request):
    if request.user.is_authenticated:
        messages.success(request,'Ya existe una sesión abierta')
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user:
            login(request,user)
            usuario = request.user
            if user.has_perm('alumno.profesor'):
                messages.success(request,'Bienvenido profesor {}'.format(user.username))
                return redirect('home_docente')
            elif user.has_perm('alumno.estudiante'):
                messages.success(request,'Bienvenido estudiante {}'.format(user.username))
                return redirect('home_estudiante')
            messages.success(request,'Bienvenido {}'.format(user.username))
            return redirect('login')
        else:
            messages.error(request,'Usuario o contraseña no validos')
    return render(request,'usuario/login.html',{

    })

def logout_view(request):
    logout(request)
    messages.success(request,'Sesión cerrada exitosamente')
    return redirect('login')
