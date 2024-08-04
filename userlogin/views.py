from django.shortcuts import render

def home(request):
    return render(request, 'login.html')
def forgot(request):
    return render(request, 'forgot-password.html')

def reset(request):
    return render(request, 'reset-password.html')