# Generated by Django 2.2 on 2019-09-14 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('did', '0003_auto_20190914_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='credential',
            name='sig',
            field=models.CharField(max_length=200),
        ),
    ]
