# Generated by Django 4.2.2 on 2023-06-08 14:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_rename_condition_article_etat_remove_article_auteur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
