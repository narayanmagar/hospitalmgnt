from django.shortcuts import render, redirect

# Create your views here.
from .forms import RegisterForm

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def role_redirect_view(request):
    user = request.user

    if user.role == 'ADMIN':
        return redirect('/admin-dashboard/')
    elif user.role == 'DOCTOR':
        return redirect('/doctor-dashboard/')
    elif user.role == 'NURSE':
        return redirect('/nurse-dashboard/')
    elif user.role == 'RECEPTIONIST':
        return redirect('/reception-dashboard/')
    else:
        return redirect('/accounts/login/')




def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

