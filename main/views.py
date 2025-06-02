
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

def home(request):
    template_name = 'main/home.html'
    return render(request, template_name)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # or render a success template
    else:
        form = ContactForm()
    return render(request, 'main/forms.html', {'form': form})

def skills(request):
    context = {
        'skills': ['python', 'django', 'html', 'css']
    }
    template_name = 'main/skills.html'
    return render(request, template_name, context)


