from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

def home(request):
    return render(request, 'home.html', {'name':'Siddharth'})

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'User Created')
                messages.info(request, 'Please Login')
        else:
            messages.info(request, 'Password not matching')
    return redirect('/')


def login(request):
    username = request.POST['login_username']
    password = request.POST['login_password']

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return render(request, 'success_login.html', {'name': username})
    else:
        messages.info(request, 'Invalid Credentials')
        return redirect('/#')


def logout(request):
    auth.logout(request)
    return redirect('/#')
