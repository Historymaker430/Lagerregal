# Generated by Django 2.0.13 on 2019-05-08 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_theme_blank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lageruser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
