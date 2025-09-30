from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.http import HttpResponse
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def index(request):
    return HttpResponse("infinite robux By Salah, 7<br>make me the best player at 99 nights in the forest by Inaayah, 5")
