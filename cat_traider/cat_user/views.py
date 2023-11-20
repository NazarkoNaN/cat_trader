from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.http import HttpResponseRedirect

@login_required(login_url="login")
def user_page_view(response):
    data = {
        "username": response.user.username
    }
    return render(response, "cat_user/user-page.html", data)


def user_log_out_view(response):
    logout(response)
    return redirect("home")


def user_log_in_view(response):
    #Check if user is already loged in
    if response.user.is_authenticated:
        return redirect("user_page")

    #Log in proces
    if response.method == "POST":
        username = response.POST["username"]
        password = response.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(response, user)
            return redirect("user_page")
        else:
            pass

    #Render login.html if it is not POST method
    return render(response, "cat_user/login.html")


def user_register_view(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("user_page")
    else:
        form = RegisterForm()

    return render(response, "cat_user/register.html", {"form":form})