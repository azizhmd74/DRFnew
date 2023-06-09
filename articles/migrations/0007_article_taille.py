# Generated by Django 4.2.2 on 2023-06-08 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_rename_created_at_article_date_cr'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='taille',
            field=models.CharField(choices=[('', 'None'), ('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Double Extra Large'), ('XXXL', 'Triple Extra Large')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]