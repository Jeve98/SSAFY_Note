from django.shortcuts import render, redirect
# built-in form
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
# session 생성
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
# 데코레이터
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # session 생성
            auth_login(request, form.get_user())
            
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    # session delete
    auth_logout(request)

    return redirect('articles:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # 자동 로그인
            user = form.save()
            auth_login(request, user)

            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/signup.html', context)


@login_required
def signout(request):
    request.user.delete()

    auth_logout(request)
    
    return redirect('articles:index')


def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        'form': form,
    }

    return render(request, 'accounts/update.html', context)


def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()

            # 세션 무효화 방지
            update_session_auth_hash(request, user)

            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form,
    }

    return render(request, 'accounts/password.html', context)