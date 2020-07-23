from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def signup(request):
    if request.method == 'POST':
        # >>-----Form submitted for processing------<<

        if request.POST['password1'] == request.POST['password2']:

            # >>>---Password matched, check username availability----<<<
            try:
                user = User.objects.get(username=request.POST['username'])
                context = {
                    'error': 'Username is taken. Please try some other username.'}
                return render(request, 'users/signup.html', context)

            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])

                # >>------- Registration Successful, log user in ---------<<
                auth.login(request, user)

                # >>-------Login successful, back to home-------<<
                return redirect('products:home')
        else:
            context = {
                'error': "Passwords don't match."}
            return render(request, 'users/signup.html', context)

    else:
        # >>--------- Display page -----------<<
        return render(request, 'users/signup.html', context=None)


def signin(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('products:home')
        else:
            context = {'error': 'Incorrect username or password.'}
            return render(request, 'users/signin.html', context)
    else:
        return render(request, 'users/signin.html', context=None)


def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('products:home')
