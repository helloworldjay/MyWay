from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'forwardhead/index.html', {})

def contact(request):
    return render(request,'forwardhead/contact.html', {})

def get_fhp_ex(request):
    return render(request, "fhp_explain.html", {})