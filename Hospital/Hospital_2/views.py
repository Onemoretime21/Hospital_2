from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def index(request):
    hospital_info = Hospitals.objects.all(),
    headofdoctors_info = HeadOfDoctors.objects.all(),
    doctor_info = Doctor.objects.all(),
    context = {
        'hospital_info': hospital_info,
        'headofdoctors_info': headofdoctors_info,
        'doctor_info': doctor_info
    }
    return render(request, 'Hospital_2/index.html', context=context)


def hospital_detail(request):
    hospital_info = Hospitals.objects.all(),
    headofdoctors_info = HeadOfDoctors.objects.all(),
    doctor_info = Doctor.objects.all(),
    nure_info = Nure.objects.all()
    context = {
        'hospital_info': hospital_info,
        'headofdoctors_info': headofdoctors_info,
        'doctor_info': doctor_info,
        'nure_info': nure_info,
    }
    return render(request, 'Hospital_2/hospital1.html', context=context)

