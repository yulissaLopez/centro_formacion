# Generated by Django 5.1.4 on 2024-12-13 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
