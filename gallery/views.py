from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ChildForm, ArtworkForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Child, Artwork

def index(request):
    # Show landing page with login/register forms if not logged in
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
                messages.success(request, f'Welcome to Art-Hive, {user.username}! 🐝')
                return redirect('index')  # Redirect after registration
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
                    messages.success(request, f'Welcome back, {user.username}! 🐝')
                    return redirect('index')  # Redirect after login
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
    # Query all children for the logged-in parent
    children = Child.objects.filter(parent=request.user)
    return render(request, 'dashboard.html', {'children': children})

@login_required
def add_child(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.parent = request.user  # Set parent to logged-in user
            child.save()
            messages.success(request, f"Child '{child.name}' added!")
            return redirect('dashboard')
    else:
        form = ChildForm()
    return render(request, 'add_child.html', {'form': form})

@login_required
def edit_child(request, child_id):
    child = get_object_or_404(Child, id=child_id, parent=request.user)
    if request.method == 'POST':
        form = ChildForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
            messages.success(request, f"Child '{child.name}' updated!")
            return redirect('dashboard')
    else:
        form = ChildForm(instance=child)
    return render(request, 'edit_child.html', {'form': form, 'child': child})

@login_required
def delete_child(request, child_id):
    child = get_object_or_404(Child, id=child_id, parent=request.user)
    if request.method == 'POST':
        child.delete()
        messages.success(request, f"Child '{child.name}' deleted!")
        return redirect('dashboard')
    return render(request, 'delete_child.html', {'child': child})

@login_required
def add_artwork(request, child_id):
    child = get_object_or_404(Child, id=child_id, parent=request.user)
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.child = child
            artwork.save()
            messages.success(request, f"Artwork '{artwork.title}' added for {child.name}!")
            return redirect('gallery', child_id=child.id)  # Redirect to gallery after adding artwork
    else:
        form = ArtworkForm()
    return render(request, 'add_artwork.html', {'form': form, 'child': child})

@login_required
def gallery(request, child_id):
    child = get_object_or_404(Child, id=child_id, parent=request.user)
    artworks = child.artworks.all()
    return render(request, 'gallery.html', {'child': child, 'artworks': artworks})

@login_required
def edit_artwork(request, child_id, artwork_id):
    child = get_object_or_404(Child, id=child_id, parent=request.user)
    artwork = get_object_or_404(Artwork, id=artwork_id, child=child)
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            messages.success(request, f"Artwork '{artwork.title}' updated!")
            return redirect('gallery', child_id=child.id)
    else:
        form = ArtworkForm(instance=artwork)
    return render(request, 'edit_artwork.html', {'form': form, 'child': child, 'artwork': artwork})

@login_required
def delete_artwork(request, child_id, artwork_id):
    """Confirm and delete an artwork belonging to the current user's child."""
    child = get_object_or_404(Child, id=child_id, parent=request.user)
    artwork = get_object_or_404(Artwork, id=artwork_id, child=child)
    if request.method == 'POST':
        title = artwork.title
        # Try to delete underlying asset (e.g., Cloudinary) without saving model
        try:
            if getattr(artwork, 'image', None):
                artwork.image.delete(save=False)
        except Exception:
            pass
        artwork.delete()
        messages.success(request, f"Artwork '{title}' deleted!")
        return redirect('gallery', child_id=child.id)
    return render(request, 'delete_artwork.html', {'child': child, 'artwork': artwork})

def custom_logout(request):
    """Custom logout view to add a success message."""
    from django.contrib.auth import logout
    logout(request)
    messages.success(request, 'You have been logged out. See you soon! 🐝')
    return redirect('index')
