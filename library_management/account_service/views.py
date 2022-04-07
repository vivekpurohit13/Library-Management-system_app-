from tkinter.tix import Form
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import UserAdminCreationForm
from .models import CustomUser

def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    return render(req,'register.html', {'form': form})

def logout_view(req):
    logout(req)
    return redirect('/')
