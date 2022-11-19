# Generated by Django 4.1.2 on 2022-11-19 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_alter_estudiante_email_alter_profesor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='email',
            field=models.EmailField(error_messages={'unique': 'El email ya está registrado'}, max_length=254, unique=True),
        ),
    ]
