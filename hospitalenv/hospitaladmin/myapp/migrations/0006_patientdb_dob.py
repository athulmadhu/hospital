# Generated by Django 5.0.4 on 2024-06-01 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdb',
            name='dob',
            field=models.CharField(default='1/1/1990', max_length=200),
        ),
    ]