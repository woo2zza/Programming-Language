from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
# Create your views here.

@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')

    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)
        

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('movies:index')
    

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
        
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        auth_logout(request)
        return redirect('movies:index')
    return render(request, 'accounts/delete.html')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', context)

@require_http_methods(['GET', 'POST'])
def profile(request, username):
    user = get_user_model()
    person = user.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request , 'accounts/profile.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def follow(request, user_pk):
    you = get_object_or_404(get_user_model(), pk=user_pk)
    me = request.user

    if request.method == 'POST':
        if me != you:
            if me in you.followers.all():
                you.followers.remove(me)
            else:
                you.followers.add(me)
        return redirect('accounts:profile', you.username)
    else:
        followers = you.followers.all()
        followings = you.followings.all()

        context = {
            'you': you,
            'followers': followers,
            'followings': followings,
        }
        return render(request, 'accounts/follow_list.html', context)