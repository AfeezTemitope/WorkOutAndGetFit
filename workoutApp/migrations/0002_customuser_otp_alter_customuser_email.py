# Generated by Django 5.1.5 on 2025-01-14 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workoutApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='otp',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
