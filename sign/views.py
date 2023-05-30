from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm



"""def usual_login_view(request):
    username = request.POST[‘username’]
    password = request.POST[‘password’]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        OneTimeCode.objects.create(code=random.choice('12345'), user=user)
    # send one-time code by email
    # show or redirect to put code page
    else:

    # Error

def login_with_code_view(request):
    username = request.POST[‘username’]
    code = request.POST[‘code’]
    if OneTimeCode.objects.filter(code=code, user__username=username).exists():
        login(request, user)
    else:
        print('Error')"""


# Create your views here.
