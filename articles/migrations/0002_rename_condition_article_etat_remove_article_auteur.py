# Generated by Django 4.2.2 on 2023-06-08 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='condition',
            new_name='Etat',
        ),
        migrations.RemoveField(
            model_name='article',
            name='auteur',
        ),
    ]
