# Generated by Django 4.2.2 on 2023-06-09 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_user_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_profile',
        ),
    ]
