from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Project
from .forms import ContactForm


def home(request):
    projects = Project.objects.all()
    return render(request, "portfolio/home.html", {"projects": projects})


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')
        else:
            response = HttpResponse('<h1>Invalid form</h1>')
            response.status_code = 400
            return response
    else:
        form = ContactForm()

    return render(request, "portfolio/contacts.html", {'form': form})


