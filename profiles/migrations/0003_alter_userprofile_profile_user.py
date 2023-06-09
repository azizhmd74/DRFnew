# Generated by Django 4.2.2 on 2023-06-09 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_alter_userprofile_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]