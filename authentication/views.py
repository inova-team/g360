from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect


# Create your views here.
from authentication.models import Staff


def renderLogin(request):
    if request.user.is_authenticated:
        return redirect('intranet')

    if request.POST:

        dataFromHTML = request.POST
        username = dataFromHTML['username']
        password = dataFromHTML['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:  # Succesful login
            login(request, user)
            return redirect('intranet')
        else:  # Unsuccesul login
            context = {
                'failLogin': 1
            }
            # logout(request)
            return render(request, 'authentication/login.html', context)

    context = {
        'failLogin': 0,
        'title_page': 'Login',
        'is_active_login': 'active'
    }
    return render(request, 'authentication/login.html', context)


def renderRegister(request):
    context = {
        'flagRegisterFail': 0,
        'flagExistingUser': 0,
    }

    if request.POST:

        dataFromHTML = request.POST
        firstname = dataFromHTML['firstname']
        lastname = dataFromHTML['lastname']
        email = dataFromHTML['email']
        password = dataFromHTML['password']
        confirm_password = dataFromHTML['confirmPassword']

        if password == confirm_password:
            if User.objects.filter(email=email).count() == 0:  # No existing user
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=email,
                                                password=password, email=email)
                group = Group.objects.get(name="Member")
                group.user_set.add(user)

                staff = Staff()
                staff.user = user
                staff.save()

                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')

            else:  # Already existing user
                context['flagExistingUser'] = 1
                return render(request, "authentication/register.html", context)
        else:
            context['flagRegisterFail'] = 1
            return render(request, "authentication/register.html", context)
    return render(request, 'authentication/register.html', context)


def renderLogout(request):
    if not request.user.is_authenticated:
        return redirect('home')

    logout(request)
    return redirect('home')