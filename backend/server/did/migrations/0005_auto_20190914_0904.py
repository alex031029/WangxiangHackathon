# Generated by Django 2.2 on 2019-09-14 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('did', '0004_auto_20190914_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
