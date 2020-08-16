from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            firstname = form.cleaned_data.get('first_name')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            confirm = form.cleaned_data.get('confirm')
            if (raw_password == confirm):
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'sinauBS/register.html', {
                    "form": form,
                    "message": "Pass Confirm Wrong" 
                    })
    else:
        form = UserCreationForm()
    return render(request, 'sinauBS/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "sinauIndex/login.html", {
                "message": "Not Found"
            })
    return render(request, "sinauIndex/login.html")

def logout_view(request):
    logout(request)
    return render(request, "sinauIndex/login.html", {
        "message": "Keluar"
})
