# Generated by Django 4.1.1 on 2022-10-06 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bezero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bezero',
            name='adina',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
