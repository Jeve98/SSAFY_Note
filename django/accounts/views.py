from django.shortcuts import render, redirect
# built-in form
from django.contrib.auth.forms import AuthenticationForm
# session 생성
from django.contrib.auth import login as auth_login

# Create your views here.
def login(request):
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