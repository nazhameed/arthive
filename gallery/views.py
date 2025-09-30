from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    # Show landing page with login/register forms if not logged in
    if request.user.is_authenticated:
        return redirect('dashboard')
    login_form = AuthenticationForm()
    signup_form = SignUpForm()
    login_error = None
    signup_error = None
    active_form = None
    # Handle registration POST
    if request.method == 'POST':
        if 'register' in request.POST:
            active_form = 'register'
            signup_form = SignUpForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save(commit=False)
                user.set_password(signup_form.cleaned_data['password'])
                user.save()
                login(request, user)
                return redirect('dashboard')
            else:
                signup_error = signup_form.errors
        elif 'login' in request.POST:
            active_form = 'login'
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = authenticate(
                    username=login_form.cleaned_data['username'],
                    password=login_form.cleaned_data['password']
                )
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    login_error = 'Invalid username or password.'
            else:
                login_error = login_form.errors
    return render(request, 'index.html', {
        'form': login_form,
        'signup_form': signup_form,
        'login_error': login_error,
        'signup_error': signup_error,
        'active_form': active_form
    })

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
