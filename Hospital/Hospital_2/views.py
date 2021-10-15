from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    ln = LatestNews.objects.all()
    context = {
        "qwe": ln
    }
    return render(request, template_name='Hospital_2/index.html', context=context)