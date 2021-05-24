from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContact


def login(request):
    # print(request.POST)
    # If the post fields are empty -> Avoid error or information messages
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
    # Authenticates the user to the Django database
    user = auth.authenticate(request, username=username, password=password)
    # print(user)
    if not user:
        messages.error(request, 'Usuário ou senha invalidos!')
        return render(request, 'accounts/login.html')
    else:
        # Logs in the authenticated user
        auth.login(request, user)
        messages.success(request, f'Login de {user} realizado com sucesso!')
        return redirect('index')


def logout(request):
    # auth.logout(request)
    # return redirect('logout')
    return render(request, 'accounts/logout.html')


def off(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    # print(request.POST)
    # If the post fields are empty -> Avoid error or information messages
    if request.method != 'POST':
        return render(request, 'accounts/register_.html')
    else:
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

    if not name:
        messages.error(request, 'O campo do seu nome está vázio')
        return render(request, 'accounts/register_.html')
    if not surname:
        messages.error(request, 'O campo do seu sobrenome está vázio')
        return render(request, 'accounts/register_.html')
    if not email:
        messages.error(request, 'O campo do seu e-mail está vázio')
        return render(request, 'accounts/register_.html')
    elif User.objects.filter(email=email).exists():
        messages.error(request, f'O email {email} já esta cadastrado!!')
        return render(request, 'accounts/register_.html')
    else:
        try:
            validate_email(email)
        except:
            messages.error(request, 'E-mail Invalido.')
            return render(request, 'accounts/register_.html')
    if not username:
        messages.error(request, 'O campo do nome do usuário está vázio.')
        return render(request, 'accounts/register_.html')
    elif len(username) < 6:
        messages.error(request, 'O nome do usuário de ter no mínimo 6 catacteres!')
        return render(request, 'accounts/register_.html')
    elif User.objects.filter(username=username).exists():
        messages.error(request, f'O usuario {username} já esta cadastrado!!')
        return render(request, 'accounts/register_.html')
    if not password_1:
        messages.error(request, 'O campo de senha está vázio.')
        return render(request, 'accounts/register_.html')
    elif len(password_1) < 8:
        messages.error(request, 'A senha deve ter no mínimo 8 carateres.')
        return render(request, 'accounts/register_.html')
    if not password_2:
        messages.error(request, 'O campo de confirmação da senha está vázio')
        return render(request, 'accounts/register_.html')
    elif password_2 != password_1:
        messages.error(request, 'As senha são diferentes!')
        return render(request, 'accounts/register_.html')
    messages.success(request, 'Cadastro com sucesso!')

    # Creates the user
    user = User.objects.create_user(username=username,
                                    email=email,
                                    password=password_1,
                                    first_name=name,
                                    last_name=surname)
    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    # If the form is empty
    if request.method != 'POST':
        form_contact = FormContact()
        return render(request, 'accounts/dashboard.html', {'form': form_contact})
    # Receives form fields (POST) and attached file (FILE)
    form_return = FormContact(request.POST, request.FILES)
    # If the validation performed by Django is not positive
    if not form_return.is_valid():
        # Returns the form with the data entered by the user
        form_contact = FormContact(request.POST)
        messages.error(request, 'Dados inconsitentes - verifique!')
        return render(request, 'accounts/dashboard.html', {'form': form_contact})

    # Command template for reading fields individually
    email = request.POST.get('email')

    messages.success(request, f'Cadastro de '
                              f'{request.POST.get("name")} '
                              f'{request.POST.get("surname")} '
                              f'realizado com sucesso!')
    form_return.save()
    return redirect('dashboard')
