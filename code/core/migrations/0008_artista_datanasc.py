# Generated by Django 4.0.2 on 2023-02-14 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_artista_datanasc'),
    ]

    operations = [
        migrations.AddField(
            model_name='artista',
            name='dataNasc',
            field=models.DateTimeField(default='date published'),
        ),
    ]
