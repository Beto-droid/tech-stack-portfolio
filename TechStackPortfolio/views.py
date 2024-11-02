"""
Render Home portfolio
"""
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from TechStackPortfolio.form import LoginForm

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('main_portfolio_presentation_cv_home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})

def crispy_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if request.headers.get('HX-Request'):
                    return JsonResponse({"redirect": "/"})
                return redirect('/')
            else:
                form.add_error(None, "Invalid username or password.")
                return render(request, 'registration/login_partial_htmx.html', {'form': form})
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

def crispy_register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_portfolio_presentation_cv_home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})