from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('blog-home')

    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form, 'title': 'Register'})

def profile(request):
    return render(request, 'users/profile.html', {'title': 'Profile'})