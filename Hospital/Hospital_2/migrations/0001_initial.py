from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(

            name='Hospitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital', models.CharField(max_length=200)),
                ('main_doctor', models.CharField(max_length=200)),
                ('hirurg', models.CharField(max_length=200)),
                ('terapevt', models.CharField(max_length=200)),
                ('medsestra', models.CharField(max_length=200)),
                ('pasienty', models.CharField(max_length=200)),
            ]

    )
]
