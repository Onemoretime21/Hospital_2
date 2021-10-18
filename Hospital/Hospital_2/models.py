from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Hospitals(models.Model):
    region_dic = (
          ('bishkek','Бишкек'),
          ('chuy','Чуй'),
          ('talas', 'Талас'),
          ('osh','Ош'),
          ('batken', 'Баткен'),
          ('naryn','Нарын'),
          ('djalal','Джалал-Абад'),
          ('issyk','Иссык-куль')
    )
    hospital_name = models.CharField(max_length=200, verbose_name='Название больницы', unique=True)
    region_of_hospital = models.CharField(max_length=25, choices=region_dic, default='', verbose_name='Регион бальницы')
    count_of_staff = models.IntegerField(default=1, validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ], verbose_name='Кол-во сотрудников', help_text='Максимум 100')
    type_of_hospital = models.BooleanField(default=True, verbose_name='Тип больницы', help_text='Если больница государственная то 1, иначе 0')

    #Строчное отображение нашего объекта, а точнее его лицо выбираем поле
    def __str__(self):
        return f'{self.hospital_name}'



class HeadOfDoctors(models.Model):
    hospitalForHead_id = models.OneToOneField(Hospitals, on_delete=models.CASCADE, verbose_name='Название больницы')
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Привязка к user')
    full_name = models.CharField(max_length=255, verbose_name="ФИО Главврача")
    passport_pin = models.IntegerField(null=True, verbose_name="ПИН-КОД паспорта")
    age = models.IntegerField(null=True, verbose_name='Возраст')
    experience = models.CharField(max_length=10, verbose_name='Стаж работы')
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона')

    def __str__(self):
        return f'{self.full_name}'

class Doctor(models.Model):
    headOfDoctors_id = models.ForeignKey(HeadOfDoctors, on_delete=models.CASCADE, verbose_name='ФИО главрача')
    type_doctor_dic = (('hirurg', 'хирург'), ('terapevt', 'терапевт'))
    type_of_doctor = models.CharField(max_length=10, default='', choices=type_doctor_dic, verbose_name='Направление')
    full_name = models.CharField(max_length=255, verbose_name="ФИО врача")
    passport_pin = models.IntegerField(null=True, verbose_name="ПИН-КОД паспорта")
    age = models.IntegerField(null=True, verbose_name='Возраст')
    experience = models.CharField(max_length=10, verbose_name='Стаж работы')
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона')

    def __str__(self):
        return f'{self.type_of_doctor}'

class Nure(models.Model):
    nurseForDoctors_id = models.OneToOneField(Doctor, on_delete=models.CASCADE, verbose_name='ФИО врача')
    full_name = models.CharField(max_length=255, verbose_name="ФИО медсестры")
    passport_pin = models.IntegerField(null=True, verbose_name="ПИН-КОД паспорта")
    age = models.IntegerField(null=True, verbose_name='Возраст')
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона')

    def __str__(self):
        return f'{self.full_name}'

class Patient(models.Model):
    doctorForPatient_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='ФИО лечащего врача')
    nure_id = models.ForeignKey(Nure, on_delete=models.PROTECT, verbose_name='ФИО пациента')
    full_name = models.CharField(max_length=255, verbose_name="ФИО медсестры")
    passport_pin = models.IntegerField(null=True, verbose_name="ПИН-КОД паспорта")
    age = models.IntegerField(null=True, verbose_name='Возраст')
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона')
    reason = models.CharField(max_length=100, verbose_name='Причина обращения в больницу')

    def __str__(self):
        return f'{self.full_name}'



