from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    hp = Hospitals.objects.all()
    context = {
        "Hospital": hp
    }
    return render(request, template_name='Hospital_2/index.html', context=context)