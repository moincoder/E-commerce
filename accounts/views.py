from django.shortcuts import render

# Create your views here.


def login_view(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def my_account(request):
    return render(request,'my_account.html')