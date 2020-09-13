from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password2']
        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username you entered is not available.')
                return redirect('register')    
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email you entered is not available.')
                    return redirect('register')    
                else:
                    user = User.objects.create_user(username=username, password=password,
                    first_name=first_name, last_name=last_name, email=email)
                    user.save()
                    messages.success(request, 'You\'ve successfuly created an account. Now you can log in.')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords don\'t match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == "POST":
        login_user()
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')