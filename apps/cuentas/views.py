from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Enviar correo de bienvenida
            send_mail(
                'Bienvenido a la plataforma',
                f'Hola {user.username}, gracias por registrarte.',
                os.environ.get('DEFAULT_FROM_EMAIL'),
                [user.email],
                fail_silently=False,
            )
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegistroForm()
    return render(request, 'registration/register.html', {'form': form})

from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'login'

