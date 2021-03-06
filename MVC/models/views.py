from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# Registration
def register(request):
    if request.user.is_authenticated:
        return redirect("view:home")
    else:
        if request.method == "POST":
            form_class = RegistrationForm
            form = RegistrationForm(request.POST or None)
            # Check if the is valid
            if form.is_valid():
                user = form.save()

                # get the raw password
                raw_password = form.cleaned_data.get('password1')

                # authenticate the user
                user = authenticate(username=user.username, password=raw_password)

                # login the user
                login(request, user)

                return redirect("view:home")
        else:
            form_class = RegistrationForm
            form = RegistrationForm()
        return render(request, "models/register.html", {"form": form})


# login
def login_user(request):
    if request.user.is_authenticated:
        return redirect("view:home")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            # check the credentials
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("view:home")
                else:
                    return render(request, 'models/login.html', {"error": "Your account has been disabled."})
            else:
                return render(request, 'models/login.html', {"error": "Invalid Username or Password. Try Again."})
        return render(request, 'models/login.html')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        print("Logged out successfully.")
        return redirect("models:login")
    else:
        return redirect("models:login")
