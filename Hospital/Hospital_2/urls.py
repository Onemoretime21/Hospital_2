from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('hospital/1/', views.hospital_detail, name='hospital_detail')

]