from django.shortcuts import render

# Create your views here.
def get_home(request):
    return render(request, 'base.html', {})

def get_contact(request):
    return render(request, 'contact.html', {})